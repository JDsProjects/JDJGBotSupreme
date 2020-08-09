import DatabaseConfig
import datetime
import math
import discord
from bson import ObjectId

def GetNextLevelUp(level):
  return math.floor(((level/1.5)*(level/1.5)*(level/1.5))+150)
def CheckIfExisting(user):
  try:
    now = datetime.datetime.now()
    doc = {"user_id":user.id,"level":0,"exp":0,"last_exp":now.minute}
    DatabaseConfig.db.users_testing.insert_one(doc)
    return 0
  except:
    return 1
async def UpdateScore(message):
  user = message.author
  if CheckIfExisting(user)==1:
    now = datetime.datetime.now()
    doc = DatabaseConfig.db.users_testing.find_one({"user_id":user.id})
    exp = int(doc['exp'])
    level = int(doc['level'])
    next_level_exp = GetNextLevelUp(level)
    if now.minute != int(doc['last_exp']):
      exp=exp+10
    if exp > next_level_exp+GetNextLevelUp(level-1):
      level = doc['level'] + 1
      doc2 = DatabaseConfig.db.server_settings.find_one({'ser_id':message.guild.id})
      try:
        if doc2['st']==1:
          await message.channel.send("Congrats <@"+str(user.id)+">! You have just leveled up to level "+str(level)+"!")
      except:
        await message.channel.send("Congrats <@"+str(user.id)+">! You have just leveled up to level "+str(level)+"!")
    DatabaseConfig.db.users_testing.delete_one(doc)
    doc['exp'] = exp
    doc['level'] = level
    doc['user_id'] = user.id
    doc['last_exp'] = now.minute
    DatabaseConfig.db.users_testing.insert_one(doc)
def GetRank(user,server="all"):
  ret =[]
  user_dat = DatabaseConfig.db.users_testing.find_one({"user_id":user.id})
  for doc in DatabaseConfig.db.users_testing.find():
    if server=="all":
      ret.append(int(doc['exp']))
    else:
      for users in server.members:
        if doc['user_id']==users.id:
          ret.append(int(doc['exp']))
  ret.sort(reverse=True)
  i=0
  for xp in ret:
    i=i+1
    if xp==int(user_dat['exp']):
      return i


async def GetTop10(client,message):
  ret=[]
  i=-1
  try:
    args = message.content.split(" ")[1]
  except:
    try:
      args = message.content.split(" ")[2]
    except:
      args="local"
  if args=="global":
    for doc in DatabaseConfig.db.users_testing.find():
      ret.append(doc['exp'])
    ret.sort(reverse=True)
    embedVar = discord.Embed(title="Top 10 Leaderboard [Global]")
    for xp in ret:
      i=i+1
      if i<10:
        try:
          doc = DatabaseConfig.db.users_testing.find_one({"exp":xp})
          embedVar.add_field(name="#"+str(i+1)+". "+str(client.get_user(doc['user_id'])),value=str(doc['exp']),inline = True)
        except:
          banana=0
    await message.channel.send(embed=embedVar)
  else:
    embedVar = discord.Embed(title="Top 10 Leaderboard [Local]")
    for users in message.guild.members:
      try:
        ret.append(int(DatabaseConfig.db.users_testing.find_one({"user_id":users.id})['exp']))
      except:
        banana=0
    ret.sort(reverse=True)
    #embedVar = discord.Embed(title=)
    for xp in ret:
      i=i+1
      if i<10:
        doc = DatabaseConfig.db.users_testing.find_one({"exp":xp})
        embedVar.add_field(name="#"+str(i+1)+". "+str(client.get_user(doc['user_id'])),value=str(doc['exp']),inline = True)
    await message.channel.send(embed=embedVar) 
        
        


      

    

async def GetStatus(message):
  doc = ""
  user = message.author
  if CheckIfExisting(user)==1:
    doc = DatabaseConfig.db.users_testing.find_one({"user_id":user.id})
    level= int(doc['level'])
    exp = int(doc['exp'])
    next_level_exp = GetNextLevelUp(level)
    embedVar = discord.Embed(title="Rank of "+str(user))
    embedVar.add_field(name="Global Rank   ",value=str(GetRank(message.author)))
    embedVar.add_field(name="Server Rank",value =str(GetRank(message.author,message.guild)),inline=True)
    embedVar.add_field(name="Level" ,value=str(doc['level']))
    embedVar.add_field(name="Experience: ",value=str(doc['exp']))
    embedVar.add_field(name="Experience till Level up: ",value=str((GetNextLevelUp(level-1)+next_level_exp)-exp))
    await message.channel.send(embed=embedVar)
def GetUserByName(client,message):
  args = ""
  i = -1
  for arg in message.content.split(" "):
    i=i+1
    if i > 0:
      args = args + str(arg)
      if i+1 != len(message.content.split(" ")):
        args=args+" "
  for user in client.get_all_members():
    if str(user.name).startswith(args):
      return user.id
  return 1232123

async def DevGetStatus(client,message):
  doc = ""
  user = client.get_user(GetUserByName(client,message))
  if CheckIfExisting(user)==1:
    doc = DatabaseConfig.db.users_testing.find_one({"user_id":user.id})
    level= int(doc['level'])
    exp = int(doc['exp'])
    next_level_exp = GetNextLevelUp(level)
    embedVar = discord.Embed(title="Rank of "+str(user))
    embedVar.add_field(name="Global Rank",value=str(GetRank(user)))
    embedVar.add_field(name="Server Rank",value =str(GetRank(user,message.guild)),inline=True)
    embedVar.add_field(name="Level" ,value=str(doc['level']))
    embedVar.add_field(name="Experience: ",value=str(doc['exp']))
    embedVar.add_field(name="Experience till Level up: ",value=str((GetNextLevelUp(level-1)+next_level_exp)-exp))
    await message.channel.send(embed=embedVar)
def ToggleLevelUpMsg(message):
  try:
    DatabaseConfig.db.server_settings.insert_one({'ser_id':message.guild.id,'st':1})
    ret_str = "Level Up Messages Enabled"
  except:
    ret_str = ""
    doc = DatabaseConfig.db.server_settings.find_one({'ser_id':message.guild.id})
    st = doc['st']
    if st == 1:
      st=0
      ret_str = "Level Up Messages Enabled"
    else:
      st=1
      ret_str = "Level Up Messages Disabled"
    DatabaseConfig.db.server_settings.delete_one(doc)
    DatabaseConfig.db.server_settings.insert_one({'ser_id':message.guild.id,"st":st})
    return ret_str
    
