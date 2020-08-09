import discord
import DatabaseConfig
def defDoc(num, val,guildId):
  doc = [guildId,"NULL","NULL","NULL"]
  doc[num] = val
  return {"ser_id":doc[0],"title":doc[1],"body_head":doc[2],"body":doc[3]}
def GetArgs(message):
  args = ""
  tmpmsg = message.content
  tmpmsg = tmpmsg.replace("JDBot*update ","")
  tmpmsg = tmpmsg.replace("[title] ","")
  tmpmsg = tmpmsg.replace("[body_head] ","")
  tmpmsg = tmpmsg.replace("[body] ","")
  return tmpmsg
  i = -1
  for arg in message.content.split(" "):
    i=i+1
    if i > 0:
      args = args + str(arg)
      if i+1 != len(message.content.split(" ")):
        args=args+" "
  return args
async def UpdateNote(message,client):
  mode = "NULL"
  banana=0
  args =[ "NULL","NULL"]
  try:
    mode = message.content.split(" ")[1]
  except:
    banana=0
  try:
    args[0] = GetArgs(message)
  except:
    banana=0
  if mode == "[title]":
    try:
      DatabaseConfig.db.update_note.insert_one({"ser_id":message.guild.id,"title":args[0],"body_head":"NULL","body":"NULL"})
    except:
      doc = DatabaseConfig.db.update_note.find_one({'ser_id':message.guild.id})
      DatabaseConfig.db.update_note.delete_one(doc)
      DatabaseConfig.db.update_note.insert_one({'ser_id':doc['ser_id'],'title':args[0],'body_head':doc['body_head'],'body':doc['body']})
  if mode == "[body_head]":
    try:
      DatabaseConfig.db.update_note.insert_one({"ser_id":message.guild.id,"title":"NULL","body_head":args[0],"body":"NULL"})
    except:
      doc = DatabaseConfig.db.update_note.find_one({'ser_id':message.guild.id})
      DatabaseConfig.db.update_note.delete_one(doc)
      DatabaseConfig.db.update_note.insert_one({'ser_id':doc['ser_id'],'title':doc['title'],'body_head':args[0],'body':doc['body']})
  if mode == "[body]":
    try:
      DatabaseConfig.db.update_note.insert_one({"ser_id":message.guild.id,"title":"NULL","body_head":"NULL","body":args[0]})
    except:
      doc = DatabaseConfig.db.update_note.find_one({'ser_id':message.guild.id})
      DatabaseConfig.db.update_note.delete_one(doc)
      DatabaseConfig.db.update_note.insert_one({'ser_id':doc['ser_id'],'title':doc['title'],'body_head':doc['body_head'],'body':args[0]})
  if mode == '[preview]':
    try:
      doc = DatabaseConfig.db.update_note.find_one({'ser_id':message.guild.id})
    except:
      banana=0
    embedVar = discord.Embed(title=doc['title'])
    embedVar.add_field(name=doc['body_head'],value=doc['body'],inline =True)
    if (message.author.dm_channel is None):
      await message.author.create_dm()
    await message.author.dm_channel.send(embed=embedVar)
  if mode=='[set]':
    await message.channel.send(SetChannel(message))
  if mode=='[send]':
    doc = DatabaseConfig.db.server_settings.find_one({"ser_id":message.guild.id})
    try:
      doc1 = DatabaseConfig.db.update_note.find_one({'ser_id':message.guild.id})
      embedVar = discord.Embed(title=doc1['title'])
      embedVar.add_field(name=doc1['body_head'],value=doc1['body'],inline =True)
      await client.get_channel(doc['up_chan']).send(embed=embedVar)
    except:
      if (message.author.dm_channel is None):
        await message.author.create_dm()
      await message.author.dm_channel.send("There is no channel specified to send this update message to! Please define what channel you would like to send updates to with 'JDBot*update set' in the channel that you would like to send messages to")
  
def SetChannel(message):
  try:
    DatabaseConfig.db.server_settings.insert_one({"ser_id":message.guild.id,"st":0,"up_chan":message.channel.id})
    return "Update Channel Linked"
  except:
    doc = DatabaseConfig.db.server_settings.find_one({"ser_id":message.guild.id})
    DatabaseConfig.db.server_settings.delete_one(doc)
    DatabaseConfig.db.server_settings.insert_one({"ser_id":message.guild.id,"st":doc['st'],"up_chan":message.channel.id})
    return "There was already a channel set to recive updates so it was deleted and this one was linked instead!"