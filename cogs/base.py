import discord

from discord.ext import commands

class Base(commands.Cog):

    """Cog for Base commands"""

    def __init__(self, bot):
        self.bot = bot

    #Ping Command
    @commands.command(description="ping pong")
    async def ping(self, ctx):
        await ctx.send("Pong")

    #Poll Command
    @commands.command(pass_context=True)
    async def poll(self, ctx, *args):
        mesg = ' '.join(args)
        await ctx.message.delete()
        embed = discord.Embed(
            title='A Poll has Started!',
            description='{0}'.format(mesg),
            color=0x00FF00)
        embed.set_footer(text=f"Poll created by: {ctx.message.author} • React to vote! • Yours truly, {client.user.name}")
        embed_message = await ctx.send(embed=embed)

        await embed_message.add_reaction('👍')
        await embed_message.add_reaction('👎')
        await embed_message.add_reaction('🤷')
    
    #Server Command
    @commands.command(aliases=["server"])
    async def s_info(self, ctx):
        server = ctx.guild
        icon = ("\uFEFF")
        embed = discord.Embed(
            title=f"Server info for {server.name}",
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=server.icon_url_as(size=512))
        embed.add_field(name="Name", value=server.name, inline=True)
        embed.add_field(name="Region", value=server.region, inline=True)
        embed.add_field(name="Member Count", value=server.member_count, inline=True)
        embed.add_field(name="Owner", value="<@" + f"{server.owner_id}" + ">", inline=True)
        embed.add_field(name="ID", value=server.id, inline=True)
        embed.add_field(name="Creation Date", value=f"{server.created_at}", inline=True)
        embed.add_field(name="Server Icon Url", value={server.icon_url}, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {client.user.name}")
        embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #Stats Command
    @commands.command()
    async def stats(self, ctx):

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(client.guilds)
        memberCount = len(set(client.get_all_members()))

        embed = discord.Embed(
            title=f'{client.user.name} Stats',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)

        embed.add_field(
            name='Python Version:', value=f"{pythonVersion}", inline=False)
        embed.add_field(
            name='Py-Cord Version', value=f"{dpyVersion}", inline=False)
        embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
        embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
        embed.add_field(name='Bot Developer:', value="<@" + f"{ownerID}" + ">", inline=False)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def channelid(self, ctx):
        await ctx.send(str(ctx.channel.id))

    @commands.command(brief="Get the ID of a member")
    async def userid(ctx,member : discord.Member):
      if member == None:
        await ctx.send(str(ctx.author.id))
      else:
        await ctx.send(str(member.id))

def setup(bot):
    bot.add_cog(Base(bot))