import discord

from os import environ

import random

import time

import aiohttp

import requests

all_commands = "\n rm - is random messages"+"\n ad -advice"+"\n help is how you get help"+"\n Owner(bot makers) has access to change the status - a.k.a with JDBot*status(it's admin only for safetly reasons)"+"\n rn is random number(ability to choose starting and ending numbers will be added soon...)"+"\n time will give you the current bot time"+"\n About is who made it"+"\n say repeats what you say"+"\n support contacts the bot makers in Admin and gets their support(Okay so... well you can choice DM or send it to a certain channel)"+"\n mail allows you to send messages to people in Dms soon.."+"\n Log off is a command to turn off the bot(admins only)"+"\n Support as includes Suggestions(more features will be added soon)"+"\n"

game_status = "Running the Bot with Repl.it(thank You Nomic Zorua (Imanton1), idea and some code made by JDJG, and thanks to shadi for also helping making this bot"

client = discord.Client(status=discord.Status.do_not_disturb, activity=discord.Game(game_status))

#be careful not to have a * anywhere else,
#or the text will be italicised
discordprefix = "JDBot*"

##Replace admins with your user ids on discord for you to be admins, and the help commands with your prefix, basically replace JDBot* with your prefix of choice if you want to.

@client.event
async def on_ready():
  print("Bot is ready. \n")

async def help(message):
  if (message.author.dm_channel is None):
    await message.author.create_dm()
    await message.author.dm_channel.send("Help is on the way!")

    helpmsg = "\n prefix is JDBot*, commands are:\n "+all_commands

    embed_message = discord.Embed(title="About(commands):", description=helpmsg)

  await message.author.dm_channel.send(embed=embed_message)

admins = [
  168422909482762240,
  269904594526666754,
  717822288375971900
]

get_updates = [
  168422909482762240,
  660295633223024671,
  717822288375971900
]

#adding an id(if you have access to the source code and want to fork it, credit us, getting your discord id is easy, replace ours with the ones you are playing to use)

send_channel = [
  556242984241201167, #my server
  730895828855554069, #for my friend's shadi server(who is trying a fork to see how it works)
  730940969196847164,
  722675262256316488, #one for you to use if you want to
]


#support channels(get contacted of a support message)

@client.event
async def on_message(message):

  if message.content.startswith(discordprefix+"help"):
    await help(message)

  if message.content.startswith(discordprefix+"rm"):
    #rm = random message
    answer = random_message()
    await message.channel.send(answer)

  if message.content.startswith(discordprefix+"ad"):

    answer = ad() 

    await message.channel.send(answer)

  if message.content.startswith(discordprefix+"status") and message.author.id in admins:
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(message.content[len(discordprefix+"status "):]))


  #if message.content.startswith(discordprefix+"rn"):

    #random_number = generator(message.content[len(discordprefix+"rn"):])))

    #await message.channel.send(random_number)

  if message.content.startswith(discordprefix+"about"):

    embed_message = discord.Embed(title="About(commands):", description=all_commands)

    user_send = message.author.id

    user_send2 = client.get_user(user_send)

    if (user_send2.dm_channel is None):

      await user_send2.create_dm()

    await user_send2.send(embed=embed_message)

    embed_message2 = discord.Embed(title="About(credits):", description=credits)

    await user_send2.send(embed=embed_message2)

  if message.content.startswith(discordprefix+"time"):
  
    current_time = current_timexp()

    await message.channel.send(current_time)

  if message.content.startswith(discordprefix+"say"):

    current_message = message.content[len(discordprefix+"say"):]

    if current_message == "":

      current_message = "are you trying to crash me?"

    await message.channel.send(current_message)
    

  if message.content.startswith(discordprefix+"support DM"):

    support_msg=message.content[len(discordprefix+"support DM"):]

    for adID in admins:

      admin_user = client.get_user(adID)
   
      #print(admin_user)  #just a test... (looping it will allow it to send it to all the admins) - works

      if (admin_user.dm_channel is None):

        await admin_user.create_dm()

      support_msg2 = "Message from <@%d> (%d) : %s" % (message.author.id, message.author.id, support_msg)
      
      who_sent = str(message.author)

      embed_message = discord.Embed(title=who_sent, description=support_msg2)


      await admin_user.send(embed=embed_message)
      


  if message.content.startswith(discordprefix+"mail"):

    mail_msg = message.content[len(discordprefix+"mail"):]

    user_sendto = 168422909482762240

    #will be able to select which user to go to id

    author_id = str(message.author.id)
      
    who_sent = "Mail from: \n"+str(message.author)+"\n with the id of "+author_id+"\n:"


    embed_message = discord.Embed(title=who_sent, description=mail_msg)

    address = client.get_user(user_sendto)

    if (address.dm_channel is None):

      await address.create_dm()
      
    await address.send(embed=embed_message)

  if message.content.startswith(discordprefix+"log off") and message.author.id in admins:
    
    await message.channel.send("Shutting off")

    await client.logout()

    #ability to log off

  if message.content.startswith(discordprefix) and message.author.id in admins:

    if message.content.startswith(discordprefix+"update"):

      update_msg = message.content[len(discordprefix+"update"):]

      for updateID in get_updates:
        
        get_updates_epic = client.get_user(updateID)

      if (get_updates_epic.dm_channel is None):

        await get_updates_epic.create_dm()

      await get_updates_epic.send(update_msg)




  if message.content.startswith(discordprefix+"support channel"):
    support_msg = message.content[len(discordprefix+"support channel"):]

    normal_username=str(message.author)

    #It allows us to get the username in full with the username and tag. unless you have something else to use...(repl.it also has a chat.)

  # I like comments, it shows what I'm talking about

    support_msg2 = str(support_msg)

    user_info = "Message from "+"\n ("+str(message.author.id)+") \n "+normal_username+":"

    embed_message33 = discord.Embed(title=user_info, description=support_msg2)

    for cid in send_channel:

      channel_id99=client.get_channel(cid)

      await channel_id99.send(embed=embed_message33)

  #if message.content  #evuntally - the DM collection code

      

random_responses_all = [
"Alright",
"10/10 It tastes bad",
"attack of the killer Nuggets",
"I have a new epic idea \n it's a horror game",
"bruh",
"well we're doomed",
"I'm coming",
"For freedom",
"I have no comment",
"Well I... frick",
"Why did you post that?",
"Wait what?",
"New Movie idea World War Karen(Karens v.s. the world)",
"Stop Banning people when they don't deserve that",
"I shouldn't have said that",
"frick me",
]
random_responses = []

def random_message():
  global random_responses
  if len(random_responses) == 0:
    random_responses = random_responses_all
    random.shuffle(random_responses)
  return "\n"+random_responses.pop()

ad_all = [
  "Hey Fun fact in Project64 you can copy cheats in the cheat file(just have things that makes it easier to copy(you need to open it in Sublime or Notepad++ in order to read that(a.k.a notepad does't work on just it's own",
"When I say eh, it can have many meanings, also take what I say with a grain of salt at times.",
"I can edit javascript code, because one it's easy to see, but I also know python.(I mainly know python but I can understand other programming languages because they are all similar in a couple of ways)",
"Trust is how you truly get along with people, you might not fully trust your friends, but you might as well do trust them a bit",
"True friends have their falls and don't always get along, but they will always be able to get able to hang out around better",
"never moderate with a person feeling, basically never have your emotions bring you head on, use crictial thinking as well, and forgive them, however if they keep doing it, then think about it",
"Not all choices are the best, but try to choose the best one",
"to be the best person, you need to learn from your mistakes and be true to yourself, and don't be a jerk to others, and fight others who can't themselves(people are thrown down, because of their status, a.k.a bullied), also don't let people make you a worse person by changing yourself to what they want entirely(have your own choices) ",
"I really don't have any advice right now",
"Advice is something you might need time to time, but it's what you do with it, that counts",
"Be nice when you can but you can still be mean when you need to(don't go overboard)",
"don't let people have power over you",
"not all authority is good, try to find the good people in life to hang out with",
"Not all advice is spelled correctly..",
]

credits = "\n Programmer - Nomic Zorua (Imanton1)#6488 \n Programmer - JDJG Inc. Official#3493 \n Programmer - Shadi#7879(for ranks and such+and some cool new features)- bit of help from him(thank You :D)"+"\n Invite link is https://discordapp.com/oauth2/authorize?client_id=702238592725942374&scope=bot&permissions=8"+"\n coded on Python"+"\n Open source on https://repl.it/@JDJGInc_Offical/JDJGBotSupreme (check it out) - it's open source so you can see how it works"


ad_some = []

help_some = []

def ad():
  global ad_some
  if len(ad_some) == 0:
    ad_some = ad_all
    random.shuffle(ad_some)
  return "\n"+ad_some.pop()

def help_program():

  global help_some

  if len(help_some) == 0:

    help_some == all_commands

  return "\n"+help_some.pop()



def current_timexp():

  #Don't delete any of these variables, please

  currenttime99=time.localtime()

  current_year = currenttime99.tm_year

  current_month = currenttime99.tm_mon

  current_dayofmonth = currenttime99.tm_mday

  current_hour = currenttime99.tm_mday

  current_minute = currenttime99.tm_min

  current_second = currenttime99.tm_sec

  current_dayoftheweek = currenttime99.tm_wday

  current_yearday = currenttime99.tm_yday

  current_timezone = currenttime99.tm_zone

  current_daylightsavingstime = currenttime99.tm_isdst

  #currentgmfoff = currenttime99.tm_gmtoff

  #seconds away from UTC, in this case there is none

  if current_daylightsavingstime == 0:

    savings_time = "\n No daylight's saving time in play"

  if current_daylightsavingstime == 1:

    savings_time = "\n Daylight's saving time in effect"

  

  time_current = str(current_month)+"/"+str(current_dayofmonth)+"/"+str(current_year)+" "+str(current_hour)+":"+str(current_minute)+":"+str(current_second)+" in "+str(current_timezone)+str(savings_time)

  return time_current

def generator(numbers):

  result = random.randint(1,100)

  #should be able to take two numbers and make them the two values the program is looking for

  return result 

client.run(environ['Discordtoken'])

