import DatabaseConfig
from bson import ObjectId
def CheckIfExisting(user):
  doc = DatabaseConfig.db.users_testing.find_one({"user_id":user.id})
  if doc != "":
    print(1)
    return 1
  else:
    print(0)
    return 0
def UpdateScore(user):
  if CheckIfExisting(user)==1:
    doc = DatabaseConfig.db.users_testing.find_one({"user_id":user.id})
    exp = int(doc['exp']) +10
    level = doc['level']
    if exp > 1000:
      exp=0
      level = doc['level'] + 1
    DatabaseConfig.db.users_testing.delete_one(doc)
    doc['exp'] = exp
    doc['level'] = level
    doc['user_id'] = user.id
    DatabaseConfig.db.users_testing.insert_one(doc)
  else:
    doc = {"user_id":user.id,"level":0,"exp":0}
    DatabaseConfig.db.users_testing.insert_one(doc)
def GetStatus(client,message):
  doc = ""
  if CheckIfExisting(message.author)==1:
    doc = DatabaseConfig.db.users_testing.find_one({"user_id":message.author.id})
  else:
    doc = {"user_id":message.author.id,"level":0,"exp":0}
    DatabaseConfig.db.users_testing.insert_one(doc)
  client.message.channel.send("Rank of "+str(message.author))
  client.message.channel.send("\tLevel: "+str(doc.level))
  client.message.channel.send("\tExperience: "+str(doc.exp))
  client.message.channel.send("\tExperience till Level up: "+str(1000-doc.exp))