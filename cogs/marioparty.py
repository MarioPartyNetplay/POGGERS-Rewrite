#***************************************************************************#
#                                                                           #
# Poggers                                                                   #
# https://github.com/MarioPartyNetplay/Poggers-Rewrite                      #
# Copyright (C) 2024-2025 Tabitha Hanegan. All rights reserved.                     #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

import discord
import random
import urllib
import requests
import re
import asyncio

from bs4 import BeautifulSoup
from discord.ext import commands
from discord import SlashCommandGroup
from util.wheel import generate_wheel_gif

class MarioParty(commands.Cog):

    """Cog for Mario Party commands"""

    def __init__(self, bot):
        self.bot = bot

    board = SlashCommandGroup("board", "MP Board related commands")
    partyplanner = SlashCommandGroup("partyplanner", "Party Planner related commands")

    @board.command(name='1')
    async def one(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 1 board."""
        boardList = [
            "DK's Jungle Adventure", "Peach's Birthday Cake", "Yoshi's Tropical Island", 
            "Mario's Rainbow Castle", "Wario's Battle Canyon", "Luigi's Engine Room", 
            "Eternal Star", "Bowser's Magma Mountain"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)
        
        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/1/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='2')
    async def two(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 2 board."""
        boardList = [
            "Western Land", "Space Land", "Mystery Land", 
            "Pirate Land", "Horror Land", "Bowser Land"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/2/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='3')
    async def three(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 3 board."""
        boardList = [
            "Chilly Waters", "Deep Bloober Sea", "Woody Woods", 
            "Creepy Cavern", "Spiny Desert", "Waluigi's Island"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/3/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='4')
    async def four(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 4 board."""
        boardList = [
            "Toad's Midway Madness", "Boo's Haunted Bash", "Koopa's Seaside Soiree", 
            "Goomba's Greedy Gala", "Shy Guy's Jungle Jam", "Bowser's Gnarly Party"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/4/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='5')
    async def five(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 5 board."""
        boardList = [
            "Toy Dream", "Rainbow Dream", "Pirate Dream", 
            "Future Dream", "Undersea Dream", "Sweet Dream", "Bowser's Nightmare"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/5/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='6')
    async def six(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 6 board."""
        boardList = [
            "Towering Treetop", "E Gadd's Garage", "Faire Square", 
            "Snowflake Lake", "Castaway Bay", "Clockwork Castle"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/6/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='7')
    async def seven(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 7 board."""
        boardList = [
            "Grand Canal", "Pagoda Peak", "Pyramid Park", 
            "Neon Heights", "Windmillville", "Bowser's Enchanted Inferno"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/7/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='8')
    async def eight(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 8 board."""
        boardList = [
            "DK's Treetop Temple", "Goomba's Booty Boardwalk", "King Boo's Haunted Hideaway", 
            "Shy Guy's Perplex Express", "Koopa's Tycoon Town", "Bowser's Warped Orbit"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/8/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='9')
    async def nine(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 9 board."""
        boardList = [
            "Toad Road", "Blooper Beach", "Boo's Horror Castle", 
            "DK's Jungle Ruins", "Bowser's Station", "Magma Mine", "Bob-omb Factory"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/9/{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.respond(embed=result_embed)

    @board.command(name='10')
    async def ten(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 10 board."""
        boardList = ["Mushroom Park", "Whimsical Waters", "Chaos Castle", "Airship Central", "Haunted Trail"]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.respond(file=gif_file)

        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        final_image_message = await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/10/{boardParsed}.png")
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
        await ctx.send(embed=result_embed)

    @board.command()
    async def ds(self, ctx):
        """Spins a wheel to randomly pick a Mario Party DS board."""
        boardList = ["Wiggler's Garden", "Kamek's Library", "Bowser's Pinball Machine", "Toadette's Music Room", "DK's Stone Statue"]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.respond(file=gif_file)

        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        final_image_message = await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/DS/{boardParsed}.png")
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
        await ctx.send(embed=result_embed)

    @board.command(name='super')
    async def super(self, ctx):
        """Spins a wheel to randomly pick a Super Mario Party board."""
        boardList = ["Whomp's Domino Ruins", "King Bob-omb's Powderkeg Mine", "Megafruit Paradise", "Kamek's Tantalizing Tower"]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.respond(file=gif_file)

        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        final_image_message = await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/Super/{boardParsed}.png")
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
        await ctx.send(embed=result_embed)

    @board.command(name='superstars')
    async def superstars(self, ctx):
        """Spins a wheel to randomly pick a Mario Party Superstars board."""
        boardList = ["Yoshi's Tropical Island", "Peach's Birthday Cake", 'Space Land', 'Horror Land', 'Woody Woods']

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.respond(file=gif_file)

        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        final_image_message = await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/Superstars/{boardParsed}.png")
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
        await ctx.send(embed=result_embed)

    @board.command(name='jamboree')
    async def jamboree(self, ctx):
        """Spins a wheel to randomly pick a Super Mario Party Jamboree board."""
        boardList = [
            "Mega Wiggler's Tree Party", "Rainbow Galleria", 'Goomba Lagoon', 
            "Roll\'em Raceway", 'Western Land', "Mario\'s Rainbow Castle", "King Bowser\'s Keep"
        ]

        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        boardParsed = urllib.parse.quote(selected_board)

        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)


        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Get the board image from GitHub
        github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards//{boardParsed}.png"

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        final_image_message = await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url=github_image_url)
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

        await ctx.send(embed=result_embed)

    # Party Planner Board Get
    @partyplanner.command(pass_context=True, aliases=["cf"])
    async def curseforge(self, ctx, search: str=None):
        if search == None:
            params = {
            'gameId': '6351',
            'searchFilter': search
            }
        else:
            params = {
            'gameId': '6351',
            'searchFilter': search
            }
        url = "https://api.curse.tools/v1/cf/mods/search"
        responce = requests.get(url, params=params)
        json = responce.json()
        packList = []
        embed = discord.Embed(
            title=f"PartyPlanner64 Board Lookup",
            description="\uFEFF",
            colour=0x98FB98        )
        for pack in json["data"]:
            url2 = "https://api.curse.tools/v1/cf/mods/" + str(pack["id"]) + "/files/" + str(pack["mainFileId"])
            responce = requests.get(url2)
            json2 = responce.json()
            embed.add_field(name=pack["name"], value="https://" + urllib.parse.quote(json2["data"]["downloadUrl"][8:]), inline=True)

        if json["data"] == []:
            embed.add_field(name="No Results", value="")
        else:
            pass
        try:
            embed.set_thumbnail(
                url="https://i.ibb.co/k8tXpy4/ZNV4-Eki3-400x400.jpg"
            )
        except:
            pass
        embed.set_footer(
            text=f"Ran by: {ctx.author} • Yours truly, Poggers"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.respond(content=None, embed=embed)

    # Party Planner Board Get
    @partyplanner.command(pass_context=True, aliases=["legacy", "mpl"])
    async def mariopartylegacy(self, ctx, search: str=None):
        embed = discord.Embed(
            title=f"PartyPlanner64 Board Lookup",
            description="\uFEFF",
            colour=0x98FB98        )
        boardNameList = []
        boardURLList = []
        if search == None:
            urlHack = "https://www.mariopartylegacy.com/forum/index.php?action=downloads;cat=3;sortby=mostview;orderby=desc;start=0"
        else:
            urlHack = "https://www.mariopartylegacy.com/forum/index.php?action=downloads;cat=3;sortby=mostview;orderby=desc;start=0;sa=search2;searchfor=" + search
        response = requests.get(urlHack)
        soup = BeautifulSoup(response.content, 'html.parser')
        boardTitles = soup.find_all('tr', class_=["windowbg", "windowbg2"])
        for title in boardTitles:
            boardName = title.get_text()
            boardName = boardName.split("(None)")[0]
            boardName = boardName.strip()
            boardName = ' '.join([word for word in boardName.split() if not re.search(r'[123459789()]', word)])
            boardNameList.append(boardName)
        for url in boardTitles:
            link_element = url.find('a')
            if link_element:
                boardID = re.findall(r'\d+', link_element['href'])[-1]
                downloadURL = "https://www.mariopartylegacy.com/forum/index.php?action=downloads;sa=downfile&id=" + boardID
                boardURLList.append(downloadURL)

        for name, url in zip(boardNameList, boardURLList):
            embed.add_field(name=name, value=url, inline=True)
        try:
            embed.set_thumbnail(
                url="https://i.ibb.co/k8tXpy4/ZNV4-Eki3-400x400.jpg"
            )
        except:
            pass
        embed.set_footer(
            text=f"Ran by: {ctx.author} • Yours truly, Poggers"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.respond(content=None, embed=embed)

    


def setup(bot):
    bot.add_cog(MarioParty(bot))
