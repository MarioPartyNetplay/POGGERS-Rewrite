import discord
import platform

from discord.ext import commands

#Variables
ownerID = 543576276108181506
class Base(commands.Cog):

    """Cog for Base commands"""

    def __init__(self, bot):
        self.bot = bot

    #Ping Command
    @commands.slash_command(description="Ping pong")
    async def ping(self, ctx):
        await ctx.respond("Pong")

    #Poll Command
    @commands.slash_command(description="Starts a poll")
    async def poll(self, ctx, question: str):
        mesg = ' '.join({question})
        embed = discord.Embed(
            title='A Poll has Started!',
            description='{0}'.format(mesg),
            color=0x00FF00)
        embed.set_footer(text=f"Poll created by: {ctx.author} • React to vote! • Yours truly, Poggers")
        embed_message = await ctx.respond(embed=embed)

        await embed_message.add_reaction('👍')
        await embed_message.add_reaction('👎')
        await embed_message.add_reaction('🤷')
    
    #Server Command
    @commands.slash_command(descriptin="Shows server info")
    async def server(self, ctx):
        server = ctx.guild
        icon = ("\uFEFF")
        embed = discord.Embed(
            title=f"Server info for {server.name}",
            description='\uFEFF',
            colour=0x98FB98)
        try:
            embed.set_thumbnail(url=server.icon(size=512))
        except:
            pass
        embed.add_field(name="Name", value=server.name, inline=True)
        embed.add_field(name="Member Count", value=server.member_count, inline=True)
        embed.add_field(name="Owner", value="<@" + f"{server.owner_id}" + ">", inline=True)
        embed.add_field(name="ID", value=server.id, inline=True)
        embed.add_field(name="Creation Date", value=f"{server.created_at}", inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
        await ctx.respond(content=None, embed=embed)

    #Stats Command
    @commands.slash_command()
    async def stats(self, ctx):

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(
            title=f'Poggers Stats',
            description='\uFEFF',
            colour=0x98FB98)

        embed.add_field(
            name='Python Version:', value=f"{pythonVersion}", inline=False)
        embed.add_field(
            name='Py-Cord Version', value=f"{dpyVersion}", inline=False)
        embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
        embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
        embed.add_field(name='Bot Developer:', value="<@" + f"{ownerID}" + ">", inline=False)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
        await ctx.respond(embed=embed)

    @commands.slash_command()
    async def channelid(self, ctx):
        await ctx.respond(str(ctx.channel.id))

    @commands.slash_command(brief="Get the ID of a member")
    async def userid(self, ctx, member : discord.Member=0):
      if member == 0:
        await ctx.respond(str(ctx.author.id))
      else:
        await ctx.respond(str(member.id))

def setup(bot):
    bot.add_cog(Base(bot))