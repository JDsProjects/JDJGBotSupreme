import random
def invert(complete_color_code):

  complete_color_code=complete_color_code.upper()
  

  #you might want to convert this to a database fetching for Cometspectrum

  Inverted_color_code = []

  Inverted_color_code_inverted = []

  #the arraries will be using later to store the inverted code.

  times_ran_1 = 0
  lines=complete_color_code.split("\n")

  #makes this into a list

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
    DatabaseConfig.db.color_code.insert_one({"user_id":_user.id,"color":"NULL"})
    return 1
  except:
    return 0
def get(_user):
  VaildateUser(_user)
  user = DatabaseConfig.db.color_code.find_one({"user_id":_user.id})
  return user['color']
def valid_cc(_user):
  if(get(_user)=="NULL"):
    return 0
  return 1
def save(_user, color_code):
  VaildateUser(_user)
  user = DatabaseConfig.db.color_code.find_one({"user_id":_user.id})
  user['color'] = color_code
  DatabaseConfig.db.color_code.delete_one({"user_id":_user.id})
  DatabaseConfig.db.color_code.insert_one(user)

async def veiw(_user,channel, wire,ins = 0):
#  import Pixman
#  _color_code = get(_user)
#  if(ins):
#    _color_code = invert(_color_code)
#  decoder = Pixman.ram()
#  image  = Pixman.get()
#  image.decode(decoder.b(_color_code))
#  image.render()
#  image.export("render.png")

 # await channel.send("Color Code of "+_user.name+"```"
  #+_color_code+"```")
 #await channel.send(file=discord.File('render.png'))
  import _3D
  _color_code = get(_user)
  if(ins):
    _color_code = invert(_color_code)
  marioRender = _3D.mario()
  marioRender.render(_color_code,wire)
  await channel.send("Color Code of "+_user.name+"```"+_color_code+"```")
  await channel.send(file=discord.File('render.png'))
