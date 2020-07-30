from bson import ObjectId
def AddPost(dbsGroup,post):
  post_id = dbsGroup.insert_one(post).inserted_id
  return post_id
def getPost(dbsGroup,ID):
  return dbsGroup.find_one({"_id":ID})
def AddChannelLink(dbsGroup,Channel_Source, Channel_destination):
  document = {"src":Channel_Source,"dest":Channel_destination}
  document_id = dbsGroup.insert_one(document).inserted_id
  return document_id
def DeleteChannelLink_ID(dbsGroup,ID):
  dbsGroup.delete_one({'_id': ObjectId(str(ID))})
  return (str(ID)+" Deleted")
def DeleteChannelLink_ChanNum(dbsGroup,Channel_Source,Channel_destination):
  tmp_doc = {"src":Channel_Source,"dest":Channel_destination}
  dbsGroup.delete_one(tmp_doc)
  return "Deleted Link"
def GetLinkedChannels(dbsGroup,Channel_Source):
  ret_str = "Channel "+str(Channel_Source)+" is linked to "
  for doc in dbsGroup.find():
    if(doc['src']==int(Channel_Source)):
      ret_str = ret_str + str(doc['dest']) + ", "
  return ret_str
def GetLinkedChannelsList(dbsGroup,Channel_Source):
  ret=[]
  for doc in dbsGroup.find():
    if(doc['src']==int(Channel_Source)):
      ret.append(doc['dest'])
  return ret

#DISCORD.PY
