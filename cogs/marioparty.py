#***************************************************************************#
#                                                                           #
# Underground Grotto Bot                                                    #
# Mario Party Commands                                                      #
# Copyright (C) 2024-2025 Tabitha Hanegan. All rights reserved.            #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

import discord
import urllib
import asyncio
from discord.ext import commands
from discord import SlashCommandGroup
from discord.ui import Modal
from util.wheel import generate_wheel_gif

class MarioParty(commands.Cog):

    """Cog for Mario Party commands"""

    def __init__(self, bot):
        self.bot = bot
        # Store eliminated boards per channel and game
        self.eliminated_boards = {}
        # Store eliminated games per channel
        self.eliminated_games = {}

    board = SlashCommandGroup("board", "MP Board related commands")

    async def spin_generic_elimination(self, ctx, options_list, final_title):
        """Handles survivor-style elimination for generic options."""
        remaining = options_list.copy()
        
        await ctx.respond(f"🎲 Starting elimination process with {len(remaining)} options!", delete_after=3)
        await asyncio.sleep(2)
        
        while len(remaining) > 1:
            loop = asyncio.get_running_loop()
            selected, gif_io, _ = await loop.run_in_executor(None, generate_wheel_gif, remaining)
            
            remaining.remove(selected)
            left = len(remaining)
            
            gif_file = discord.File(gif_io, "spinning_wheel.gif")
            status_msg = await ctx.send(f"🎯 Spinning... ({left + 1} remaining)")
            gif_msg = await ctx.send(file=gif_file)
            
            await asyncio.sleep(5)
            await gif_msg.delete()
            await status_msg.delete()
            
            result_embed = discord.Embed(
                title=f"❌ Eliminated: {selected}",
                description=f"**{left}** remaining",
                colour=0xFF6B6B
            )
            await ctx.send(embed=result_embed)
            
            if left > 1:
                await asyncio.sleep(3)
                
        winner = remaining[0]
        _, _, final_img_io = generate_wheel_gif([winner])
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        
        winner_embed = discord.Embed(
            title=f"🏆 WINNER: {winner}!",
            description=final_title,
            colour=0x98FB98
        )
        winner_embed.set_image(url="attachment://final_wheel.png")
        await ctx.send(embed=winner_embed, file=final_image_file)

    async def spin_wheel_and_show_result(self, ctx, options, title, description, elimination: bool = False, image_path=None, filename=None):
        """Generic function to spin wheel and show result with embed."""
        if elimination and len(options) > 1:
            await self.spin_generic_elimination(ctx, options, title)
            return

        # Defer immediately to avoid interaction timeout
        await ctx.defer()
        
        # Use the wheel system - get both GIF and final image
        loop = asyncio.get_running_loop()
        selected, gif_io, _ = await loop.run_in_executor(None, generate_wheel_gif, options)

        # Send the GIF as a follow-up
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.followup.send(file=gif_file)

        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()
        
        # Generate final wheel with ONLY the winner (like elimination results)
        _, _, final_img_io = generate_wheel_gif([selected])
        
        # Create embed with the final wheel - all in one
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        result_embed = discord.Embed(
            title=f"🏆 WINNER: {selected}!",
            description=title,
            colour=0x98FB98
        )
        result_embed.set_image(url="attachment://final_wheel.png")
        
        # Send everything in one message as follow-up
        await ctx.followup.send(embed=result_embed, file=final_image_file)

    async def spin_game_wheel(self, ctx, gameList, category_name, elimination: bool = False):
        """Helper function to spin the wheel for game selection with elimination."""
        if not elimination:
            await self.spin_wheel_and_show_result(ctx, gameList, "🏆 Random Game Selected!", "game selection")
            return

        channel_id = ctx.channel.id
        
        # Initialize channel tracking if needed
        if channel_id not in self.eliminated_games:
            self.eliminated_games[channel_id] = {}
        if category_name not in self.eliminated_games[channel_id]:
            self.eliminated_games[channel_id][category_name] = []
        
        eliminated = self.eliminated_games[channel_id][category_name]
        remaining_games = [game for game in gameList if game not in eliminated]
        
        if len(remaining_games) == 0:
            self.eliminated_games[channel_id][category_name] = []
            remaining_games = gameList.copy()
            await ctx.respond("🔄 All games have been played! Starting new elimination round...", delete_after=3)
            await asyncio.sleep(2)
        
        total_games = len(remaining_games)
        await ctx.respond(f"🎲 Starting elimination process with {total_games} game{'s' if total_games != 1 else ''}!", delete_after=3)
        await asyncio.sleep(2)
        
        while len(remaining_games) > 1:
            selected_game, gif_io, final_img_io = generate_wheel_gif(remaining_games)
            self.eliminated_games[channel_id][category_name].append(selected_game)
            remaining_games = [game for game in remaining_games if game != selected_game]
            games_left = len(remaining_games)
            
            gif_file = discord.File(gif_io, "spinning_wheel.gif")
            status_msg = await ctx.send(f"🎯 Spinning... ({int(games_left + 1)} game{'s' if games_left != 1 else ''} remaining)")
            gif_msg = await ctx.send(file=gif_file)

            await asyncio.sleep(5)
            await gif_msg.delete()
            await status_msg.delete()

            result_embed = discord.Embed(
                title=f"❌ Eliminated: {selected_game}",
                description=f"**{games_left}** game{'s' if games_left != 1 else ''} remaining",
                colour=0xFF6B6B
            )
            await ctx.send(embed=result_embed)
            if games_left > 1:
                await asyncio.sleep(3)
        
        winner = remaining_games[0]
        _, _, final_img_io = generate_wheel_gif([winner])
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        
        winner_embed = discord.Embed(
            title=f"🏆 WINNER: {winner}!",
            description=f"**The last game standing!**\nThis is your game for today!",
            colour=0x98FB98
        )
        winner_embed.set_image(url="attachment://final_wheel.png")
        await ctx.send(embed=winner_embed, file=final_image_file)
        self.eliminated_games[channel_id][category_name] = []

    async def spin_board_wheel(self, ctx, boardList, game_name, elimination: bool = False):
        """Helper function to spin the wheel for any Mario Party game board with elimination."""
        if not elimination:
            # Single spin fallback
            await ctx.defer()
            loop = asyncio.get_running_loop()
            winner, gif_io, _ = await loop.run_in_executor(None, generate_wheel_gif, boardList)
            
            gif_file = discord.File(gif_io, "spinning_wheel.gif")
            message = await ctx.followup.send(file=gif_file)
            await asyncio.sleep(5)
            await message.delete()
            
            try:
                board_file = discord.File(f"boards/{game_name}/{winner}.png", filename="board.png")
                winner_embed = discord.Embed(title=f"🏆 WINNER: {winner}!", description="**This is your board for today!**", colour=0x98FB98)
                winner_embed.set_image(url="attachment://board.png")
                await ctx.followup.send(embed=winner_embed, file=board_file)
            except FileNotFoundError:
                _, _, final_img_io = generate_wheel_gif([winner])
                final_image_file = discord.File(final_img_io, "final_wheel.png")
                winner_embed = discord.Embed(title=f"🏆 WINNER: {winner}!", description="**This is your board for today!**", colour=0x98FB98)
                winner_embed.set_image(url="attachment://final_wheel.png")
                await ctx.followup.send(embed=winner_embed, file=final_image_file)
            return

        channel_id = ctx.channel.id
        if channel_id not in self.eliminated_boards:
            self.eliminated_boards[channel_id] = {}
        if game_name not in self.eliminated_boards[channel_id]:
            self.eliminated_boards[channel_id][game_name] = []
        
        eliminated = self.eliminated_boards[channel_id][game_name]
        remaining_boards = [board for board in boardList if board not in eliminated]
        
        if len(remaining_boards) == 0:
            self.eliminated_boards[channel_id][game_name] = []
            remaining_boards = boardList.copy()
            await ctx.respond("🔄 All boards have been played! Starting new elimination round...", delete_after=3)
            await asyncio.sleep(2)
        
        total_boards = len(remaining_boards)
        await ctx.respond(f"🎲 Starting elimination process with {total_boards} boards!", delete_after=3)
        await asyncio.sleep(2)
        
        while len(remaining_boards) > 1:
            selected_board, gif_io, final_img_io = generate_wheel_gif(remaining_boards)
            self.eliminated_boards[channel_id][game_name].append(selected_board)
            remaining_boards = [board for board in remaining_boards if board != selected_board]
            boards_left = len(remaining_boards)
            
            gif_file = discord.File(gif_io, "spinning_wheel.gif")
            status_msg = await ctx.send(f"🎯 Spinning... ({boards_left} board{'s' if boards_left != 1 else ''} remaining)")
            gif_msg = await ctx.send(file=gif_file)

            await asyncio.sleep(5)
            await gif_msg.delete()
            await status_msg.delete()

            result_embed = discord.Embed(
                title=f"❌ Eliminated: {selected_board}",
                description=f"**{boards_left}** board{'s' if boards_left != 1 else ''} remaining",
                colour=0xFF6B6B
            )
            await ctx.send(embed=result_embed)
            if boards_left > 1:
                await asyncio.sleep(3)
        
        winner = remaining_boards[0]
        try:
            board_file = discord.File(f"boards/{game_name}/{winner}.png", filename="board.png")
            winner_embed = discord.Embed(
                title=f"🏆 WINNER: {winner}!",
                description=f"**The last board standing!**\nThis is your board for today!",
                colour=0x98FB98
            )
            winner_embed.set_image(url="attachment://board.png")
            await ctx.send(embed=winner_embed, file=board_file)
        except FileNotFoundError:
            _, _, final_img_io = generate_wheel_gif([winner])
            final_image_file = discord.File(final_img_io, "final_wheel.png")
            winner_embed = discord.Embed(
                title=f"🏆 WINNER: {winner}!",
                description=f"**The last board standing!**\nThis is your board for today!",
                colour=0x98FB98
            )
            winner_embed.set_image(url="attachment://final_wheel.png")
            await ctx.send(embed=winner_embed, file=final_image_file)
        
        self.eliminated_boards[channel_id][game_name] = []


    # Game selection commands
    @commands.slash_command(name="pickgame", description="Random Mario Party game")
    async def pickgame(self, ctx, elimination: bool = False):
        games = [f"Mario Party {i}" for i in range(1, 9)]
        await self.spin_game_wheel(ctx, games, "all_games", elimination)

    @commands.slash_command(name="pickgcwii", description="Random GC/Wii Mario Party game")
    async def pickgcwii(self, ctx, elimination: bool = False):
        games = [f"Mario Party {i}" for i in range(4, 9)]
        await self.spin_game_wheel(ctx, games, "gcwii_games", elimination)

    @commands.slash_command(name="pickn64", description="Random N64 Mario Party game")
    async def pickn64(self, ctx, elimination: bool = False):
        games = [f"Mario Party {i}" for i in range(1, 4)]
        await self.spin_game_wheel(ctx, games, "n64_games", elimination)

    @commands.slash_command(name="pickdxmode", description="Random Mario Party version")
    async def pickDXmode(self, ctx, elimination: bool = False):
        modes = ["Vanilla", "DX"]
        await self.spin_wheel_and_show_result(ctx, modes, "🎯 Mario Party Version Selected!", "DX or vanilla version", elimination=elimination)

    # Settings commands
    @commands.slash_command(name="bonusstars", description="Random bonus stars setting")
    async def bstars(self, ctx, elimination: bool = False):
        options = ["Off", "On", "Ztars"]
        await self.spin_wheel_and_show_result(ctx, options, "⭐ Bonus Stars Setting Selected!", "bonus stars setting", elimination=elimination)

    @commands.slash_command(name="duels", description="Samee space duels")
    async def samespaceduels(self, ctx, elimination: bool = False):
        options = ["Always", "Vanilla", "Never"]
        await self.spin_wheel_and_show_result(ctx, options, "⚔️ Same Space Duels Setting Selected!", "duels setting", elimination=elimination)

    @commands.slash_command(name="gentlemans", description="Random gentleman's rule setting")
    async def gentlemans(self, ctx, elimination: bool = False):
        options = ["On", "Off"]
        await self.spin_wheel_and_show_result(ctx, options, "🎩 Gentleman's Rule Setting Selected!", "gentlemans rule setting", elimination=elimination)

    @commands.slash_command(name="stealchoice", description="Random steal choice setting")
    async def stealduels(self, ctx, elimination: bool = False):
        options = ["Choose", "Random"]
        await self.spin_wheel_and_show_result(ctx, options, "🎯 Steal Choice Setting Selected!", "steal choice setting", elimination=elimination)

    @commands.slash_command(name="duelchoice", description="Random duel choice setting")
    async def stealduel(self, ctx, elimination: bool = False):
        options = ["Choose", "Random"]
        await self.spin_wheel_and_show_result(ctx, options, "🎯 Duel Choice Setting Selected!", "duel choice setting", elimination=elimination)

    @board.command(name='1')
    async def one(self, ctx, elimination: bool = False):
        """Spins a wheel to randomly pick a Mario Party 1 board."""
        boardList = [
            "DK's Jungle Adventure", "Peach's Birthday Cake", "Yoshi's Tropical Island", 
            "Mario's Rainbow Castle", "Wario's Battle Canyon", "Luigi's Engine Room", 
            "Eternal Star", "Bowser's Magma Mountain"
        ]
        await self.spin_board_wheel(ctx, boardList, "1", elimination)

    @board.command(name='2')
    async def two(self, ctx, elimination: bool = False):
        boardList = ["Western Land", "Space Land", "Mystery Land", "Pirate Land", "Horror Land", "Bowser Land"]
        await self.spin_board_wheel(ctx, boardList, "2", elimination)

    @board.command(name='3')
    async def three(self, ctx, elimination: bool = False):
        boardList = ["Chilly Waters", "Deep Bloober Sea", "Woody Woods", "Creepy Cavern", "Spiny Desert", "Waluigi's Island"]
        await self.spin_board_wheel(ctx, boardList, "3", elimination)

    @board.command(name='4')
    async def four(self, ctx, elimination: bool = False):
        boardList = ["Toad's Midway Madness", "Boo's Haunted Bash", "Koopa's Seaside Soiree", "Goomba's Greedy Gala", "Shy Guy's Jungle Jam", "Bowser's Gnarly Party"]
        await self.spin_board_wheel(ctx, boardList, "4", elimination)

    @board.command(name='5')
    async def five(self, ctx, elimination: bool = False):
        boardList = ["Toy Dream", "Rainbow Dream", "Pirate Dream", "Future Dream", "Undersea Dream", "Sweet Dream", "Bowser's Nightmare"]
        await self.spin_board_wheel(ctx, boardList, "5", elimination)

    @board.command(name='6')
    async def six(self, ctx, elimination: bool = False):
        boardList = ["Towering Treetop", "E Gadd's Garage", "Faire Square", "Snowflake Lake", "Castaway Bay", "Clockwork Castle"]
        await self.spin_board_wheel(ctx, boardList, "6", elimination)

    @board.command(name='7')
    async def seven(self, ctx, elimination: bool = False):
        boardList = ["Grand Canal", "Pagoda Peak", "Pyramid Park", "Neon Heights", "Windmillville", "Bowser's Enchanted Inferno"]
        await self.spin_board_wheel(ctx, boardList, "7", elimination)

    @board.command(name='8')
    async def eight(self, ctx, elimination: bool = False):
        boardList = ["DK's Treetop Temple", "Goomba's Booty Boardwalk", "King Boo's Haunted Hideaway", "Shy Guy's Perplex Express", "Koopa's Tycoon Town", "Bowser's Warped Orbit"]
        await self.spin_board_wheel(ctx, boardList, "8", elimination)

    @board.command(name='9')
    async def nine(self, ctx, elimination: bool = False):
        boardList = ["Toad Road", "Blooper Beach", "Boo's Horror Castle", "DK's Jungle Ruins", "Bowser's Station", "Magma Mine", "Bob-omb Factory"]
        await self.spin_board_wheel(ctx, boardList, "9", elimination)

    @board.command(name='10')
    async def ten(self, ctx, elimination: bool = False):
        boardList = ["Mushroom Park", "Whimsical Waters", "Chaos Castle", "Airship Central", "Haunted Trail"]
        await self.spin_board_wheel(ctx, boardList, "10", elimination)

    @board.command()
    async def ds(self, ctx, elimination: bool = False):
        boardList = ["Wiggler's Garden", "Kamek's Library", "Bowser's Pinball Machine", "Toadette's Music Room", "DK's Stone Statue"]
        await self.spin_board_wheel(ctx, boardList, "DS", elimination)

    @board.command(name='super')
    async def super(self, ctx, elimination: bool = False):
        boardList = ["Whomp's Domino Ruins", "King Bob-omb's Powderkeg Mine", "Megafruit Paradise", "Kamek's Tantalizing Tower"]
        await self.spin_board_wheel(ctx, boardList, "Super", elimination)

    @board.command(name='superstars')
    async def superstars(self, ctx, elimination: bool = False):
        boardList = ["Yoshi's Tropical Island", "Peach's Birthday Cake", 'Space Land', 'Horror Land', 'Woody Woods']
        await self.spin_board_wheel(ctx, boardList, "Superstars", elimination)

    @board.command(name='jamboree')
    async def jamboree(self, ctx, elimination: bool = False):
        boardList = ["Mega Wiggler's Tree Party", "Rainbow Galleria", 'Goomba Lagoon', "Roll\'em Raceway", 'Western Land', "Mario\'s Rainbow Castle", "King Bowser\'s Keep"]
        await self.spin_board_wheel(ctx, boardList, "Jamboree", elimination)

    @commands.slash_command(name='wheel', description="Spin a wheel with custom options")
    async def wheel(self, ctx, elimination: bool = False):
        """Shows a modal to input wheel options."""
        modal = WheelModal(self, elimination)
        await ctx.send_modal(modal)

class WheelModal(Modal):
    """Modal for entering wheel options."""
    
    def __init__(self, cog, elimination: bool):
        super().__init__(title="Wheel Options")
        self.cog = cog
        self.elimination = elimination
        self.options_input = discord.ui.TextInput(
            label="Options (comma-separated)",
            placeholder="1, 2, 3",
            style=discord.InputTextStyle.paragraph,
            required=True,
            max_length=4000
        )
        self.add_item(self.options_input)
    
    async def callback(self, interaction: discord.Interaction):
        """Handle modal submission."""
        options_text = self.options_input.value.strip()
        
        if not options_text:
            await interaction.response.send_message("❌ Please provide at least one option!", ephemeral=True)
            return
        
        filter_options = [option.strip() for option in options_text.split(',') if option.strip()]
        
        if len(filter_options) < 2:
            await interaction.response.send_message("❌ Please provide at least 2 options for the wheel!", ephemeral=True)
            return
        
        await interaction.response.defer()
        
        class InteractionContext:
            def __init__(self, inter):
                self.interaction = inter
                self.author = inter.user
                self.channel = inter.channel
                self.followup = inter.followup
                
            async def defer(self):
                pass
                
            async def respond(self, content=None, **kwargs):
                return await self.interaction.followup.send(content=content, **kwargs)
            
            async def send(self, content=None, **kwargs):
                return await self.interaction.followup.send(content=content, **kwargs)
        
        ctx = InteractionContext(interaction)
        await self.cog.spin_wheel_and_show_result(ctx, filter_options, f"🎉 The wheel landed on!", "custom wheel", elimination=self.elimination)

def setup(bot):
    bot.add_cog(MarioParty(bot))