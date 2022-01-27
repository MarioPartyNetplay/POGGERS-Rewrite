@client.command(pass_context=True)
async def ban(ctx, user: discord.Member, *, arg):
    author = ctx.message.author
    reason = arg
    server = ctx.guild.name
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    staff_log = client.get_channel(780939099283521557)
    embed = discord.Embed(
        name="MEMBER_BANNED",
        description="------------------------------------------------------",
        color=0x00ff00)
    embed.set_author(name="Member Banned:\nMember Banned Successfully")
    embed.add_field(
        name="Banned by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Banned: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(
        text="Requested by {} \a {}".format(author, data),
        icon_url=author.avatar_url)
    await ctx.send(embed=embed)
    embed = discord.Embed(
        name="MEMBER_BANNED",
        description="------------------------------------------------------",
        color=0xff0000)
    embed.set_author(name="Member Banned:")
    embed.add_field(
        name="Banned by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Banned: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(text="Banned at {}".format(data))
    await staff_log.send(embed=embed)
    embed = discord.Embed(
        name="BANNED",
        description="------------------------------------------------------",
        color=0xff0000)
    embed.set_author(name="Member Banned:\nYou've been Banned")
    embed.add_field(
        name="Banned by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Banned in: ", value="{}".format(server), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(text="Banned at {}".format(data))
    await user.send(user, embed=embed)
    await ctx.guild.ban(user, reason=reason)

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member, *, arg):
    author = ctx.message.author
    reason = arg
    server = ctx.guild.name
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    staff_log = client.get_channel(780939099283521557)
    embed = discord.Embed(
        name="MEMBER_KICKED",
        description="------------------------------------------------------",
        color=0x00ff00)
    embed.set_author(name="Member Kicked:\nMember Kicked Successfully")
    embed.add_field(
        name="Kicked by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Kicked: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(
        name="Kicked: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(
        text="Requested by {} \a {}".format(author, data),
        icon_url=author.avatar_url)
    await ctx.send(embed=embed)
    embed = discord.Embed(
        name="MEMBER_KICKED",
        description="------------------------------------------------------",
        color=0xff0000)
    embed.set_author(name="Member Kicked:")
    embed.add_field(
        name="Kicked by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Kicked: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(text="Kicked at {}".format(data))
    await staff_log.send(embed=embed)
    embed = discord.Embed(
        name="KICKED",
        description="------------------------------------------------------",
        color=0xff0000)
    embed.set_author(name="Member Kicked:\nYou've been Kicked")
    embed.add_field(
        name="Kicked by: ", value="{}".format(author.mention), inline=False)
    embed.add_field(
        name="Kicked in: ", value="{}".format(server), inline=False)
    embed.add_field(
        name="Reason: ",
        value="{}\n------------------------------------------------------".
        format(arg),
        inline=False)
    embed.set_footer(text="Kicked at {}".format(data))
    await user.send(user, embed=embed)
    await ctx.guild.kick(user, reason=reason)