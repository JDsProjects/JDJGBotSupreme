import DatabaseConfig
import DatabaseControl
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