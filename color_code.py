import random
def cc_inverter(color_code_passed):

  complete_color_code = ""

  x = 0

  while x < len(color_code_passed):

    last_bit="\n"+color_code_passed[x]

    complete_color_code=complete_color_code+last_bit

    x = x + 1
    
    
  complete_color_code=complete_color_code.upper()

  

  #you might want to convert this to a database fetching for Cometspectrum

  Inverted_color_code = []

  Inverted_color_code_inverted = []

  #the arraries will be using later to store the inverted code.

  times_ran_1 = 0
  lines=complete_color_code.split("\n")

  #makes this into a list

  while times_ran_1 < len(lines):

    if '' == lines[times_ran_1]:

      times_ran_1 = times_ran_1+1

      Inverted_color_code.append('')

      Inverted_color_code_inverted.append('')

    if not '' == lines[times_ran_1]:

      break

  #this is to check to make sure it will start at an actual value, rather than not starting at an actual value and causing the program to crash.

  #"" are added to make sure the code will match.

  x = int(times_ran_1)

  color_counter = 0
  times_ran_program_1 = 0

  #the actual inverter function is copied later and is slightly tweaked to be the inverted_color_code. 


  while x+1 < len(lines):

    color_value = lines[x]

    color_value2 = lines[x+1]

    colored_bit=color_value.split(" ")

    colored_bit2 = color_value2.split(" ")

    color_code_front = colored_bit[0]

    color_code_front2 = colored_bit2[0]

    color_section = colored_bit[1]

    color_section2 = colored_bit2[1]
    r = int(color_section[0:2], 16)
    g = int(color_section[2:4], 16)
    b = int(color_section2[0:2], 16)

    #fetches values from the values above(the inverter itself could be reused.)
    r = 0xFF - r
    g = 0xFF - g
    b = 0xFF - b

    bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"

    first_color_line =  bits_used998[0:4].upper()

    second_color_line = bits_used998[4:6].upper()

    #this works either way, but I wanted to make sure that the color code would be the same.

    color_code_needed = color_code_front+" "+first_color_line

    color_code_needed_2 = color_code_front2+" "+second_color_line+color_section2[2:4]

    Inverted_color_code.append(color_code_needed)

    Inverted_color_code.append(color_code_needed_2)

    x = x +2

    color_counter = color_counter + 1

    times_ran_program_1 = times_ran_program_1 + 1

  times_ran_1 = 0

  #the counter is set back to 0 and the values have been appended.

  times_ran_1 = 0

  #basically the same code as before.

  while times_ran_1 < len(Inverted_color_code):

    if '' == Inverted_color_code[times_ran_1]:

      times_ran_1 = times_ran_1+1

    if not '' == Inverted_color_code[times_ran_1]:

      break

  z = int(times_ran_1)

  while z < len(Inverted_color_code):

    color_value = Inverted_color_code[z]

    color_value2 = Inverted_color_code[z+1]

    colored_bit=color_value.split(" ")

    colored_bit2 = color_value2.split(" ")

    color_code_front = colored_bit[0]

    color_code_front2 = colored_bit2[0]

    color_section = colored_bit[1]

    color_section2 = colored_bit2[1]
    r = int(color_section[0:2], 16)
    g = int(color_section[2:4], 16)
    b = int(color_section2[0:2], 16)
    r = 0xFF - r
    g = 0xFF - g
    b = 0xFF - b

    #this is basically the same code, as used before, but this time, it's using inverted_Color_code.

    bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"
    first_color_line =  bits_used998[0:4].upper()

    second_color_line = bits_used998[4:6].upper()
    color_code_needed_2 = color_code_front+" "+first_color_line

    color_code_needed_2 = color_code_front2+" "+second_color_line+color_section2[2:4]
    Inverted_color_code_inverted.append(color_code_needed)

    Inverted_color_code_inverted.append(color_code_needed_2)

    #appends inverted color code.

    z = z +2


  if Inverted_color_code_inverted == lines:

    pass

    if not Inverted_color_code_inverted == lines:

      pass

  #checks if they are correct and match.
      
  j = 0

  test_string99 = ""

  #this is adding the data back into a string.

  while j < len(Inverted_color_code):

    test_string99 = test_string99+(Inverted_color_code[j]+"\n")


    j = j + 1

  return test_string99

  #orginally it would print it, but we will be returning this value.




import DatabaseConfig
import discord
def VaildateUser(_user):
  try:
    DatabaseConfig.db.color_code.insert_one({"user_id":_user.id,"color":["NULL"]})
    return 1
  except:
    return 0
def SaveColorCode(_user, color_code):
  VaildateUser(_user)
  user = DatabaseConfig.db.color_code.find_one({"user_id":_user.id})
  user['color'] = color_code
  DatabaseConfig.db.color_code.delete_one({"user_id":_user.id})
  DatabaseConfig.db.color_code.insert_one(user)
def ReturnColorCode(_user):
  user = DatabaseConfig.db.find_one({"user_id":_user.id})
  return "banana"
def GetEmbed(_user, invert = 0):
  embedVar = discord.Embed(title = _user.author.name+"'s Color Code",color=random.randint(0, 16777215))
  color_code = ReturnColorCode(_user)
  val = None
  for obj in color_code:
    val+='\n'+obj
  embedVar.add_field(name = "Color Code:",value = val)
def normalize(_color_code):
  color_code = []
  for obj in _color_code:
    color_code.append(obj.replace(" ",""))
  new_code = []
  is_other = (len(color_code[0])==len(color_code[1]))
  if(is_other):
    i=-1
    while i<(len(color_code)/2):
      new_code.append(color_code[i]+color_code[i+1])
      i+=1
    return new_code
  else:
    return color_code