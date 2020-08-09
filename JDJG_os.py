import random
import time
import datetime # don't double import
from pytz import timezone #all good
import math
import clear_code

def program_os():

  version_info = "0.0.1"

  time_location = "America/New_York"

  #for now anyway

  #Port this program to discord.py soon...

  operating_system = "PythonOS"

  print("\n Booting",operating_system)

  on = True

  logon = input("\n What is your username?:")

  clear_code.clear()

  os_commands = [
    "cls",
    "clear",
    "exit",
    "break",
    "log off",
    "list commands",
    "random number",
    "ver",
    "version",
    "time",
    "username",
    "date",
    "datetime",
    "help",

  ]

  while on == True:

    display_name = logon+"@"+operating_system+":"

    command_console = input(display_name)

    print("\n")

    if command_console == "cls" or command_console == "clear":

      clear_code.clear()

    if command_console == "exit" or command_console == "break" or command_console == "log off":

      print("\n Logging out of console")

      break
    
    if command_console == "list commands":

      command_amount = len(os_commands)

      command_count = 0

      while command_count < command_amount:

        print(os_commands[command_count])

        command_count = command_count+1

    if command_console == "random number":

      number_one = input("Starting number:")

      number_two = input("\n Ending number:")

      #incomplete code(JDJG Bot has it anyway)

      #good_or_bad=type(number_one)

      #https://note.nkmk.me/en/python-check-int-float/#:~:text=float%20has%20is_integer()%20method,an%20integer%2C%20and%20False%20otherwise.&text=For%20example%2C%20a%20function%20that,function%20returns%20False%20for%20str%20.

      #if good_or_bad == "str":

        #print("Not good")

    if command_console == "time":

      time_info = (datetime.datetime.now(timezone(time_location)).strftime("%H:%M:%S"))

      print(time_info)

    if command_console == "date":

      value_search = "%m/%d/%Y"

      time_info = (datetime.datetime.now(timezone(time_location)).strftime(value_search))

      print(time_info)

    
    if command_console == "datetime":

      value_search = "%m/%d/%Y %H:%M:%S"

      time_info = (datetime.datetime.now(timezone(time_location)).strftime(value_search))

      print(time_info)

    
    if command_console == "ver" or command_console == "version":

      print(version_info)

    if command_console == "username":

      usage = logon

      print(usage)

    if not command_console in os_commands:

      print("\n not A valid command")

    print("\n")

#now ported to https://repl.it/@JDJGInc_Offical/JDJGBotSupreme#JDJG_os.py

#og code at https://repl.it/@JDJGInc_Offical/Python-os-Console#main.py (I will write the rest here....)