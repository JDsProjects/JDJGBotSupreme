import pytz
import datetime
from os import system, name

def clear(): 
  
  # for windows 
  if name == 'nt': 
      _ = system('cls') 

  # for mac and linux(here, os.name is 'posix') 
  else: 
      _ = system('clear') 

#Thank you https://www.geeksforgeeks.org/clear-screen-python/


while True:

  time_database99 = [
    "Etc/GMT+7",
    "Etc/GMT-3",
    "Etc/GMT+4",
    "Etc/GMT+6",
    "Etc/GMT+4",
    "Etc/GMT+7",
    "Etc/GMT+4",
    "Etc/GMT-1",
    "Etc/GMT-10",
    "Etc/GMT+0",
  ]

  #it's actually the reverse for real Gmt values, and when daylight savings time happens the etc/gmt+4 location will change(it's gmt-4) in actual timezones.

  x = 0

  y = 0

  people = [
    "RenDev:",
    "Nicks:",
    "JDJG:",
    "The Hook:",
    "Redstone Wiz:",
    "Crimson:",
    "Shadi:",
    "Salimi:",
    "Rodimus:",
    "Nightcore:",

  ]



  for x in range(len(time_database99)):

    #len tells the len of the object time_database99

    time_here=(datetime.datetime.now(pytz.timezone(time_database99[x])).strftime("%m/%d/%Y %H:%M:%S"))
    #the [x] is there to tell which part of the list to use.

    #format command.
    person_name = people[x]
    print(person_name+" "+time_here)

    x = x + 1

  print("\n Hit Enter to Update Times")

  input("\n Press any key to continue . . .")

  clear()
