import DatabaseConfig
import DatabaseControl
import ClientConfig
import GetPfp
import discord
client  = ClientConfig.client
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
async def SendMessage(message):
  for gChan in DatabaseConfig.db.g_link_testing.find():
        if message.channel.id == gChan['chan_id']:
          for gChan in DatabaseConfig.db.g_link_testing.find():
            if message.guild.id != gChan['ser_id']:
              embedVar = discord.Embed(title=message.guild.name)
              embedVar.set_author(name=str(message.author),icon_url=message.author.avatar_url)
              embedVar.set_thumbnail(url = GetPfp.GetServerPfp(message))
              embedVar.add_field(name=str(message.author),value=str(FilterMessage(message)),inline=True)
              try:
                await client.get_channel(gChan['chan_id']).send(embed=embedVar)
              except:
                banana = 1
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

