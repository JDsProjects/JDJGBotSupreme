import discord, aiohttp, re, os, contextlib, traceback
from discord.ext import commands
intents_usage = discord.Intents.all()

async def get_prefix(client,message):
  extras = ["JDBot*","jd*"]
  comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
  match = comp.match(message.content)
  if match is not None:
    extras.append(match.group(1))
  return commands.when_mentioned_or(*extras)(client, message)


async def status_task():
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=" JDBot*help"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers | {len(client.users)} users"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="the creators:"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Nomic Zorua"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="JDJG and Shadi"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="RenDev and LinuxTerm"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="JDJG Bot will DM you two servers join if you want help from the bot makers - from about command or help command"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="(the first one is the support server), though the blooper server will tend to do it now - second one"))
        await asyncio.sleep(30)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="use JDBot!help for the test commands"))
        await asyncio.sleep(30)

async def startup():
  await self.wait_until_ready()

  #line added by RenDev 2/26/2021
  self.whoami = client.user.id

  await status_task()

class JDJG_Bot(commands.Bot):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

  async def start(self,*args, **kwargs):
    self.aiohttp_session=aiohttp.ClientSession()
    await super().start(*args, **kwargs)

  async def close(self):
    await self.aiohttp_session.close()
    await super().close()

  async def getch_member(self, guild, member_id):
    member = None
    with contextlib.suppress(discord.Forbidden, discord.HTTPException):
      member = guild.get_member(member_id) or await guild.fetch_member(member_id)
    return member

  async def getch_user(self, user_id):
    user = None

    with contextlib.suppress(discord.NotFound, discord.HTTPException):
      user = self.get_user(user_id) or await self.fetch_user(user_id)
    return user

  async def setup_hook(self):
    await self.load_extension('jishaku')

    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        try:
          await self.load_extension(f'cogs.{filename[:-3]}')
        except commands.errors.ExtensionError:
          traceback.print_exc()

    self.loop.create_task(startup(self))

    

client = JDJG_Bot(command_prefix=(get_prefix),intents = discord.Intents.all())

whoami = 0




