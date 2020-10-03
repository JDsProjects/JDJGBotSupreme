import ClientConfig
def GetServerPfp(message):
  
  contents = message.content.split(" ")
  
  id_bit = 0
 
  try:

    id_bit = int(contents[1])
 
  except:

    id_bit = int(message.guild.id)
  
  guild_fetched=ClientConfig.client.get_guild(id_bit)

  server_icon=guild_fetched.icon_url

  return server_icon




def GetUserPfp(message):
  
  contents = message.content.split(" ")
  
  id_bit = 0
 
  try:

    id_bit = int(contents[1])
 
  except:

    id_bit = int(message.author.id)

  server_icon=ClientConfig.client.get_user(id_bit).avatar_url
  return server_icon

def DownloadAllPfp(message):
  for obj in message.guild.members:
    print(obj.avatar_url)