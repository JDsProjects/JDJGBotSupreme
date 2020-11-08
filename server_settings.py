import DatabaseConfig
import discord
col = DatabaseConfig.db.server_settings
def toggle_bool(_bool):
  if(_bool):
    return 0
  else:
    return 1
def setup_server(guild):
  try:
    doc = col.find_one({"ser_id":guild.id})
    col.delete_one({"ser_id":guild.id})
  except:
    doc = "NULL"
  try:
    safe = doc["safe"]
  except:
    safe = 1
  try:
    st = doc["st"]
  except:
    st = 1    
  try:
    slur = doc["slur"]
  except:
    slur = []
  try:
    pfix = doc["pfix"]
  except:
    pfix = "JDBot*"
  try:
    admins = doc["admins"]
  except:
    admins = []
  try:
    ban = doc["ban"]
  except:
    ban = []
  doc = {"ser_id":guild.id,"admins":admins,"ban":ban,"st":st,"safe":safe,"slur":slur,"pfix":pfix}
  return doc

def change_setting(guild,setting,args):
  doc = setup_server(guild)
  #setting
  #   1 - Level Up Messages
  #   2 - Safe Server
  #   3 - Slur Ok [args](why tho)
  #   4 - prefix change
  #   5 - admin add
  #   6 - Ban List
  #args (slurs)
  #   1 - N*****
  #   2 - S***
  #   3 - F***
  #   4 - 
  #args (prefix change)
  #   - prefix
  #args (admins)
  #   - admin_id
  #args (user)
  #   - userid
  if(setting==1):
    doc["st"] = toggle_bool(doc["st"])
  if(setting==2):
    doc["safe"] = toggle_bool(doc["safe"])
  if(setting==3):
    for arg in args:
      if not (arg in doc["slur"]):
        doc["slur"][arg] = doc["slur"].append(arg)
      else:
        doc["slur"][arg] = doc["slur"].remove(arg)
  if(setting==4):
    doc["pfix"] = args
  if(setting==5):
    doc["admins"].append(args)
  if(setting==6):
    doc["ban"].append(args)
  col.insert_one(doc)
def view(guild):
  doc = setup_server(guild)
  em = discord.Embed(title = "NULL")
  em.add_field(name="Level up Messages",value=doc["st"])
  em.add_field(name="Level up Messages",value=doc["st"])
  em.add_field(name="Level up Messages",value=doc["st"])