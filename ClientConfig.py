import discord
import re
import os
from discord.ext import commands
import aiohttp
intents_usage=discord.Intents.all()

async def get_prefix(client,message):
  extras = ["JDBot*","jd*"]
  comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
  match = comp.match(message.content)
  if match is not None:
    extras.append(match.group(1))
  return commands.when_mentioned_or(*extras)(client, message)

class JDJG_Bot(commands.Bot):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

  async def start(self,*args, **kwargs):
    self.aiohttp_session=aiohttp.ClientSession()
    await super().start(*args, **kwargs)

  async def close(self):
    await self.aiohttp_session.close()
    await super().close()

client = JDJG_Bot(command_prefix=(get_prefix),intents = discord.Intents.all())

whoami = 0

client.load_extension('jishaku')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      try:
        client.load_extension(f'cogs.{filename[:-3]}')
      except commands.errors.NoEntryPointError:
        pass