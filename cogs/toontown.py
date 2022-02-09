import discord
import requests

from discord.ext import commands

class Toontown(commands.Cog):

    """Cog for Toontown commands"""

    def __init__(self, bot):
        self.bot = bot


    #TTR Districts Command
    @commands.command(pass_context=True, aliases=["ttr_districts", "ttr"])
    async def ttrdistricts(self, ctx):
        ttr_districts_api = "https://www.toontownrewritten.com/api/population"
        ttr_districts_response = requests.get(ttr_districts_api, verify=True)
        ttr_districts_json = ttr_districts_response.json()
        ttr_districts = ttr_districts_json["populationByDistrict"]
        ttr_districts = json.dumps(ttr_districts, sort_keys=True, indent=2)
        ttr_districts = ttr_districts.replace('"', '')
        ttr_districts = ttr_districts.replace(',', '')
        ttr_districts = str(ttr_districts)[1:-2]
        embed = discord.Embed(
            title=f'Toontown Rewritten Population',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://i.ibb.co/RzrzDVh/TTR.png")
        embed.add_field(name="Population:", value=ttr_districts, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {client.user.name}")
        embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
        await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Toontown(bot))