from discord.ext import commands
import discord
import os
import logging 
import traceback
import re
import aiohttp
import asyncpg

async def get_prefix(bot, message):
    extras = ["jd/", "j/"]

    comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
    match = comp.match(message.content)
    if match is not None:
        extras.append(match.group(1))

    return commands.when_mentioned_or(*extras)(bot, message)

class JDJGBot(commands.Bot):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  async def start(self, *args, **kwargs):
    self.session = aiohttp.ClientSession()
    self.db = await asyncpg.create_pool(os.getenv("DB_key"))

    #self.linked_data = await self.db.fetch("SELECT * FROM linked_chat")
    #self.linked_channels = [c.get("channel_id") for c in self.linked_data]

    #change this to be different(unique global chat table name, with linked channels like the orginal method)

    #grab from guild_bans - guild bans
    #bans - user bans (blacklist)

    await super().start(*args, **kwargs)

  async def close(self):
    await self.session.close()
    await self.db.close()
    await super().close()


bot = JDJGBot(command_prefix = (get_prefix), intents = discord.Intents.all())

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
bot.run(os.environ["TOKEN"])
