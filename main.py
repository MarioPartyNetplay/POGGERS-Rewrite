#***************************************************************************#
#                                                                           #
# Poggers                                                                   #
# https://github.com/MarioPartyNetplay/Poggers-Rewrite                      #
# Copyright (C) 2023 Nora Hanegan. All rights reserved.                     #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#
import discord
import os
import platform

from cogs.base import Base
from cogs.fun import Fun
from cogs.marioparty import MarioParty

from discord.ext import tasks
from discord.ext import commands

#Intents
intents = discord.Intents.all()

#Define Client
bot = commands.Bot(description="Doopliss", command_prefix=commands.when_mentioned_or("/"), intents=intents, activity=discord.Game(name='around with different names'), guild_ids=[1048370760776962159])

@bot.event
async def on_ready():
  memberCount = len(set(bot.get_all_members()))
  serverCount = len(bot.guilds)
  

  print("                                                                ")
  print("################################################################") 
  print(f"      __________                                               ")
  print(f"      \______   \____   ____   ____   ___________  ______      ")
  print(f"       |     ___/  _ \ / ___\ / ___\_/ __ \_  __ \/  ___/      ")
  print(f"       |    |  (  <_> ) /_/  > /_/  >  ___/|  | \/\___ \       ")
  print(f"       |____|   \____/\___  /\___  / \___  >__|  /____  >      ")
  print(f"                     /_____//_____/      \/           \/       ")
  print("                                                                ")
  print("################################################################") 
  print("Running as: " + bot.user.name + "#" + bot.user.discriminator)
  print(f'With Client ID: {bot.user.id}')
  print("\nBuilt With:")
  print("Python " + platform.python_version())
  print("Py-Cord " + discord.__version__)


#Boot Cogs
bot.add_cog(Base(bot))
bot.add_cog(Fun(bot))
bot.add_cog(MarioParty(bot))

#Run Bot
#keep_alive()
TOKEN = os.environ.get("BOT_TOKEN")
bot.run(TOKEN)
