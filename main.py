#***************************************************************************#
#                                                                           #
# Doopliss - A Discord Bot For Me.                                          #
# https://github.com/NoraHanegan/Doopliss                                   #
# Copyright (C) 2021 Nora Hanegan. All rights reserved.                     #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

import discord
import random
import os
import json
import aiohttp
import box
import platform
import requests

from dadjokes import Dadjoke
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from keep_alive import keep_alive

#Variables
ownerID = 543576276108181506

#Intents
intents = discord.Intents.default()
intents.members = True

#Define Client
client = commands.Bot(description="Doopliss", command_prefix="!", intents=intents, activity=discord.Game(name='around with different names'))

#Remove Stock Help Command
client.remove_command('help')

@client.event
async def on_ready():
  memberCount = len(set(client.get_all_members()))
  serverCount = len(client.guilds)
  print("                                                                ")
  print("################################################################") 
  print(f" ______                            __    _                     ")
  print(f"|_   _ `.                         [  |  (_)                    ")
  print(f"  | | `. \  .--.    .--.   _ .--.  | |  __   .--.   .--.       ")
  print(f"  | |  | |/ .'`\ \/ .'`\ \[ '/'`\ \| | [  | ( (`\] ( (`\]      ")
  print(f" _| |_.' /| \__. || \__. | | \__/ || |  | |  `'.'.  `'.'.      ")
  print(f"|______.'  '.__.'  '.__.'  | ;.__/[___][___][\__) )[\__) )     ")
  print(f"                           [__|              \___/  \___/      ")
  print("                                                                ")
  print("################################################################") 
  print("Running as: " + client.user.name + "#" + client.user.discriminator)
  print(f'With Client ID: {client.user.id}')
  print("\nBuilt With:")
  print("Python " + platform.python_version())
  print("Py-Cord " + discord.__version__)

#Help Command
@client.command()
async def help(ctx):
    embed = discord.Embed(color=discord.Color.orange(), title="Help Menu")
    #General Comamnds
    embed.add_field(
        name="General",
        value=
        "!help - Shows This Message\n\n!ping - Says Pong Back To You\n\n!server - Shows Server Info\n\n!stats - Show Bot Stats\n",
        inline=False)

    #Fun Comamnds
    embed.add_field(
        name="Fun",
        value=
        "!toss - Coin Flip\n\n!joke - Give a Dad Joke\n\n!dice - Roll 1-6\n\n!reverse <term> - Reverses the given text\n\n!meme - Gives a random meme.\n\n!reddit <term> - Search reddit and find a post matching.\n",
        inline=False)

      #Utilities Commands
    embed.add_field(
        name="Utilities",
        value=
        "!poll <question> - Creates a poll using an upvote, downvote system.\n",
        inline=False)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    await ctx.send(embed=embed)

#Ping Command
@client.command()
async def ping(ctx):
    """Ping Pong"""
    await ctx.send('Pong!')


#Roll Dice Command
@client.command(aliases=["roll"])
async def dice(ctx):
    """Rolls the dice"""
    cont = random.randint(1, 6)
    await ctx.send("You Rolled **{}**".format(cont))


#Coin Flip Command
@client.command(aliases=["flip"])
async def toss(ctx):
    """Put the toss"""
    ch = ["Heads", "Tails"]
    rch = random.choice(ch)
    await ctx.send(f"You got **{rch}**")


#Reverse Text Command
@client.command()
async def reverse(ctx, *, text):
    """Reverse the given text"""
    await ctx.send("".join(list(reversed(str(text)))))


#Meme Command
@client.command()
async def meme(ctx):
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


#Reddit Wide Search Command
@client.command()
async def reddit(ctx, meme_term):
    url_comb = "https://www.reddit.com/search.json?sort=newlimit=100&q=" + meme_term
    r = await aiohttp.ClientSession().get(url_comb)
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


#Dadjoke Command
@client.command(aliases=["dadjoke"])
async def joke(ctx):
    """Sends the dadjokes"""
    async with ctx.typing():
        await ctx.send(Dadjoke().joke)

#Server Command
@client.command(aliases=["server"])
async def s_info(ctx):
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
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    await ctx.send(content=None, embed=embed)



#Stats Command
@client.command()
async def stats(ctx):

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
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {client.user.name}")
    await ctx.send(embed=embed)


#Poll Command
@client.command(pass_context=True)
async def poll(ctx, *args):
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


#TTR Districts Command
@client.command(pass_context=True, aliases=["ttr_districts", "ttr"])
async def ttrdistricts(ctx):
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
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    await ctx.send(content=None, embed=embed)


  
#On Command Error
#@client.event
#async def on_command_error(ctx, error):
#    if isinstance(error, CommandNotFound):
#        await ctx.send("That Command Was not found!")

#Run Bot
keep_alive()
TOKEN = os.environ.get("TOKEN")
client.run(TOKEN)