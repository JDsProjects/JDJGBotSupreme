from discord.ext import commands
import discord
import os
import B
import logging 
import traceback
import re

async def get_prefix(bot, message):
    extras = ["jd/", "j/"]

    comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
    match = comp.match(message.content)
    if match is not None:
        extras.append(match.group(1))

    return commands.when_mentioned_or(*extras)(bot, message)

bot = commands.Bot(command_prefix = (get_prefix), intents = discord.Intents.all())

@bot.event
async def on_error(event, *args, **kwargs):
  more_information = os.sys.exc_info()
  error_wanted = traceback.format_exc()
  traceback.print_exc()
  #print(more_information[0])

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
        except commands.errors.ExtensionError:
            traceback.print_exc()

logging.basicConfig(level=logging.INFO)
B.b()
bot.run(os.environ["TOKEN"])
