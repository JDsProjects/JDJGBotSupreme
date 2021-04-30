import DatabaseConfig

class DataCode:
  good_name = "NULL"
  aliases = []

  def __init__(self, good_name, aliases):
    self.good_name = good_name
    self.aliases = aliases


class UserCodes:
  code_types = [
      DataCode("Switch", [
          "NX",
          "switch"
        ]),
              DataCode("Wii U", [
          "wii u",
          "wii",
          "WII U",
        ]),
              DataCode("3DS", [
          "3DS"
        ]),
  ]

  data_code_types = [
      DataCode("Super Smash Bros.", [
          "SSBU",
          "SSB",
          "Super Smash Bros",
          "Super Smash Bros Ultimate"
        ]),
      DataCode("Super Mario Maker", [
        "SMM",
        "SMM2",
        "Mario Maker",
        "Mario Maker 2",
        "Super Mario Maker 2",
      ]),
      DataCode("Super Mario Odyssey", [
        "Mario Odyssey",
        "SMO",
        "Luigis Baloon World",
        "Baloon",
        "Luigi's Balon World"
      ])
  ]



  reg_codes = []
  user_id = 0
  cached_doc = "NULL"

  def __init__(self, user_id):
    self.user_id = user_id
    self.isExisting(user_id)

    self.cached_doc = DatabaseConfig.db.users_testing.find_one({"user_id": user_id})

    self.reg_codes = self.cached_doc["codes"]


  def isExisting(user_id):
    try:
      dummy_doc = DatabaseConfig.db.users_testing.find_one({"user_id": user_id})
      dumy_string = dummy_doc["user_id"]
      return True
    except:
      try:
        dummy_doc = DatabaseConfig.db.users_testing.find_one({"user_id": user_id})
        dummy_doc["user_id"]
        #if we have made it past this point it means all we
        #have to do is update the struct
        new_doc = {
          "user_id" : dummy_doc["user_id"],
          "level" : dummy_doc["level"],
          "exp" : dummy_doc["exp"],
          "last_exp" : dummy_doc["last_exp"],
          "codes": []
        }
        DatabaseConfig.users_testing.delete_one({"user_id": user_id})
        DatabaseConfig.db.users_testing.insert_one(new_doc)
      except:
        #user has never used JDBot before
        new_doc = {
          "user_id" : user_id,
          "level" : 0,
          "exp" : 0,
          "last_exp" : 0,
          "codes": []
        }
        DatabaseConfig.db.users_testing.insert_one(new_doc)

  #this function will take a user's intput of what type
  #they are looking for and it will turn that into a valid
  #data reference from the defined data_code_types
  def linker(self, alias):
    for code in self.code_types:
      if(alias.lower() == code.lower()):
        return code
    for data_type in self.data_code_types:
      for type_alias in data_type.aliases:
        if(type_alias.lower() == alias.lower()):
          return data_type.good_name
    raise Exception("Linker: Reference not defined :" + str(alias))

  #This function will take int the raw code type that the
  #user might have not typed correctly and links it to the
  #corrrect data type as well as appends the data to the user
  #This function returns true or false based on the
  #function's success and requires all feilds
  def addCode(self, title, code_type, code):
    try:
      linked_reference = self.linker(code_type)
    except:
      return False
    self.reg_codes[linked_reference].append({"title":title, "id": code})
    return True
  

  #will get a code from the database based on either
  #the name or the code. Only 1 of the 
  #two feilds are required
  def getCode(self, code = "NULL", title = "NULL"):
    mode = -1
    
    if(code == "NULL"):
      mode = 0

    if(title == "NULL"):
      mode = 1

    if(mode == -1):
      raise Exception("getCode: NOT VALID GET MODE");

    for i1 in range(len(self.reg_codes)): #gets the list of datatypes
      for i in range(len(self.reg_codes[i1])): #iterates through the elemetnts in that data type
        if(mode == 0):
          if(int(self.reg_codes[i1][i]["code"]) == int(code)):
            return self.reg_codes[i1][i]
        if(mode == 1):
          if(int(self.reg_codes[i1][i]["title"]) == int(title)):
            return self.reg_codes[i1][i]
    return False #default return


  #will delete a code from the database based on either
  #the name or the code. Returns true or false. 
  #based on if the element was found. Only 1 of the 
  #two feilds are required
  def deleteCode(self, code = "NULL", title = "NULL"):
    mode = -1
    
    if(code == "NULL"):
      mode = 0

    if(title == "NULL"):
      mode = 1

    if(mode == -1):
      raise Exception("deleteCode: NOT VALID DELETE MODE");

    for i1 in range(len(self.reg_codes)): #gets the list of datatypes
      for i in range(len(self.reg_codes[i1])): #iterates through the elemetnts in that data type
        if(mode == 0):
          if(int(self.reg_codes[i1][i]["code"]) == int(code)):
            self.reg_codes[i1].pop(i)
            return True
        if(mode == 1):
          if(int(self.reg_codes[i1][i]["title"]) == int(title)):
            self.reg_codes[i1].pop(i)
            return True
    return False #default return


  #Will get a list of all codes and 
  #return it as a string array
  def getCodeList(self):
    #use three spaces for a tab
    ret = []
    ret.append("Friend Code Types: ")
    for _type in self.code_types:
      ret.append("   "+ str(_type.good_name))
    ret.append(" ")
    ret.append("Game Code Types: ")
    for d_type in self.data_code_types:
      ret.append("   " + d_type.good_name)
      ret.append("   " + d_type.good_name + "'s Ailases:")
      for alias in d_type.aliases:
        ret.append("   "+ "   " + alias)
      ret.append(" ")
    return ret


  #makes a printout of the User's data
  #returns a string list
  def toString(self):
    ret = []
    for gerne in self.reg_codes:
      ret.append(gerne.good_name)
      for doc in gerne:
        ret.append("   " + doc.title + " = " + doc.code)
    return ret
  
  #class destructor
  def __del__(self):
    DatabaseConfig.db.users_testing.delete_one({"user_id" :self.user_id })
    self.cached_doc["codes"] = self.reg_codes
    DatabaseConfig.db.users_testing.insert_one(self.cached_doc)
    
    