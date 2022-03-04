import discord, os, random, asyncio, chardet, re, math, logging, mystbin, sr_api, asuna_api, aioimgur, time, async_cse
#modules ^
from discord.ext import commands
import ClientConfig, random_response, DatabaseControl, RankSystem, GlobalLinker, UpdateNotify, DatabaseConfig,  GetPfp, color_code, swear_checker
#custom programs ^
#from itertools import cycle
import datetime
from pytz import timezone #all good
from difflib import SequenceMatcher
#import itertools

bad_list=swear_checker.bad_word_list

logging.basicConfig(level=logging.INFO)

client = ClientConfig.client

jdjg_id = [
  168422909482762240,
  393511863385587712,
]

#this is used for the order command

#jdjg's id only(don't add any more)

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
        

#be careful not to have a * anywhere else,
#or the text will be italicised

discordprefix = "JDBot*"

guild_prefixes = {}

async def startup():
  await client.wait_until_ready()

  #line added by RenDev 2/26/2021
  ClientConfig.whoami = client.user.id

  await status_task()
    

admins = [
  168422909482762240,
  269904594526666754,
  717822288375971900,
  357006546674253826,
  734666800905846834,
]

admin_contact = [
  168422909482762240,
  717822288375971900,
  357006546674253826,]

admin_contact2 = [
  168422909482762240,
  357006546674253826,
]

#adding an id(if you have access to the source code and want to fork it, credit us, getting your discord id is easy, replace ours with the ones you are playing to use)


slur_censor = []

class BetterMemberConverter(commands.Converter):
  async def convert(self,ctx,argument):
    try:
      user = await commands.MemberConverter().convert(ctx,argument)
    except commands.MemberNotFound:
      user = None

    if user == None:
      tag = re.match(r"#?(\d{4})",argument)
      if tag:
        if ctx.guild:
          test=discord.utils.get(ctx.guild.members, discriminator = tag.group(1))
          if test:
            user = test
          if not test:
            user=ctx.author
        if ctx.guild is None:
          user = await BetterUserconverter().convert(ctx,argument)
          if user:
            user = client.get_user(user.id)
          if user is None:
            user = ctx.author
               
    return user

class BetterUserconverter(commands.Converter):
  async def convert(self, ctx, argument):
    try:
     user=await commands.UserConverter().convert(ctx,argument)
    except commands.UserNotFound:
      user = None
    if not user and ctx.guild:
      user=ctx.guild.get_member_named(argument)
    if user == None:

      match2 = re.match(r'<@&([0-9]+)>$',argument)
      if match2:
        argument2=match2.group(1)
        role=ctx.guild.get_role(int(argument2))
        if role.is_bot_managed:
            user=role.tags.bot_id
            user = client.get_user(user)
            if user is None:
              user = await client.fetch_user(user)

    if user == None:
      tag = re.match(r"#?(\d{4})",argument)
      if tag:
        test=discord.utils.get(client.users, discriminator = tag.group(1))
        if test:
          user = test
        if not test:
          user=ctx.author
          
    return user

async def triggered_converter(url,ctx):
  sr_client=sr_api.Client(session=client.aiohttp_session)
  source_image=sr_client.filter(option="triggered",url=str(url))

  imgur_client= aioimgur.ImgurClient(os.environ["imgur_id"],os.environ["imgur_secret"])
  imgur_url= await imgur_client.upload_from_url(source_image.url)

  embed = discord.Embed(color=random.randint(0, 16777215))
  embed.set_author(name=f"Triggered gif requested by {ctx.author}",icon_url=(ctx.author.display_avatar.url))
  embed.set_image(url=imgur_url["link"])
  embed.set_footer(text="powered by some random api")
  await ctx.send(embed=embed)

@client.command()
async def CRAP_BACKUP(ctx):
  await ctx.send("Crap ok...ill back them up real quick")
  guild_search = client.get_guild(736422329399246990)
  guild_emoji_fetch = guild_search.emojis
  for obj in guild_emoji_fetch:
    print(obj.url)

@client.group(name="order",invoke_without_command=True)
async def order(ctx,*,args=None):
  if args is None:
    await ctx.send("You can't order nothing.")
  if args:
    time_before=time.perf_counter()
    image_client=async_cse.Search(os.environ["image_api_key"],engine_id=os.environ["google_image_key"])
    results = await image_client.search(args, safesearch=True, image_search=True)
    emoji_image = sorted(results, key=lambda x: SequenceMatcher(None, x.image_url,args).ratio())[-1]
    await image_client.close()
    time_after=time.perf_counter()
    try:
      await ctx.message.delete()
    except discord.errors.Forbidden:
      pass
  
    embed = discord.Embed(title=f"Item: {args}", description=f"{ctx.author} ordered a {args}",color=random.randint(0, 16777215),timestamp=ctx.message.created_at)
    embed.set_author(name=f"order for {ctx.author}:",icon_url=(ctx.author.display_avatar.url))
    embed.add_field(name="Time Spent:",value=f"{int((time_after - time_before)*1000)}MS")
    embed.add_field(name="Powered by:",value="Google Images Api")
    embed.set_image(url=emoji_image.image_url)
    embed.set_footer(text = f"{ctx.author.id} \nCopyright: I don't know the copyright.")
    await ctx.send(content="Order has been logged for safety purposes(we want to make sure no unsafe search is sent)",embed=embed)
    await client.get_channel(921939352769167360).send(embed=embed)

@client.command(brief="a command to get the avatar of a user",help="using the userinfo technology it now powers avatar grabbing.",aliases=["pfp",])
async def avatar(ctx,*,user: BetterUserconverter = None): 
  if user is None:
    user = ctx.author
  embed = discord.Embed(color=random.randint(0, 16777215))
  embed.set_author(name=f"{user.name}'s avatar:",icon_url=(user.display_avatar.url))
  embed.set_image(url=(user.display_avatar.url))
  embed.set_footer(text=f"Requested by {ctx.author}")
  await ctx.send(embed=embed)

@client.command(brief = "a command that takes a url and sees if it's an image.")
async def image_check(ctx):
  
  images = list(filter(lambda e: e.type == "image", ctx.message.embeds))

  for e in images:
    if e.type == "image":
      await ctx.send(f"{e.url}")
      
  if not images:
    await ctx.send("you need to pass a url with an image, if you did, then please run again. This is a discord issue, and I do not want to wait for discord to change its message.")

@client.command(brief="a command to send mail")
async def mail(ctx,*,user: BetterUserconverter=None):
  if user is None:
    await ctx.reply("User not found, returning Letter")
    user = ctx.author
  if user:
    def check(m):
      return m.author.id == ctx.author.id
    await ctx.reply("Please give me a message to use.")
    message = await client.wait_for("message",check=check)
    embed_message = discord.Embed(title=message.content, timestamp=(message.created_at), color=random.randint(0, 16777215))
    embed_message.set_author(name=f"Mail from: {ctx.author}",icon_url=(ctx.author.display_avatar.url))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url = "https://i.imgur.com/1XvDnqC.png")
    if (user.dm_channel is None):
      await user.create_dm()
    await user.send(embed=embed_message)
    embed_message.add_field(name="Sent To:",value=str(user))
    await client.get_channel(921939352769167360).send(embed=embed_message)

@order.command(brief="a command to shuffle images from google images")
async def shuffle(ctx,*,args=None):
  if args is None:
    await ctx.send("You can't order nothing")
  if args:
    time_before=time.perf_counter()
    image_client=async_cse.Search(os.environ["image_api_key"],engine_id=os.environ["google_image_key"])
    results = await image_client.search(args, safesearch=True, image_search=True)
    emoji_image = results[random.randint(0,len(results)-1)]
    await image_client.close()
    time_after=time.perf_counter()
    try:
      await ctx.message.delete()
    except discord.errors.Forbidden:
      pass

    embed = discord.Embed(title=f"Item: {args}", description=f"{ctx.author} ordered a {args}",color=random.randint(0, 16777215),timestamp=ctx.message.created_at)
    embed.set_author(name=f"order for {ctx.author}:",icon_url=(ctx.author.display_avatar.url))
    embed.add_field(name="Time Spent:",value=f"{int((time_after - time_before)*1000)}MS")
    embed.add_field(name="Powered by:",value="Google Images Api")
    embed.set_image(url=emoji_image.image_url)
    embed.set_footer(text = f"{ctx.author.id} \nCopyright: I don't know the copyright.")
    await ctx.send(content="Order has been logged for safety purposes(we want to make sure no unsafe search is sent)",embed=embed)
    await client.get_channel(921939352769167360).send(embed=embed)

@client.command(brief="a command to shuffle images from google images",aliases=["order-shuffle"])
async def order_shuffle(ctx,*,args):
  if args is None:
    await ctx.send("You can't order nothing")
  if args:
    time_before=time.perf_counter() 
    image_client=async_cse.Search(os.environ["image_api_key"],engine_id=os.environ["google_image_key"])
    results = await image_client.search(args, safesearch=True, image_search=True)
    emoji_image = results[random.randint(0,len(results)-1)]
    await image_client.close()
    time_after=time.perf_counter()
    try:
      await ctx.message.delete()
    except discord.errors.Forbidden:
      pass

    embed = discord.Embed(title=f"Item: {args}", description=f"{ctx.author} ordered a {args}",color=random.randint(0, 16777215),timestamp=ctx.message.created_at)
    embed.set_author(name=f"order for {ctx.author}:",icon_url=(ctx.author.display_avatar.url))
    embed.add_field(name="Time Spent:",value=f"{int((time_after - time_before)*1000)}MS")
    embed.add_field(name="Powered by:",value="Google Images Api")
    embed.set_image(url=emoji_image.image_url)
    embed.set_footer(text = f"{ctx.author.id} \nCopyright: I don't know the copyright.")
    await ctx.send(content="Order has been logged for safety purposes(we want to make sure no unsafe search is sent)",embed=embed)
    await client.get_channel(921939352769167360).send(embed=embed)

@client.command(help="a hug command to hug people",brief="this the first command to hug.")
async def hug(ctx,*, Member: BetterMemberConverter=None):
  if Member is None:
    Member = ctx.author
    
  if Member.id == ctx.author.id:
    person = client.user
    target = ctx.author
  
  if Member.id != ctx.author.id:
    person = ctx.author
    target = Member

  sr_client=sr_api.Client(session=client.aiohttp_session)
  image=await sr_client.get_gif("hug")

  embed=discord.Embed(color=random.randint(0, 16777215))
  embed.set_author(name=f"{person} hugged you! Awwww...",icon_url=(person.display_avatar.url))
  embed.set_image(url=image.url)
  embed.set_footer(text="powered by some random api")
  
  if isinstance(ctx.channel, discord.TextChannel):
    await ctx.send(content=target.mention,embed=embed) 

  if isinstance(ctx.channel,discord.DMChannel):
    if target.dm_channel is None:
      await target.create_dm()
    
    try:
      await target.send(content=target.mention,embed=embed)
    except discord.Forbidden:
      await ctx.author.send("Failed DM'ing them...")

@client.command(help="another command to give you pat gifs",brief="powered using the asuna api")
async def pat2(ctx,*, Member: BetterMemberConverter= None):
  if Member is None:
    Member = ctx.author
    
  if Member.id == ctx.author.id:
    person = client.user
    target = ctx.author
  
  if Member.id != ctx.author.id:
    person = ctx.author
    target = Member
  
  asuna = asuna_api.Client(session=client.aiohttp_session)
  url = await asuna.get_gif("pat")

  embed=discord.Embed(color=random.randint(0, 16777215))
  embed.set_author(name=f"{person} patted you! *pat pat pat*",icon_url=(person.display_avatar.url))
  embed.set_image(url=url.url)
  embed.set_footer(text="powered using the asuna.ga api")
  
  if isinstance(ctx.channel, discord.TextChannel):
    await ctx.send(content=target.mention,embed=embed) 

  if isinstance(ctx.channel,discord.DMChannel):
    if target.dm_channel is None:
      await target.create_dm()
    
    try:
      await target.send(content=target.mention,embed=embed)
    except discord.Forbidden:
      await ctx.author.send("Failed DM'ing them...")


@client.command(help="a command to send facepalm gifs",brief="using some random api it sends you a facepalm gif lol")
async def facepalm(ctx,*, Member: BetterMemberConverter=None):
  if Member is None:
    Member = ctx.author
    
  if Member.id == ctx.author.id:
    person = client.user
    target = ctx.author
  
  if Member.id != ctx.author.id:
    person = ctx.author
    target = Member
  
  sr_client=sr_api.Client(session=client.aiohttp_session)
  image=await sr_client.get_gif("face-palm")

  embed=discord.Embed(color=random.randint(0, 16777215))
  embed.set_author(name=f"{target} you made {person} facepalm",icon_url=(person.display_avatar.url))
  embed.set_image(url=image.url)
  embed.set_footer(text="powered by some random api")
  
  if isinstance(ctx.channel, discord.TextChannel):
    await ctx.send(content=target.mention,embed=embed) 

  if isinstance(ctx.channel,discord.DMChannel):
    if target.dm_channel is None:
      await target.create_dm()
    
    try:
      await target.send(content=target.mention,embed=embed)
    except discord.Forbidden:
      await ctx.author.send("Failed Dming them...")

@client.command(help="takes a .png attachment or your avatar and makes a triggered version.")
async def triggered(ctx):
  y = 0
  if len(ctx.message.attachments) > 0:
    for x in ctx.message.attachments:
      if x.filename.endswith(".png"):
        url = x.url
        await triggered_converter(url,ctx)
        y = y + 1
      if not x.filename.endswith(".png"):
        pass

  if len(ctx.message.attachments) == 0 or y == 0:
    url = ctx.author.avatar_url_as(format="png")
    await triggered_converter(url,ctx)

@client.command(help="uploads your emojis into a mystbin link")
async def look_at(ctx):
  if isinstance(ctx.message.channel, discord.TextChannel):
    message_emojis = ""
    for x in ctx.guild.emojis:
      message_emojis = message_emojis+" "+str(x)+"\n"
    mystbin_client = mystbin.Client(session=client.aiohttp_session)
    paste = await mystbin_client.post(message_emojis)
    await ctx.send(paste.url)
    
  if isinstance(ctx.channel,discord.DMChannel):
    await ctx.send("We can't use that in DMS")

@client.command()
async def headpat(ctx):
  import petpet.Pet
  await petpet.Pet.get_pet(ctx.message,ctx.message.channel)

@client.command(help="a way to look up minecraft usernames",brief="using the official minecraft api, looking up minecraft information has never been easier(tis only gives minecraft account history relating to name changes)")
async def mchistory(ctx,*,args=None):
  import asuna_api
  asuna = asuna_api.Client(session=client.aiohttp_session)
  minecraft_info=await asuna.mc_user(args)
  
  if not args:
    await ctx.send("Please pick a minecraft user.")

  if args:
    embed=discord.Embed(title=f"Minecraft Username: {args}",color=random.randint(0, 16777215))
    embed.set_footer(text=f"Minecraft UUID: {minecraft_info.uuid}")
    embed.add_field(name="Orginal Name:",value=minecraft_info.name)
    y = 0
    for x in minecraft_info.history:
      if y > 0:
        embed.add_field(name=f"Username:\n{x['name']}",value=f"Date Changed:\n{x['changedToAt']}\n \nTime Changed: \n {x['timeChangedAt']}")

      y = y + 1
    embed.set_author(name=f"Requested by {ctx.author}",icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=embed)

@client.command(help="a command to backup text",brief="please don't upload any private files that aren't meant to be seen")
async def text_backup(ctx):
  if ctx.message.attachments:
    for x in ctx.message.attachments:
      file=await x.read()
      if len(file) > 0:
        encoding=chardet.detect(file)["encoding"]
        if encoding:
          text = file.decode(encoding)
          mystbin_client = mystbin.Client(session=client.aiohttp_session)
          paste = await mystbin_client.post(text)
          await ctx.send(content=f"Added text file to mystbin: \n{paste.url}")
        if encoding is None:
          await ctx.send("it looks like it couldn't decode this file, if this is an issue DM JDJG Inc. Official#3439 or it wasn't a text file.")
      if len(file ) < 1:
        await ctx.send("this doesn't contain any bytes.")

@client.command()
async def ping(ctx):
  await ctx.send("Pong")
  await ctx.send(f"Response time: {client.latency*1000}")

@client.group(name="apply",invoke_without_command=True)
async def apply(ctx):
  await ctx.send("this command is meant to apply")

@apply.command(help="a command to apply for our Bloopers.")
async def bloopers(ctx,*,args=None):
  if args is None:
    await ctx.send("You didn't give us any info.")
  if args:
    if isinstance(ctx.message.channel, discord.TextChannel):
      await ctx.message.delete()

    for x in [708167737381486614,168422909482762240]:
      apply_user = client.get_user(x)
    
    if (apply_user.dm_channel is None):
      await apply_user.create_dm()
    
    embed_message = discord.Embed(title=args,color=random.randint(0, 16777215),timestamp=(ctx.message.created_at))
    embed_message.set_author(name=f"Application from {ctx.author}",icon_url=(ctx.author.avatar_url))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/PfWlEd5.png")
    await apply_user.send(embed=embed_message)

@client.command(help="get an invite to invite the bot")
async def invite(ctx):
  embed  = discord.Embed(title = "The Invite Links!", value = "One is for testing, one is the normal bot.",color=random.randint(0, 16777215))
  embed.add_field(name = "Testing Link:", value = "https://discordapp.com/oauth2/authorize?client_id=702243652960780350&scope=bot&permissions=8", inline = False)
  embed.add_field(name = "Normal Invite:", value = f"https://discordapp.com/oauth2/authorize?client_id={client.user.id}&scope=bot&permissions=8", inline = False)
  embed.set_thumbnail(url=(client.user.avatar_url))
  await ctx.send(embed=embed)

@client.command(help="gives the id of the current guild or DM if you are in one.")
async def guild_get(ctx):
  if isinstance(ctx.channel, discord.TextChannel):
    await ctx.send(content=ctx.guild.id) 

  if isinstance(ctx.channel,discord.DMChannel):
    await ctx.send(ctx.channel.id)

@client.command(help="This gives random history using Sp46's api.",brief="a command that uses SP46's api's random history command to give you random history responses")
async def random_history(ctx,*,args=None):
  if args is None:
    args = 1
  asuna = asuna_api.Client(session=client.aiohttp_session)
  response = await asuna.random_history(args)
  for x in response:
    await ctx.send(f":earth_africa: {x}")

@client.command(help="a way to view open source",brief="you can see the open source with the link it provides",aliases=["open source"])
async def open_source(ctx):
  source_send=discord.Embed(title="Project at: https://github.com/JDJGInc/JDJGBotSupreme", description="Want to get more info, contact the owner with the JDBot*owner command",color=random.randint(0, 16777215))
  source_send.set_author(name=f"{client.user} Source Code:",icon_url=(client.user.avatar_url))
  await ctx.send(embed=source_send)

@client.command(help="a command to tell you the channel id")
async def this(ctx):
  await ctx.send(ctx.channel.id)
  await ctx.send(ClientConfig.whoami)

@client.command(help="gives you the milkman gif",brief="you summoned the milkman oh no")
async def milk(ctx):
  embed = discord.Embed(title="You have summoned the milkman",color=random.randint(0, 16777215))
  embed.set_image(url="https://i.imgur.com/JdyaI1Y.gif")
  embed.set_footer(text="his milk is delicious")
  await ctx.send(embed=embed)

@client.command(help="gives you who the owner is.")
async def owner(ctx):
  info = await client.application_info()
  if info.team is None:
    owner = info.owner.id
  if info.team:
    owner = info.team.owner_id

  support_guild=client.get_guild(736422329399246990)
  owner=support_guild.get_member(owner)
  if owner.bot:
    user_type = "Bot"
  if not owner.bot:
    user_type = "User"

  guilds_list=[guild for guild in client.guilds if guild.get_member(owner.id)]
  if not guilds_list:
    guild_list = "None"

  x = 0
  for g in guilds_list:
    if x < 1:
      guild_list = g.name
    if x > 0:
      guild_list = guild_list + f", {g.name}"
    x = x + 1
  
  if owner:
    nickname = str(owner.nick)
    joined_guild = owner.joined_at.strftime('%m/%d/%Y %H:%M:%S')
    status = str(owner.status).upper()
    highest_role = owner.roles[-1]
  
  if owner is None:
    nickname = "None"
    joined_guild = "N/A"
    status = "Unknown"
    for guild in client.guilds:
      member=guild.get_member(owner.id)
      if member:
        status=str(member.status).upper()
        break
    highest_role = "None Found"
  
  embed=discord.Embed(title=f"Bot Owner: {owner}",description=f"Type: {user_type}", color=random.randint(0, 16777215),timestamp=ctx.message.created_at)
  embed.add_field(name="Username:", value = owner.name)
  embed.add_field(name="Discriminator:",value=owner.discriminator)
  embed.add_field(name="Nickname: ", value = nickname)
  embed.add_field(name="Joined Discord: ",value = (owner.created_at.strftime('%m/%d/%Y %H:%M:%S')))
  embed.add_field(name="Joined Guild: ",value = joined_guild)
  embed.add_field(name="Part of Guilds:", value=guild_list)
  embed.add_field(name="ID:",value=owner.id)
  embed.add_field(name="Status:",value=status)
  embed.add_field(name="Highest Role:",value=highest_role)
  embed.set_image(url=owner.avatar_url)
  await ctx.send(embed=embed)
  try:
    await RankSystem.GetStatus(ctx.message,owner)
  except:
    await ctx.send("User not in Rank System")

@client.command(help="a command to give information about the team",brief="this command works if you are in team otherwise it will just give the owner.")
async def team(ctx):
  information=await client.application_info()
  if information.team == None:
    true_owner=information.owner
    team_members = []
  if information.team != None:
    true_owner = information.team.owner
    team_members = information.team.members
  embed=discord.Embed(title=information.name,color=random.randint(0, 16777215))
  embed.add_field(name="Owner",value=true_owner)
  embed.set_footer(text=f"ID: {true_owner.id}")
  embed.set_image(url=(information.icon_url))
  for x in team_members:
    embed.add_field(name=x,value=x.id)
  await ctx.send(embed=embed)

@client.command(help="a command to send I hate spam.")
async def spam(ctx):
  embed=discord.Embed(color=random.randint(0, 16777215))
  embed.set_image(url="https://i.imgur.com/1LckTTu.gif")
  await ctx.send(content="I hate spam.",embed=embed)

@client.command(help="a command to give information about a file")
async def file(ctx):
  if len(ctx.message.attachments) < 1:
    await ctx.send(ctx.message.attachments)
    await ctx.send("no file submitted")
  if len(ctx.message.attachments) > 0:
    embed = discord.Embed(title="Attachment info",color=random.randint(0, 16777215))
    for x in ctx.message.attachments:
      embed.add_field(name=f"ID: {x.id}",value=f"[{x.filename}]({x.url})")
      embed.set_footer(text="Check on the url/urls to get a direct download to the url.")
    await ctx.send(embed=embed,content="\nThat's good")

@client.command(help="a command meant to flip coins",brief="commands to flip coins, etc.")
async def coin(ctx, *, args = None):
  if args:
    value = random.choice([True,False]) 
    if args.lower().startswith("h") and value:
      win = True
    elif args.lower().startswith("t") and not value:
      win = True
    elif args.lower().startswith("h") and not value:
      win = False
    elif args.lower().startswith("t") and value:
      win = False    
    else:
      await ctx.send("Please use heads or Tails as a value.")
      return
    
    if(value):
      pic_name = "heads"
    else:
      pic_name ="Tails"

    url_dic = {"heads":"https://i.imgur.com/MzdU5Z7.png","Tails":"https://i.imgur.com/qTf1owU.png"}

    embed = discord.Embed(title="coin flip",color=random.randint(0, 16777215))
    embed.set_author(name=f"{ctx.author}",icon_url=(ctx.author.avatar_url))
    embed.add_field(name="The Coin Flipped: "+("heads" if value else "tails"),value=f"You guessed: {args}")
    embed.set_image(url=url_dic[pic_name])

    if win:
      embed.add_field(name="Result: ",value="You won")
    else:
      embed.add_field(name="Result: ",value="You lost")
    
    await ctx.send(embed=embed)

  if args is None:
    await ctx.send("example: \n```test*coin heads``` \nnot ```test*coin```")

@client.command()
async def stats(ctx):
  embed = discord.Embed(title="Bot stats",color=random.randint(0, 16777215))
  embed.add_field(name="Guild count",value=len(client.guilds))
  embed.add_field(name="User Count:",value=len(client.users))
  await ctx.send(embed=embed)

async def guildinfo(ctx,guild):
  bots = 0
  users = 0
  for x in guild.members:
    if x.bot is True:
      bots = bots + 1
    if x.bot is False:
      users = users + 1
  static_emojis = 0
  animated_emojis = 0
  usable_emojis = 0
  for x in guild.emojis:
    if x.animated is True:
      animated_emojis = animated_emojis + 1
    if x.animated is False:
      static_emojis = static_emojis + 1
    if x.available is True:
      usable_emojis = usable_emojis + 1
  
  embed = discord.Embed(title="Guild Info:",color=random.randint(0, 16777215))
  embed.add_field(name="Server Name:",value=guild.name)
  embed.add_field(name="Server ID:",value=guild.id)
  embed.add_field(name="Server region",value=guild.region)
  embed.add_field(name="Server created at:",value=f"{guild.created_at} UTC")
  embed.add_field(name="Server Owner:",value=guild.owner)
  embed.add_field(name="Member Count:",value=guild.member_count)
  embed.add_field(name="Users:",value=users)
  embed.add_field(name="Bots:",value=bots)
  embed.add_field(name="Channel Count:",value=len(guild.channels))
  embed.add_field(name="Role Count:",value=len(guild.roles))
  embed.set_thumbnail(url=(guild.icon_url))
  embed.add_field(name="Emoji Limit:",value=guild.emoji_limit)
  embed.add_field(name="Max File Size:",value=f"{guild.filesize_limit/1000000} MB")
  embed.add_field(name="Shard ID:",value=guild.shard_id)
  embed.add_field(name="Animated Icon",value=guild.is_icon_animated())
  embed.add_field(name="Static Emojis",value=static_emojis)
  embed.add_field(name="Animated Emojis",value=animated_emojis)
  embed.add_field(name="Total Emojis:",value=f"{len(guild.emojis)}/{guild.emoji_limit*2}")
  embed.add_field(name="Usable Emojis",value=usable_emojis)

  await ctx.send(embed=embed)

@client.command(help="gives you info about a guild",aliases=["server_info","guild_fetch","guild_info","fetch_guild",])
async def serverinfo(ctx,*,args=None):
  if args:
    match=re.match(r'(\d{16,21})',args)
    guild=client.get_guild(int(match.group(0)))
    if guild is None:
      guild = ctx.guild

  if args is None:
    guild = ctx.guild
  
  await guildinfo(ctx,guild)

@client.command(help="a command to find the nearest emoji")
async def emote(ctx,*,args=None):
  if args is None:
    await ctx.send("Please specify an emote")
  if args:
    emoji=discord.utils.get(client.emojis,name=args)
    if emoji is None:
      await ctx.send("we haven't found anything")
    if emoji:
      await ctx.send(emoji)

@client.command(help="this is a way to get the nearest channel.")
async def closest_channel(ctx,*,args=None):
  if args is None:
    await ctx.send("Please specify a channel")
  
  if args:
    if isinstance(ctx.channel, discord.TextChannel):
      channel=discord.utils.get(ctx.guild.channels,name=args)
      if channel:
        await ctx.send(channel.mention)
      if channel is None:
        await ctx.send("Unforantely we haven't found anything")

    if isinstance(ctx.channel,discord.DMChannel):
      await ctx.send("You can't use it in a DM.")

@client.command()
async def pi(ctx):
  await ctx.send(math.pi)

@client.command(help="a command to get the closest user.")
async def closest_user(ctx,*,args=None):
  if args is None:
    await ctx.send("please specify a user")
  if args:
    from difflib import SequenceMatcher
    userNearest = discord.utils.get(client.users,name=args)
    user_nick = discord.utils.get(client.users,display_name=args)
    if userNearest is None:
      userNearest = sorted(client.users, key=lambda x: SequenceMatcher(None, x.name, args).ratio())[-1]
    if user_nick is None:
      user_nick = sorted(client.users, key=lambda x: SequenceMatcher(None, x.display_name,args).ratio())[-1]
    await ctx.send(f"Username: {userNearest}")
    await ctx.send(f"Display name: {user_nick}")
  
  if isinstance(ctx.channel, discord.TextChannel):
    member_list = []
    for x in ctx.guild.members:
      if x.nick is None:
        pass
      if x.nick:
        member_list.append(x)
    
    nearest_server_nick = sorted(member_list, key=lambda x: SequenceMatcher(None, x.nick,args).ratio())[-1] 
    await ctx.send(f"Nickname: {nearest_server_nick}")

  if isinstance(ctx.channel,discord.DMChannel):
    await ctx.send("You unforantely don't get the last value.") 

@client.command(help="a command to send wink gifs",brief="you select a user to send it to and it will send it to you lol")
async def wink(ctx,*, Member: BetterMemberConverter=None):
  if Member is None:
    Member = ctx.author
    
  if Member.id == ctx.author.id:
    person = client.user
    target = ctx.author
  
  if Member.id != ctx.author.id:
    person = ctx.author
    target = Member
  
  sr_client=sr_api.Client(session=client.aiohttp_session)
  image=await sr_client.get_gif("wink")

  embed=discord.Embed(color=random.randint(0, 16777215))
  embed.set_author(name=f"{person} winked at you",icon_url=(person.avatar_url))
  embed.set_image(url=image.url)
  embed.set_footer(text="powered by some random api")

  if isinstance(ctx.channel, discord.TextChannel):
      await ctx.send(content=target.mention,embed=embed) 

  if isinstance(ctx.channel,discord.DMChannel):
    if target.dm_channel is None:
      await target.create_dm()
    
    try:
      await target.send(content=target.mention,embed=embed)
    except discord.Forbidden:
      await ctx.author.send("Failed Dming them...")

@client.command(aliases=["user_info", "user-info", "ui", "whois"], brief="a command that gives information on users", help="this can work with mentions, ids, usernames, and even full names.")
async def userinfo(ctx, *, user: BetterUserconverter = None):
  user = user or ctx.author
  user_type = ['User', 'Bot'][user.bot]
  
  if ctx.guild:
    member_version = await client.getch_member(ctx.guild, user.id)

    if member_version:
      nickname = str(member_version.nick)
      joined_guild = member_version.joined_at.strftime('%m/%d/%Y %H:%M:%S')
      status = str(member_version.status).upper()
      highest_role = member_version.top_role
      
    if not member_version:

      nickname = str(member_version)

      joined_guild = "N/A"
      status = "Unknown"

      for guild in client.guilds:
        member=guild.get_member(user.id)
        if member:
          status=str(member.status).upper()
          break
          
      highest_role = "None Found"

  if not ctx.guild:
    nickname = "None"
    joined_guild = "N/A"
    status = "Unknown"
    for guild in client.guilds:
      member=guild.get_member(user.id)
      if member:
        status=str(member.status).upper()
        break
    highest_role = "None Found"
  
  guilds_list=[guild for guild in client.guilds if guild.get_member(user.id) and guild.get_member(ctx.author.id)]
  if not guilds_list:
    guild_list = "None"

  if guilds_list:
    guild_list= ", ".join(map(str, guilds_list))

  embed=discord.Embed(title=f"{user}",description=f"Type: {user_type}", color=random.randint(0, 16777215),timestamp=ctx.message.created_at)
  embed.add_field(name="Username: ", value = user.name)
  embed.add_field(name="Discriminator:",value=user.discriminator)
  embed.add_field(name="Nickname: ", value = nickname)
  embed.add_field(name="Joined Discord: ",value = (user.created_at.strftime('%m/%d/%Y %H:%M:%S')))
  embed.add_field(name="Joined Guild: ",value = joined_guild)
  embed.add_field(name="Mutual Guilds:", value=guild_list)
  embed.add_field(name="ID:",value=user.id)
  embed.add_field(name="Status:",value=status)
  embed.add_field(name="Highest Role:",value=highest_role)
  embed.set_image(url=user.avatar_url)
  await ctx.send(embed=embed)

  await RankSystem.GetStatus(ctx.message,user)

@client.command(help="a command to give a list of servers(owner only)")
async def servers(ctx):
  if await client.is_owner(ctx.author):
    send_list = [""]
    guild_list = ["%d %s %d %s" % (len(g.members), g.name, g.id, (g.system_channel or g.text_channels[0]).mention) for g in client.guilds]
    for i in guild_list:
      if len(send_list[-1] + i) < 1000:
        send_list[-1] += i + "\n"
      else:
        send_list += [i + "\n"]
    if (ctx.author.dm_channel is None):
      await ctx.author.create_dm()
    await ctx.author.dm_channel.send("\n Servers:")
    for i in send_list:
      await ctx.author.dm_channel.send(i) 
  if await client.is_owner(ctx.author) is False:
    await ctx.send("You can't use that it's owner only")

#Typing Status Support
waitMessage = 0
#commands with embed: help, mail, support, about, update(will soon)
@client.listen()
async def on_message(message):
  await GlobalLinker.respond(message)

  global waitMessage
  user = message.author
  mention = False

  if message.content.startswith(discordprefix+" ") and not message.author.bot:
    message_info=message.content.split(" ")
    while '' in message_info:
      message_info.remove('')
    if len(message_info) > 0:
      x = 2
      message.content = message_info[0]+message_info[1]
      while x < (len(message_info)):
        if x == (len(message_info)-1):
          message.content = (message.content+" "+message_info[-1])
        else:
         message.content = (message.content+" "+message_info[x])
        x = x + 1
      
      x = 0
    
    if mention:
      message.mentions.remove(client.user)
  
  extras = ["jd*"]
  comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
  match = comp.match(message.content)
  if match:
    extras.append(match.group(1))
  for x in extras:
    message.content=message.content.replace(x,discordprefix)

  message_check=re.findall(rf"{discordprefix}[{discordprefix}]",message.content, flags=re.IGNORECASE)
  if len(message_check) > 0:
    check_time=message_check[0]
    if check_time.lower() == discordprefix.lower():
      message.content = message.content.replace(check_time,discordprefix)
    
  if message.reference != None and not message.content.startswith(discordprefix) and not message.author.bot:
    if message.mentions != None and client.user in message.mentions:
      jdjg=client.get_user(168422909482762240)
      await client.get_channel(921939352769167360).send(content=f"{jdjg.mention} {message} \n Content: {message.content} ")
    

  if not message.guild is None and not message.author.bot:
    if message.guild.id in guild_prefixes and not message.author.bot:
      server_prefix=guild_prefixes[message.guild.id]
      if message.content.startswith(server_prefix):
        message.content = message.content.replace(server_prefix,discordprefix)
        print(message.content)

  if message.content.startswith(discordprefix+"verify") and not message.author.bot:
    if message.guild != None:
      if message.guild.id == 736422329399246990:
        if message.channel.id == 736432046821343322:
          await message.channel.send("Vertification time...")
          member_role = message.guild.get_role(736423134449893428)
          await message.author.add_roles(member_role,reason="User Vertification by Bot.")
          return
      if message.guild.id == 748631738908934211:
        if message.channel.id == 779407591511818303:
          await message.channel.send("Vertification time...")
          member_role = message.guild.get_role(748654102040412291)
          await message.author.add_roles(member_role,reason="User Vertification by Bot.")
          member_role = message.guild.get_role(748640407201644624)
          await message.author.add_roles(member_role,reason="User Vertification by Bot.")
          return

  #await bot.send_typing(ctx.channel)
  #CHANNEL LINKER COMMANDS
  if not message.author.bot: #Channel Link Message Repeater
    if not message.content.startswith(discordprefix) and message.guild:
      if (waitMessage==1):
        await GlobalLinker.TestGLink(message)
        waitMessage = 0
      await RankSystem.UpdateScore(message) #For the rank 
      await GlobalLinker.SendMessage(message)
      await GlobalLinker.extend(message)
      for chanId in DatabaseControl.GetLinkedChannelsList(message.channel.id):
        await client.get_channel(chanId).send(embed=GlobalLinker.GetGlobalEmbed(message))
  if message.content.startswith(discordprefix+"GetChannelId") and not message.author.bot:
    await message.channel.send(message.channel.id)
    return
  if message.content.startswith(discordprefix+"link_this") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    DatabaseControl.AddChannelLink(message.channel.id,n1)
    await message.channel.send("This channel was linked to "+ str(client.get_channel(n1)))
    return   
  if message.content.startswith(discordprefix+"link_channel") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    n2 = str(message.content.split(" ")[2])
    n2 = DatabaseControl.to_ChannelId(n2)
    await message.channel.send(DatabaseControl.AddChannelLink(n1,n2))
    return
  if message.content.startswith(discordprefix+"delete_link") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    n2 = str(message.content.split(" ")[2])
    n2 = DatabaseControl.to_ChannelId(n2)
    await message.channel.send(DatabaseControl.DeleteChannelLink_ChanNum(n1,n2))
    return
  if message.content.startswith(discordprefix+"GetLinked") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    await message.channel.send(DatabaseControl.GetLinkedChannels(client,n1))
    return
  if message.content.startswith(discordprefix+"global_list") and not message.author.bot:
    i=0
    embedVar = discord.Embed(title = "Gobal Channels List",color=random.randint(0, 16777215))
    for obj in DatabaseConfig.db.g_link_testing.find():
      i=i+1
      header = str(i) + ": "
      try:
        header = header +str(client.get_guild(obj["ser_id"]).name)
        body  = str(client.get_channel(obj["chan_id"]).name)
      except:
        header = header + "Cannot Connect"
        body = "<#"+str(obj["chan_id"])+">"
      embedVar.add_field(name = header,value = body)
    await message.channel.send(embed = embedVar)
    return
    
  if message.content.startswith(discordprefix+"global_mention") and not message.author.bot:
    i=0
    embedVar = discord.Embed(title = "Gobal Channels List",color=random.randint(0, 16777215))
    for obj in DatabaseConfig.db.g_link_testing.find():
      i=i+1
      header = str(i) + ": "
      try:
        header = header +str(client.get_guild(obj["ser_id"]).name)
        body  = str(client.get_channel(obj["chan_id"]).mention)
      except:
        header = header + "Cannot Connect"
        body = "<#"+str(obj["chan_id"])+">"
      embedVar.add_field(name = header,value = body)
    await message.channel.send(embed = embedVar)
    return

  

#RANK SYSTEM COMMANDS
  if message.content.startswith(discordprefix+"rank") and not message.author.bot:
    await RankSystem.GetStatus(message)
    #await message.channel.send(RankSystem.CheckIfExisting(user))
    return
  if message.content.startswith(discordprefix+"dev_rank") and not message.author.bot:
    await RankSystem.DevGetStatus(client,message)
    #await message.channel.send(RankSystem.CheckIfExisting(user))
    return
  if message.content.startswith(discordprefix+"get_user") and not message.author.bot:
    await message.channel.send("Searching for User")
    await message.channel.send(await GetPfp.get_username(message))
    await message.channel.send("Done!")
    return
    
  if message.content.startswith(discordprefix+"lead") and not message.author.bot:
    await RankSystem.GetTop10(client,message)
    return
  if message.content.startswith(discordprefix+"toggle") and not message.author.bot:
    if not message.guild:
      return
    if not user.guild_permissions.administrator:
      await message.channel.send("You can't use that.")
      return

    args = message.content.split(" ")[1]
    if args == "level_msg":
      await message.channel.send(RankSystem.ToggleLevelUpMsg(message))
    return
#GLOBAL LINKER
  if message.content.startswith(discordprefix+"global") and not message.author.bot:
    args = "NULL"
    try:
      args = message.content.split(" ")[1]
    except:
      await message.channel.send("Did not input an argument!")
    if(args=="link"):
      await message.channel.send(GlobalLinker.AddGlobalLink(client,message))
      return
    if(args=="delete"):
      await message.channel.send(GlobalLinker.TerminateLink(message))
      return
    if(args=="test"):
      await message.channel.send("Next Message sent here will be used as test data")
      waitMessage = 1
      return
    await message.channel.send("Valid arguments are link or delete")
    return
#UPDATE NOTIFY
  if message.content.startswith(discordprefix+"update") and message.author.id in admins and not message.author.bot:
    await UpdateNotify.UpdateNote(message,client)
    return

#OTHER STUFF

  if message.content.startswith(discordprefix+"cc_") and not message.author.bot:
    from PIL import Image
    import Pixman
    new_cmd = message.content.replace(discordprefix+"cc_","").split(" ")[0]
    
    
    mode =0
    if ('1' in new_cmd):
      mode=1
    if ('2' in new_cmd):
      mode=2
   
   
    if (new_cmd != new_cmd.replace("view","")):
      wire=mode
      if(wire<2):
        await color_code.veiw(message.author,message.channel,wire,0)
      else:
        _user = message.author
        _color_code = color_code.get(_user)
        decoder = Pixman.ram()
        image  = Pixman.get()
        image.decode(decoder.b(_color_code))
        image.render()
        image.export("render.png")
        await message.channel.send("Color Code of "+_user.name+"```"+_color_code+"```")
        await message.channel.send(file=discord.File('render.png'))
    
    if(new_cmd != new_cmd.replace("iv","")):
      #View
      if(mode<2):
        await color_code.veiw(message.author,message.channel,mode,1)
      else:
        _user = message.author
        _color_code = color_code.invert(color_code.get(_user))
        decoder = Pixman.ram()
        image  = Pixman.get()
        image.decode(decoder.b(_color_code))
        image.render()
        image.export("render.png")
        await message.channel.send("Color Code of "+_user.name+"```"+_color_code+"```")
        await message.channel.send(file=discord.File('render.png'))
    
    if (new_cmd != new_cmd.replace("test","")):
      instructs = message.content.replace("JDBot*cc_test ","")
      wire=mode
      print(wire)
      if(wire<2):
        #await color_code.veiw("NULL",message.channel,wire,0)
        if(instructs[0]=='8'):
          await color_code.veiw_raw(instructs,message.channel,wire)
        else:
          await color_code.veiw("NULL",message.channel,wire,0)
      else:
        _user = message.author 
        _color_code = color_code.get(_user)
        decoder = Pixman.ram()
        image  = Pixman.get()
        image.decode(decoder.b(_color_code))
        image.render()
        image.export("render.png")
        await message.channel.send("Color Code of "+_user.name+"```"+_color_code+"```")
        await message.channel.send(file=discord.File('render.png'))
      await message.delete()

      
    if(new_cmd != new_cmd.replace("save"," ")):
      #Save
      new_cmd=new_cmd.replace("save ","")
      if (new_cmd[0] != ' '):
        color_code.save(message.author,new_cmd)
        await message.delete()
        await message.channel.send("Color Code Saved!")
      else:
        print(new_cmd)
        await message.delete()
        await message.channel.send("Invalid Format!")

      

    if(new_cmd != new_cmd.replace("invert","")):
      #Invert
      if(color_code.valid_cc(message.author)):
        color_code.save(message.author,color_code.invert(color_code.get(message.author)))
        await message.channel.send("Color Code Inverted And Saved!")

    
    return
  
  #from better_profanity import profanity
  if not message.author.bot:
    if GlobalLinker.isGlobalChannel(message.channel.id):
      for x in bad_list:
        if x.lower() in message.content.lower():
          try:
            banned_response=random.choice(random_response.response_used)
            await message.channel.send(banned_response)
          except discord.errors.Forbidden:
            return

  for banned_word in banned_words:
    if message.guild == None:
      pass
    elif banned_word in message.content.lower() and message.guild.id in slur_censor:
      try:
        await message.delete()
        banned_response=random.choice(random_response.response_used)
        await message.channel.send(banned_response)
      except discord.errors.Forbidden:
        return
    
  if message.content.startswith(discordprefix+"settings") and not message.author.bot:
    import server_settings
    arg = message.content.split(" ")
    #for obj in arg:
    #  print(obj)
    message_return = 0
    print("arg1: "+arg[1]+" arg2: "+arg[2])
    if(arg[1]=="level" and arg[2]=="up" and arg[3]=="message"):
      server_settings.change_setting(message.guild,1,"NULL")
      message_return = 1
    if(arg[1]=="safe" and arg[2]=="server"):
      server_settings.change_setting(message.guild,2,"NULL")
      message_return = 2
    if(arg[1]=="slur" and arg[2]=="ok"):
      args = arg[3:]
      server_settings.change_setting(message.guild,3,args)
      message_return = 3
    if(arg[1]=="prefix" and arg[2]=="change"):
      print(arg[3])
      server_settings.change_setting(message.guild,4,arg[3])
      message_return = 4
    if(arg[1]=="admin" and arg[2]=="add"):
      args = arg[3:]
      server_settings.change_setting(message.guild,5,args)
      message_return = 5
    if(arg[1]=="ban" and arg[2]=="users"):
      args = arg[3:]
      server_settings.change_setting(message.guild,6,args)
      message_return = 6
    if(arg[1]=="test"):
      args = arg[2:]
      mess=""
      for word in args:
        if(len(mess)!=0):
          mess = mess+" "+word
        else:
          mess = mess + word 
      print(mess)
      import swear_checker
      await message.channel.send(swear_checker.censor_message(mess,message.guild.id))
      return
    message_return = message_return -1
    messages = ["Level Up Message","Safe Server","Slur Ok","Prefix","Admin Add","Ban List"]
    if(message_return <5-1):
      await message.channel.send(messages[message_return]+" Toggled!")
    else:
      await message.channel.send(messages[message_return]+ " Added To Database")
    if(message_return==-1):
      await message.channel.send("Invalid Arguments!")
      em = discord.Embed(title="Vaild Commands")
      em.add_field(name="level up", value=".")
      em.add_field(name="safe server", value=".")
      em.add_field(name="slur ok <args>", value=".")
      em.add_field(name="prefix change <new prefix>", value=".")
      em.add_field(name="admin add <admin id>", value=".")
      em.add_field(name="ban users <args>", value=".")
      await message.channel.send(embed=em)
    
    #   1 - Level Up Messages
    #   2 - Safe Server
    #   3 - Slur Ok [args]
    #   4 - prefix change
    #   5 - admin add
    #   6 - Ban List
    #server_settings.change_setting(message.guild,1,"a")
    return

  test=await client.get_context(message)
  if message.content.startswith(discordprefix) and mention == False and not message.author.bot and test.valid is False:
    pfp = message.author.avatar_url
    time_used=(message.created_at).strftime('%m/%d/%Y %H:%M:%S')
    embed_message = discord.Embed(title=f" {message.content}", description=time_used,color=random.randint(0, 16777215))
    embed_message.set_author(name=f"{message.author} tried to excute invalid command:",icon_url=(pfp))
    embed_message.set_footer(text = f"{message.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/bW6ergl.png")
    await client.get_channel(921939352769167360).send(embed=embed_message)
    await message.channel.send("That's not a valid command.")
    return

#RENDEV'S CODE...NO TOUCH
@client.event
async def on_message_delete(message):
  if not message.author.bot:
    if(len(message.content)==0):
      message.content = "NULL"
      
    try:
     can = await GlobalLinker.FindGlobal(message)
     for obj in can:
        channel = client.get_channel(int(obj["chan_id"]))
        msg= await channel.fetch_message(obj["mes_id"].id)
        await msg.delete()
    except:
      banana = 0

#typing_timer=[]
@client.event
async def on_typing(channel,user,_time):
  #if not user.bot:
    #try:
    #go_for_it = 1
    #for obj in typing_timer:
    #  if(channel.id ==obj.name ):
    #    diff =obj.t.minute - _time.minute 
    #    if(diff<0):
    #      diff=(obj.t.minute-60)-_time.minute
    #    if(diff>4):
    #      go_for_it=0

    #docs = DatabaseConfig.db.g_link_testing.find()
   # for chan in docs:
     # if (chan["chan_id"]!=channel.id):
       # print("CHAN_ID: "+str(chan["chan_id"]))
       # try:
          #print(client.get_channel(int(chan["chan_id"])).name)
          #if(go_for_it):
            #await client.get_channel(int(chan["chan_id"])).trigger_typing()
        #except:
         # banana = 1
    #return
    #except:
  return

@client.event
async def on_message_edit(before,after):
  #print("EDIT")
  
  if(len(before.content)==0 or before.content is None):
    before.content = "NULL"
  if(len(after.content)==0 or after.content is None):
    after.content = "NULL"
    
  if not after.author.bot:
    try:
     can = await GlobalLinker.FindGlobal(before)
     newEmbed = GlobalLinker.GetGlobalEmbed(after)
     for obj in can:
        channel = client.get_channel(int(obj["chan_id"]))
        msg= await channel.fetch_message(obj["mes_id"].id)
        await msg.edit(embed = newEmbed)
    except:
      banana = 0

@client.event
async def on_error(name,*arguments,**karguments):
  import traceback
  idle_error=traceback.format_exc()
  if len(idle_error) < 2049:
    embed_message = discord.Embed(title="Error:",description=idle_error,color=random.randint(0, 16777215))
    embed_message.add_field(name="More Details:",value=karguments)
    embed_message.set_footer(text=f"Discord details: \n{arguments}")
    traceback.print_exc()
    print(f"\n{arguments}")
    try:
      for adID in admin_contact2:
        admin_user = client.get_user(adID)
        if (admin_user.dm_channel is None):
          await admin_user.create_dm()
        try:
          await admin_user.send(embed=embed_message)
        except:
          print(adID)
    except:
      print("\n can't DM them")
    await client.get_channel(921939352769167360).send(embed=embed_message)
  if len(idle_error) > 2049:
    traceback.print_exc()
    print(f"\n{arguments}")
    print("\n message was way too big for discord")
  a=os.sys.exc_info()
  message_error=arguments[0]
  if isinstance(message_error, discord.Message):
    jdjg = client.get_user(168422909482762240)
    if (jdjg.dm_channel is None):
      await jdjg.create_dm()
    mystbin_client = mystbin.Client(session=client.aiohttp_session)
    paste = await mystbin_client.post(message_error.content)
    await jdjg.send(f"Error: {paste.url}")
    #try:
      #member_permissions=message_error.channel.permissions_for(message_error.guild.me)
      #if member_permissions.send_messages == True:
        #if(isinstance(a[1],discord.errors.HTTPException)):
          #await message_error.channel.send("Error occuried(please try shorterning your messages)") 
        #if(isinstance(a[1],discord.errors.Forbidden)):
          #await message_error.channel.send("Either you didn't setup the bot right(a.k.a missing permissions) or the bot fell into a cricital error")
    #except discord.errors.Forbidden:
      #pass

@client.event
async def on_invite_create(invite):
  try:
    invite.revoked
    invite.guild
    invite.max_age
    invite.code
    print(invite.inviter)
    invite.id
    invite.url
    invite.uses
    creation_date = (invite.created_at).strftime('%m/%d/%Y %H:%M:%S')
  except discord.errors.Forbidden:
    pass

@client.event
async def on_invite_delete(invite):
  try:
    invite.revoked
    invite.guild
    invite.max_age
    invite.code
    print(invite.inviter)
    invite.id
    invite.url
    invite.uses
  except discord.errors.Forbidden:
    pass

banned_words = [
  'faggot',
  'retard',
  'pussy',
  'bastard',
  'nigga',
  ]

#for banned words a.k.a slurs and such (don't open if you aren't a programmer - or easily offended


token_grab = os.environ['Discordtoken']


client.loop.create_task(startup())
client.run(token_grab)

#token_grab uses Discordtoken - for 24/7 bot and Discordtoken2 for testing purposes
#(nightly bot - current open source code)
