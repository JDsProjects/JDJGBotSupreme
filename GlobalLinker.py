import DatabaseConfig
import DatabaseControl
import ClientConfig
import GetPfp
import discord
from profanity import censor_profanity
client  = ClientConfig.client

def censor_text(message):
  message=censor_profanity(message)
  return message

def AddGlobalLink(client,message):
  this = message.channel.id
  thisSer = message.guild.id
  tmp_doc = DatabaseConfig.db.g_link_testing.find_one({"ser_id":thisSer})
  try:
    DatabaseConfig.db.g_link_testing.insert_one({"ser_id":thisSer,"chan_id":this})
    return "Global Link Added!"
  except:
    DatabaseConfig.db.g_link_testing.delete_one(tmp_doc)
    DatabaseConfig.db.g_link_testing.insert_one({"ser_id":thisSer,"chan_id":this})
    return "This server already had a Global Chat Room so the old one was deleted and this channel has been Linked instead!"
def FilterMessage(message):
  tmp_msg = str(message.content)
  for men in message.mentions:
    tmp_msg = tmp_msg.replace(str("<@!"+str(men.id)+">"),men.name)
  return tmp_msg
banned_list = [
629060550525190145,
691713870238187530,
573593846772924418,
535629244517056531,
742845516743704776,

]
async def SendMessage(message):
  if message.author.id in banned_list:
    return

  for gChan in DatabaseConfig.db.g_link_testing.find():
        if message.channel.id == gChan['chan_id']:
          for gChan in DatabaseConfig.db.g_link_testing.find():
            if message.guild.id != gChan['ser_id']:
             # try:
              #  print(client.get_guild(gChan['ser_id']).name)
              #except:
              #  print("Error " + str(gChan['ser_id']))
              embedVar = discord.Embed(title=message.guild.name,description=str(FilterMessage(message)),inline=True)
              embedVar.set_author(name=str(message.author),icon_url=message.author.avatar_url)
              embedVar.set_thumbnail(url = GetPfp.GetServerPfp(message))
              try:
                await client.get_channel(gChan['chan_id']).send(embed=embedVar)
              except:
                print(gChan['chan_id'])

async def TestGLink(message):
  embedVar = discord.Embed(title=message.guild.name)
  embedVar.set_author(name=str(message.author),icon_url=message.author.avatar_url)            
  embedVar.set_thumbnail(url = GetPfp.GetServerPfp(message))
  val = str(FilterMessage(message))
  images = message.attachments
  for obj in images:
    val=val + (""+obj.url)
  embedVar.add_field(name=str(message.author),value=val,inline=True)
  await message.channel.send(embed = embedVar)
def TerminateLink(message):
  DatabaseConfig.db.g_link_testing.delete_one({'ser_id':message.guild.id})
  return "Deleted Link forever" 



async def FindGlobal(message):
  docs = DatabaseConfig.db.g_link_testing.find()
  ret = []
  for chan in docs:
    try:
      channel = ClientConfig.client.get_channel(int(chan["chan_id"]))
      if(message.channel.id!=channel.id):
        #print("SEARCHING")
        messages = await channel.history(limit=100).flatten()
        for msg in messages:
          if msg.author.bot:
            embedVar = msg.embeds[0]
            fields = embedVar.fields
            if (fields[0].name == str(message.author)):
              if(fields[0].value==str(message.content)):
                ret.append({"mes_id":msg,"chan_id":channel.id})
    except:
      banana = 1
  return ret

def GetGlobalEmbed(message):
  embedVar = discord.Embed(title=message.guild.name)
  embedVar.set_author(name=str(message.author),icon_url=message.author.avatar_url)            
  embedVar.set_thumbnail(url = GetPfp.GetServerPfp(message))
  val = str(FilterMessage(message))
  images = message.attachments
  for obj in images:
    val=val + ("\n"+obj.url)
  embedVar.add_field(name=str(message.author),value=val,inline=True)
  return embedVar



async def display_guilds_id(message):
  for gChan in DatabaseConfig.db.g_link_testing.find():
    string = ""
    string = string + str(client.get_channel(int(gChan["chan_id"])).name)
    await message.channel.send(string)



async def extend(message):
  if(ClientConfig.whoami==0):
    return
  if(message.author.id == ClientConfig.whoami):
    return
  if(message.channel.id == 782123846781370368):
    return
  if(message.channel.id != 782123846781370368 and not message.author.bot):
    gChan = DatabaseConfig.db.g_link_testing.find_one({"ser_id":message.guild.id})
    try:
      gChan["chan_id"]
    except:
      return
    if(gChan["chan_id"]==message.channel.id):
      await client.get_channel(782123846781370368).send(embed = GetGlobalEmbed(message))
    return
    print("ERROR IN EXTENDER: JDJGBOT")


async def respond(message):
  return
  if(ClientConfig.whoami==0):
    return
  try:
    if(message.guild.id != 736422329399246990):
      return
  except:
    return
  if(ClientConfig.whoami==message.author.id):
    return
  print("WHOAMI: "+ str(ClientConfig.whoami) +" : "+str(message.author.id))
  #return
  if(message.author.bot):
    print("********************************************")
    print("BOT NAME: " + str(message.author.name))
    print("GUILD NAME: " + str(message.guild.name))
    print("CHANNEL NAME: " + str(message.channel.name))
  if message.author.bot:
    if(ClientConfig.whoami!=message.author.id):
      if(message.channel.id == 782123846781370368):
        for gChan in DatabaseConfig.db.g_link_testing.find():
          if message.guild.id != gChan['ser_id']:
            try:
              await client.get_channel(gChan['chan_id']).send(embed=message.embeds[0])
            except:
              print("ERROR: NO ACCESS TO CHANNEL: "+str(gChan['ser_id']) + " : "+str(gChan['chan_id'])+"\nCONTANCT RENDEV OR DELETE THIS SERVER FROM DATABASE")
         # except:
        #      print("ERROR IN RESPONDER: SHADIBOT")
        #      print(gChan['chan_id'])
        #      banana = 1;
      else:
        banana =0
        #print("chanID: "+str(message.channel.id) + str(message.author) + str())