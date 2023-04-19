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
        text = text.replace(" ", "          ")    
        await ctx.send(text)

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
        text = text.replace("?", "<:MPQuestion:705594108676276266")
        text = text.replace(" ", "          ")    
        await ctx.send(text)

    @commands.slash_command()
    async def mpfontshake(self, ctx, text: str):
        text = text.lower()
        text = text.replace("a", "<a:mp1a:706974442160521287>")
        text = text.replace("b", "<a:mp1b:706974442328424482>")
        text = text.replace("c", "<a:mp1c:706974441976102932>")
        text = text.replace("d", "<a:mp1d:706974442215047178>")
        text = text.replace("e", "<a:mp1e:706974442219241472>")
        text = text.replace("f", "<a:mp1f:706974441762193420>")
        text = text.replace("g", "<a:mp1g:706974441929965648>")
        text = text.replace("h", "<a:mp1h:706974441946480650>")
        text = text.replace("i", "<a:mp1i:706974441699278880>")
        text = text.replace("j", "<a:mp1j:706974441791291515>")
        text = text.replace("k", "<a:mp1k:706974441850273913>")
        text = text.replace("l", "<a:mp1l:705586383019966545>")
        text = text.replace("m", "<a:mp1m:827400882713919488>")
        text = text.replace("n", "<a:mp1n:706974441833496646>")
        text = text.replace("o", "<a:mp1o:706974441560604707>")
        text = text.replace("p", "<a:mp1p:706974441636233336>")
        text = text.replace("q", "<a:mp1q:706974441208545352>")
        text = text.replace("r", "<a:mp1r:706974441791291522>")
        text = text.replace("s", "<a:mp1s:706974441241837622>")
        text = text.replace("t", "<a:mp1t:706974440633663601>")
        text = text.replace("u", "<a:mp1u:706974441686433802>")
        text = text.replace("v", "<a:mp1v:706974440864612362>")
        text = text.replace("w", "<a:mp1w:706974440847573102>")
        text = text.replace("x", "<a:mp1x:706974440738521195>")
        text = text.replace("y", "<a:mp1y:706974440587788361>")
        text = text.replace("z", "<a:mp1z:706974440864481321>")
        text = text.replace("!", "<a:mp1ex:706974440663154749") 
        text = text.replace("?", "<a:mp1qu:706974440210038928") 
        text = text.replace(" ", "          ")    
        await ctx.send(text)

    @commands.slash_command()
    async def mpfontflash(self, ctx, text: str):
        text = text.lower()
        text = text.replace("a", "<a:mp2a:706974441854205982>")
        text = text.replace("b", "<a:mp2b:706974442311385200>")
        text = text.replace("c", "<a:mp2c:706974442353590312>")
        text = text.replace("d", "<a:mp2d:706974442403790948>")
        text = text.replace("e", "<a:mp2e:706974441955000440>")
        text = text.replace("f", "<a:mp2f:706974444270387301>")
        text = text.replace("g", "<a:mp2g:706974442055532648>")
        text = text.replace("h", "<a:mp2h:706974441984360500>")
        text = text.replace("i", "<a:mp2i:706974441816457277>")
        text = text.replace("j", "<a:mp2j:706974442026434660>")
        text = text.replace("k", "<a:mp2k:706974441099493454>")
        text = text.replace("l", "<a:mp2l:706974441804005499>")
        text = text.replace("m", "<a:mp2m:827400882013339669>")
        text = text.replace("n", "<a:mp2n:706974441850273912>")
        text = text.replace("o", "<a:mp2o:706974442248471051>")
        text = text.replace("p", "<a:mp2p:706974441430712329>")
        text = text.replace("q", "<a:mp2q:706974441434775583>")
        text = text.replace("r", "<a:mp2r:706974440994504755>")
        text = text.replace("s", "<a:mp2s:706974440688451627>")
        text = text.replace("t", "<a:mp2t:706974441128591442>")
        text = text.replace("u", "<a:mp2u:706974441686433802>")
        text = text.replace("v", "<a:mp2v:706974440914812958>")
        text = text.replace("w", "<a:mp2w:706974440847835206>")
        text = text.replace("x", "<a:mp2x:706974440684257283>")
        text = text.replace("y", "<a:mp2y:706974440805630024>")
        text = text.replace("z", "<a:mp2z:706974440252244041>")
        text = text.replace("!", "<a:mp2ex:706974440663154749") 
        text = text.replace("?", "<a:mp2qu:706974440591720548") 
        text = text.replace(" ", "          ")    
        await ctx.send(text)


def setup(bot):
    bot.add_cog(Fun(bot))
