from discord.ext import commands
import discord
import os
import B
import logging 

bot = commands.Bot(command_prefix = "jd/", intents = discord.Intents.all())

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
        except commands.errors.ExtensionError:
            traceback.print_exc()

logging.basicConfig(level=logging.INFO)
B.b()
bot.run(os.environ["TOKEN"])