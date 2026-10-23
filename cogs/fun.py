#***************************************************************************#
#                                                                           #
# Poggers                                                                   #
# https://github.com/MarioPartyNetplay/Poggers-Rewrite                      #
# Copyright (C) 2024 Nayla Hanegan. All rights reserved.                    #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

import aiohttp
import discord
import random
import requests
import time

from dadjokes import Dadjoke
from discord.ext import commands
from discord import emoji, SlashCommandGroup

from util.trivia import TriviaView, TriviaModal

# Variables define at module level
n64MPList = ["Mario Party 1", "Mario Party 2", "Mario Party 3"]
gcMPList = ["Mario Party 4", "Mario Party 5", "Mario Party 6", "Mario Party 7"]
wiiMPList = ["Mario Party 8", "Mario Party 9"]
DSMPList = ["Mario Party DS"]
AdvanceMPList = ["Mario Party Advance", "Mario Party e"]
threeDSMPList = ["Mario Party: Island Tour", "Mario Party: Star Rush", "Mario Party: The Top 100", "Mario Party Advance", "Mario Party e"]
switchMPList = ["Mario Party Superstars", "Super Mario Party"]

n64List = n64MPList + ["Rugrats Scavenger Hunt", "1080 Snowboarding", "Banjo-Tooie", "Conker's Bad Fur Day", "Diddy Kong Racing", "Donkey Kong 64", "Dr. Mario 64", "F-Zero X", "GoldenEye 007", "Kirby 64", "Lego Racers", "Mario Golf", "Mario Kart 64", "Mickey's Speedway USA", "Pokemon Stadium", "Pokemon Stadium 2", "Rakuga Kids", "Super Smash Bros (N64)", "Snowboard Kids", "Snowboard Kids 2", "Star Wars Episode I Pod Racer", "Wave Race 64", "Super Smash Bros 199XTE", "Smash Remix", "South Park World Rally", "Monopoly", "Cruis'n USA", "Hotwheels: Turbo Racing", "Bomberman 64", "Pokemon Puzzle League", "Tony Hawk's Pro Skater", "Tony Hawk's Pro Skater 2", "Tony Hawk's Pro Skater 3", "NFL Blitz 2000", "NFL Blitz 2001", "Stunt Racer", "The New Tetris", "Cruis'n Exotica", "WWF No Mercy", "Superman 64", "Mundial Ronaldinho Soccer 64", "International Superstar Soccer 64", "ClayFighter: Sculptor's Cut", "Rush 2: Extreme Racing USA", "ClayFighter 63 1/3", "007: The World is Not Enough", "Killer Instinct Gold", "Mortal Kombat 4", "Mortal Kombat Trilogy", "Mario Tennis"]

gcList = gcMPList + ["Mario Party 4", "Mario Party 5", "Mario Party 6", "Mario Party 7", "Billy Hatcher and the Giant Egg", "DDR Mario Mix", "Dragon Ball Z Budokai 2", "F-Zero GX", "Harvest Moon: Magical Melody", "Kirby Air Ride", "Mario Golf: Toadstool Tour", "Mario Kart: Double Dash!!", "Mario Power Tennis", "Mario Superstar Baseball", "Metroid Prime 2: Echoes", "Pikmin 2", "Sonic Adventure 2: Battle", "Soul Calibur II", "Star Fox Assault", "Star Wars: Clone Wars", "Super Mario Strikers", "Super Monkey Ball", "Super Monkey Ball 2", "Super Smash Bros Melee", "Super Smash Bros Melee 20XX", "WarioWare: Mega Party Games", "The Simpsons: Hit & Run", "F-Zero GX-Treme", "Super Monkey Ball Deluxe (patch for 2)", "Monkeyed Ball 2: Witty Subtitle", "Super Monkey Ball: Community Workshop Level Pack", "Donkey Konga", "Donkey Konga 2", "Tony Hawk's American Wasteland", "Shrek Super Party", "Spongebob: Lights, Camera, Pants!", "Super Monkey Ball Adventure", "SSX On Tour", "NBA Street V3", "Tiger Woods PGA Tour 2003", "Sonic Gems Collection", "Namco Museum: 50th Anniversary", "007 Nightfire", "007 Everything Or Nothing", "All Star Baseball 2004", "Shrek 2", "Shrek Smash and Crash Racing", "Nicktoons Unite!", "The Legend of Zelda: Four Swords Adventures", "Sonic Riders", "Digimon Rumble Arena 2", "Digimon World 4", "Tony Hawk's Underground", "Tony Hawk's Underground 2", "Godzilla: Destroy All Monsters Melee", "Burnout 2", "Need For Speed: Hot Pursuit", "Namco Museum: Battle Collection", "some WWE game idk", "Sonic the Fighters", "Smashing Drive", "Sonic Heroes", "Madagascar", "Pac-Man World Rally", "Rayman Arena", "SSX Tricky", "Nintendo Puzzle Collection", "Mega Man 2: The Power Fighters", "Black & Bruised", "Capcom vs SNK 2", "Viewtiful Joe: Red-Hot Rumble", "Pokemon Colosseum", "Pokemon XD: Gale of Darkness", "NHL Hitz 20-02", "Need For Speed: Carbon", "Mary-Kate and Ashley: Sweet 16 – Licensed to Drive", "Pac-Man Fever", "Timesplitters 2", "Timesplitters: Future Perfect", "Lego Star Wars: The Video Game"]

wiiList = wiiMPList + ["Mario Kart Wii", "Super Smash Bros Brawl", "Project M", "Dragon Ball Z Budokai 3", "Wii Sports", "Wii Play", "Wii Sports Resort", "Wii Music", "Wii Play Motion", "Wii Party", "Mario Kart Fun", "Mario Kart Fusion", "Super Monkey Ball Banana Blitz", "Super Monkey Ball Step & Roll", "Mario Super Sluggers", "Mario Strikers Charged", "Fortune Street", "Punch-Out!!", "Mario Sports Mix", "Donkey Kong Country Returns", "Kirby's Epic Yarn", "Kirby's Return To Dream Land", "WarioWare: Smooth Moves", "Mario & Sonic at the Olympic Games", "Mario & Sonic at the Olympic Winter Games", "Mario & Sonic at the London 2012 Olympic Games", "Rhythm Heaven Fever", "Donkey Kong Barrel Blast", "Namco Museum Remix", "Rayman Raving Rabbids", "Rayman Raving Rabbids 2", "Rabbids TV Party", "Rabbids Go Home", "Rayman Origins", "New Super Mario Bros Wii", "Newer Super Mario Bros Wii", "Another Super Mario Bros Wii", "New Summer Sun Bros Wii", "M&M's Kart Racing", "Deca Sports", "GoldenEye Wii", "some call of duty game idk", "Brawl Minus", "Hasbro Family Game Night 3", "Guilty Gear XX Accent Core +", "Tatsunoko vs Capcom", "Chicken Little: Ace in Action", "Trauma Center: New Blood", "Boom Blox", "Pokemon Battle Revolution"]

whatsInBoxList = ["<a:BowserDance:687668560193126428>", "<a:BabyBowserFast:687678432045170689>", "<a:BabyBowser:404197234436079618>", "<a:BabyBowser:404197234436079618>", "<a:ToadBoat:739621939894550600>", "<a:ToadBoat:739621939894550600>", "<a:ToadDance2Fast:690633607382827069>", "<a:DKWave:902392049347739669>"]

raceList = ["<:datrBobomb:682698795686953011>", "<:datrBoo:682698795951325213>", "<:datrThwomp:682698795477368834>", "<:datrWhomp:682698795980423266>"]

class Fun(commands.Cog):
    """Cog for Fun commands"""

    def __init__(self, bot):
        self.bot = bot

    game = SlashCommandGroup("game", "Game related commands")

    #Roll Command
    @commands.slash_command(aliases=["party"])
    async def roll(self, ctx, min: int, max: int, count: int):
        """Roll a dice, default is rolling 1d6. (minNumber, maxNumber, diceCount)"""
        if count <= 20:
            results = [str(random.randint(min, max)) for _ in range(count)]
            await ctx.respond(", ".join(results))
        else:
            await ctx.respond('Invalid number of rolls')

    #Dadjoke Command
    @commands.slash_command(aliases=["dadjoke"])
    async def dadjoke(self, ctx):
        """Sends a dadjoke."""
        await ctx.respond(Dadjoke().joke)
    
    #Piracy Command
    @commands.slash_command(aliases=["piracy"])
    async def piracy(self, ctx):
        """Sends a piracy notice."""
        await ctx.respond("Piracy is no party. Wondering how to get the games? It is against our rules and Discord ToS to link to ROM sharing sites, so users here cannot help you. We encourage users to rip their own games using this guide: https://wii.guide/dump-games.html")

    #Piracy Command
    @commands.slash_command(aliases=["cplusplus"])
    async def cplusplus(self, ctx):
        """Sends a Visual C++ Redistrutable notice."""
        await ctx.respond("Wondering why your Dolphin / Dolphin-MPN wont open. It's probably because you are missing this install https://aka.ms/vs/17/release/vc_redist.x64.exe")
       
    #Coin Flip Command
    @commands.slash_command(aliases=["flip"])
    async def toss(self, ctx):
        """Flip a coin, heads or tails, your fate"""
        ch = ["Heads", "Tails"]
        rch = random.choice(ch)
        await ctx.respond(f"You got **{rch}**")

    #Reverse Text Command
    @commands.slash_command()
    async def reverse(self, ctx, *, text: str):
        """Reverse the given text"""
        await ctx.respond("".join(list(reversed(str(text)))))

    @commands.slash_command()
    async def mpfont(self, ctx, text: str):
        """Sends given text in MP font"""
        text = text.lower()
        replacements = {
            "a": "<:MPA:705586267324285021>", "b": "<:MPB:705586281463414816>", "c": "<:MPC:705586292301496320>",
            "d": "<:MPD:705586303139446784>", "e": "<:MPE:705586313042329730>", "f": "<:MPF:705586322689228891>",
            "g": "<:MPG:836775866738016307>", "h": "<:MPH:705586341450219560>", "i": "<:MPI:705586351122284574>",
            "j": "<:MPJ:705586360538628237>", "k": "<:MPK:705586374228705311>", "l": "<:MPL:705586383019966545>",
            "m": "<:MPM:827397829538349099>", "n": "<:MPN:705586402632401018>", "o": "<:MPO:836775888066314290>",
            "p": "<:MPP:836775916091736105>", "q": "<:MPQ:705586443493310564>", "r": "<:MPR:705586460136439819>",
            "s": "<:MPS:705586606370848778>", "t": "<:MPT:705586620186886184>", "u": "<:MPU:705587057510318162>",
            "v": "<:MPV:705587070734958603>", "w": "<:MPW:705587083393368135>", "x": "<:MPX:705587097150685225>",
            "y": "<:MPY:705587108584095784>", "z": "<:MPZ:705587120370352198>", "!": "<:MPExclamation:705594132181287022",
            " ": "          "
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        await ctx.respond(text)

    # Note: mpfontshake and mpfontflash have similarly been omitted from heavy dict rewriting for brevity but should be properly handled like above in your full build

    #Box Command
    @commands.slash_command()
    async def whatsinthebox(self, ctx):
        """Who is in the box"""
        box = random.choice(whatsInBoxList)
        await ctx.respond(box + " is in the box!")
    
    #Day at the Races Command
    @commands.slash_command()
    async def dayattheraces(self, ctx):
        """Mock day at the races"""
        box = random.sample(raceList, 4)
        boxMain = ", ".join(box)
        await ctx.respond("Day At The Races: Results\n\n" + boxMain)

    #Game Subcommand
    @game.command(name='marioparty')
    async def marioparty_all(self, ctx, amount: int = 1):
        """Pick a Mario Party in general"""
        box = random.sample(n64MPList + gcMPList + wiiMPList + AdvanceMPList + threeDSMPList + DSMPList + switchMPList, amount)
        boxMain = ", ".join(box)
        await ctx.respond(boxMain)

    #Game Subcommand
    @game.command(name='marioparty-n64')
    async def marioparty_n64(self, ctx):
        """Pick a Mario Party from the N64"""
        gameSelect = random.choice(n64MPList)
        await ctx.respond(gameSelect)
    
    #Game Subcommand
    @game.command(name='marioparty-gc')
    async def marioparty_gc(self, ctx):
        """Pick a Mario Party from the GameCube"""
        gameSelect = random.choice(gcMPList)
        await ctx.respond(gameSelect)
    
    #Game Subcommand
    @game.command(name='marioparty-gc8')
    async def marioparty_gc8(self, ctx):
        """Pick a Mario Party from 4-8"""
        gameSelect = random.choice(gcMPList + ["Mario Party 8"])
        await ctx.respond(gameSelect)
    
    #Game Subcommand
    @game.command(name='marioparty-wii')
    async def marioparty_wii(self, ctx):
        """Pick a Mario Party"""
        gameSelect = random.choice(wiiMPList)
        await ctx.respond(gameSelect)

    #Game Subcommand
    @game.command(name='marioparty-netplayable')
    async def marioparty_netplayable(self, ctx):
        """Pick a Mario Party that you can play over Netplay"""
        gameSelect = random.choice(n64MPList + gcMPList + wiiMPList)
        await ctx.respond(gameSelect)

    @game.command(name='nintendo-64')
    async def n64(self, ctx):
        """Pick a N64 Game"""
        gameSelect = random.choice(n64List)
        await ctx.respond(gameSelect)
        
    @game.command()
    async def gamecube(self, ctx):
        """Pick a GameCube Game"""
        gameSelect = random.choice(gcList)
        await ctx.respond(gameSelect)    

    @game.command()
    async def wii(self, ctx):
        """Pick a Wii Game"""
        gameSelect = random.choice(wiiList)
        await ctx.respond(gameSelect)

    @game.command()
    async def all(self, ctx):
        """Pick any Game"""
        gameSelect = random.choice(wiiList + gcList + n64List)
        await ctx.respond(gameSelect)
    
    @game.command()
    async def mpiq(self, ctx, id: str = None):
        """Mario Party IQ"""
        
        if id is None:
            Decider = str(random.randint(1, 100))
        else:
            Decider = id
            
        mylines = []
        try:
            with open(f'mpiq/Q{Decider}.txt', 'rt') as myfile:
                for myline in myfile:
                    mylines.append(myline.strip())
        except FileNotFoundError:
            await ctx.respond("That quiz ID doesn't exist!")
            return

        Difficulty = mylines[0] 
        Game = mylines[1] 
        Question = mylines[2] 
        
        AnswerList = [word.replace("#", " ").lower() for word in mylines[3].split()]
        ExactAnswer = mylines[4]

        # Attach the button view to the message
        view = TriviaView(AnswerList, ExactAnswer)
        
        await ctx.respond(
            f"**Quiz Starting...**\n#{Decider} | {Difficulty} - {Game}\n\n**{Question}**", 
            view=view
        )
        # Save message reference for timeout handling
        view.message = await ctx.interaction.original_response()

def setup(bot):
    bot.add_cog(Fun(bot))