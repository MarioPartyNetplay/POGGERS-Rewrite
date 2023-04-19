import aiohttp
import discord
import random
import requests

from dadjokes import Dadjoke
from discord.ext import commands
from discord import emoji

class Fun(commands.Cog):

    """Cog for Fun commands"""

    def __init__(self, bot):
        self.bot = bot
    
    #Roll Command
    @commands.slash_command(aliases=["party"])
    async def roll(self, ctx, min: int, max:int, count:int):
        
        """Roll a dice, default is rolling 1d6. (minNumber, maxNumber, diceCount)"""
        if count <= 20:
            for _ in range(count):
                await ctx.send(random.randint(min, max))
        if count > 20:
            await ctx.send('Invalid number of rolls')

    #Dadjoke Command
    @commands.slash_command(aliases=["dadjoke"])
    async def dadjoke(self, ctx):
        """Sends a dadjoke."""
        async with ctx.typing():
            await ctx.send(Dadjoke().joke)

    #Coin Flip Command
    @commands.slash_command(aliases=["flip"])
    async def toss(self, ctx):
        """Flip a coin, heads or tails, your fate"""
        ch = ["Heads", "Tails"]
        rch = random.choice(ch)
        await ctx.send(f"You got **{rch}**")


    #Reverse Text Command
    @commands.slash_command()
    async def reverse(self, ctx, *, text):
        """Reverse the given text"""
        await ctx.send("".join(list(reversed(str(text)))))


    #Meme Command
    @commands.slash_command()
    async def meme(self, ctx):
        """Sends you random meme"""
        r = await aiohttp.ClientSession().get(
            "https://www.reddit.com/r/dankmemes/top.json?sort=new&t=day&limit=100")
        r = await r.json()
        r = box.Box(r)
        data = random.choice(r.data.children).data
        img = data.url
        title = data.title
        url_base = data.permalink
        url = "https://reddit.com" + url_base
        embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
        embed.set_image(url=img)
        await ctx.send(embed=embed)

    @commands.slash_command()
    async def drama(self, ctx):
        drama = requests.get('http://staff.toonisland.online:3002/raw')
        await ctx.send(drama.text)

    @commands.slash_command()
    async def mpfont(self, ctx, text: str):
        text = text.lower()
        text = text.replace("a", "<:MPA:705586267324285021>")
        text = text.replace("b", "<:MPB:705586281463414816>")
        text = text.replace("c", "<:MPC:705586292301496320>")
        text = text.replace("d", "<:MPD:705586303139446784>")
        text = text.replace("e", "<:MPE:705586313042329730>")
        text = text.replace("f", "<:MPF:705586322689228891>")
        text = text.replace("g", "<:MPG:836775866738016307>")
        text = text.replace("h", "<:MPH:705586341450219560>")
        text = text.replace("i", "<:MPI:705586351122284574>")
        text = text.replace("j", "<:MPJ:705586360538628237>")
        text = text.replace("k", "<:MPK:705586374228705311>")
        text = text.replace("l", "<:MPL:705586383019966545>")
        text = text.replace("m", "<:MPM:827397829538349099>")
        text = text.replace("n", "<:MPN:705586402632401018>")
        text = text.replace("o", "<:MPO:836775888066314290>")
        text = text.replace("p", "<:MPP:836775916091736105>")
        text = text.replace("q", "<:MPQ:705586443493310564>")
        text = text.replace("r", "<:MPR:705586460136439819>")
        text = text.replace("s", "<:MPS:705586606370848778>")
        text = text.replace("t", "<:MPT:705586620186886184>")
        text = text.replace("u", "<:MPU:705587057510318162>")
        text = text.replace("v", "<:MPV:705587070734958603>")
        text = text.replace("w", "<:MPW:705587083393368135>")
        text = text.replace("x", "<:MPX:705587097150685225>")
        text = text.replace("y", "<:MPY:705587108584095784>")
        text = text.replace("z", "<:MPZ:705587120370352198>")
        text = text.replace("!", "<:MPExclamation:705594132181287022")     
        await ctx.send(text)


def setup(bot):
    bot.add_cog(Fun(bot))
