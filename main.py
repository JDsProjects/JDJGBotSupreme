import discord
#import discord.ext
import os
import asyncio
import random
import time
import sqlite3
from discord.ext import commands, tasks # don't use these
from discord.ext.commands import Bot, Cog # don't use these
from random import choice # don't import the same thing twice
from itertools import cycle # this import is only really used for really complex math, which you aren't doing.
import datetime # don't double import
from typing import Optional   #This is advanced, rarly used, and not used in the code
from discord import Embed, Member #don't double import
import aiohttp  #do not use
import requests #do not use unless you know why your doing
from pytz import timezone #all good
import pymongo
import discord_webhook
from difflib import SequenceMatcher
from discord import Webhook, AsyncWebhookAdapter
import tweepy
import youtube_dl
import itertools
import functools
import math
from async_timeout import timeout
from clear_code import clear
import DatabaseControl
import RankSystem
import GlobalLinker
import UpdateNotify
import DatabaseConfig
import urllib3
import numpy as np
from bs4 import BeautifulSoup
import requests

#don't delete any import statements - some things might be not used

#will add JDJG_os soon, as well as My recolor program(maybe)

#JDJG_os will be embed and be good soon(but right now it needs some upgrades)

client = discord.Client()

#don't touch the database

time_location = "America/New_York"  #The current timezone.
#DATABASE LOGIN MOVED TO DATABASECONFIG.PY

all_commands = """rm - is random messages
ad -advice
help is how you get help
Owner(bot makers) has access to change the status - a.k.a with status(it's admin only for safetly reasons)
rn is random number(ability to choose starting and ending numbers will be added soon...)
time will give you the current bot time
About is who made it
say repeats what you say
support contacts the bot makers in Admin and gets their support(Okay so... well you can choice DM or send it to a certain channel)
mail allows you to send messages to people in Dms soon..
Log off is a command to turn off the bot(admins only)
clear is now avaible(manage messages only...)
Support also includes Suggestions(more features will be added soon)
coin is coin flip try with coin flip <heads or tails> (it will tell you if you're right.>
Webhook updates(JDJG only)

Color to convert values:

use from to values then more

Example:

color hex decimal ff8a00

More commands

Emote(find a emote in the servers the bot is in(might not be that accurate but it's alright)

servers(gives some server info- admins only)

Tweet - gives messages from Usernames

exmaple:


tweet MikeTV 99

webhook - works url then message

example:

webhook <url> hey
------------------------

doesn't work the other way

(might be more):

wc is for creating a webhook

you must Use

wc <name> <reason>

You must have have an attached image

You can't grab the avatar url(instead just change the icon in it's settings...)

power - get the root of the power so if you do JDBot*square 3 1 it will be 3, and stuff like that(it won't work if you do JDBot*square three one)

radical will be like the number and using radical 3 so if you did 27 it would become 3

Like JDBot*radical 27 3 = 3"""



all_commands2 = """Work is for well seeing how well two things get a long.

(I am not adding a ship command... if I really need to, then ask...)

But it will say who requested the command.

Try the help command and reading the source code for all the features

DMing the bot will send what you send to us.

Database fuctionality is provided by well you can see if you read the source code

If you want a feature, just ask... or try a command and it will send it to us like :

hey - will be the most powerful command(vc is to make a voice channel, mc is make channel)

Time setting is now a thing....(so commands will no longer work at a certain time...)

The insult command to insult you, why?

(Fun Fact it will question your ideas.....)

Eh...

compliment is here as well
apply bloopers I would like <role>, <message(reason why)>

Arithmetic <starting_number> <number_multipled each time> <times_multipled>
link_channel
delete_link
GetLinked
GetChannelId
rank
global
"""

commmands_here=[
  "help",
  "rm",
  "ad",
  "rn",
  "about",
  "time",
  "say",
  "support DM ",
  "support channel",
  "mail",
  "clear",
  "rank",
  "lead"
]
admin_commands = [
"log off",
"dev_rank",
"link_channel",
"delete_link",
"global",
"toggle [sub-command]",
"update [sub-command]",
"GetLinked",
"GetChannelId",
"status",
"e_con"
]
commands_discription=[
"The help message you are veiwing right now",
"Sends a random message to the channel that the command was recieved from",
"Gives random advice to you just when you ask for it :)",
"Gives you a random number between a given range",
"Old Help Page",
"Gives the current time in the JDJG time zone!",
"Bot repeats what you say...sort of like a robot!",
"Does nothing for some reason",
"Also does nothing",
"Send mail to your best Discord Friends! Irl or not Irl! Creates a dm containing your mail to the specified user",
"Clears the last thing you said in that channel",
"Displays your current rank in the server as well as all linked servers",
"Shows the leaderboard for the rank system. Use JDBot*lead local for server leaderboards and JDBot*lead global for the leaderboard for all connected servers"
]
admin_commands_discription =[
  "Turns off JDJG bot for all servers",
  "Gets the rank of the specified user",
  "Merge two channels from any server into one combined chat room",
  "Delete a linked channel from any channel or server",
  "Defines a global channel that can be merged with all other servers global channel so that users can partisipate in a global chat room",
  "Toggles JDBot Settings such as level up messages!",
  "Notify people about important events that are happening in your server!",
  "Get all channels linked to the current Channel",
  "Gets the current channel Id",
  "JDBot goes into sleep mode and displays no custom status for 5 seconds?"
]
admin_commands_usage_discription=[
"JDBot*log off",
"JDBot*dev_rank USERNAME_NO_DISCRIMINATOR",
"JDBot*link_channel CHANNEL1_ID CHANNEL2_ID",
"JDBot*delete_link CHANNEL1_ID CHANNEL2_ID",
"JDBot*global",
"JDBot*toggle level_msg",
"JDBot*update [sub-subcommand] <sub commands are : title,body_head, body, preview,set,send>",
"JDBot*GetLinked",
"JDBot*GetChannelId",
"JDBot*status"
]
bad_value = [
  "",
  " ",
]

#commmands_here = commands that the code can currently do

jdjg_id = [
  168422909482762240,
  393511863385587712,

]

application_user = [
  708167737381486614,
  168422909482762240,

]


#jdjg's id only(don't add any more)

async def status_task():
    while True:
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="use JDBot*help for the commands"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="with Repl.it"))
        await asyncio.sleep(4)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="the creators:"))
        await asyncio.sleep(6)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="Nomic Zorua"))
        await asyncio.sleep(4)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="JDJG and Shadi"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="RenDev and LinuxTerm"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="JDJG Bot will DM you two servers join if you want help from the bot makers - from about command or help command"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="(the first one is the support server), though the blooper server will tend to do it now - second one"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="use JDBot!help for the test commands"))
        await asyncio.sleep(5)
        

#be careful not to have a * anywhere else,
#or the text will be italicised

discordprefix = "JDBot*"

#commands.Bot(discordprefix = discordprefix) Don't mix cog and on_message syntax

##Replace admins with your user ids on discord for you to be admins, and the help commands with your prefix, basically replace JDBot* with your prefix of choice if you want to.

@client.event
async def on_ready():
  print("Bot is ready.\n")
  client.loop.create_task(status_task())

async def help(message):
  if (message.author.dm_channel is None):
    await message.author.create_dm()
  embedVar2 = discord.Embed(title="User Commands")
  i=-1
  print(len(commmands_here))
  print(len(commands_discription))
  for x in commmands_here:
    i=i+1
    print(i)
    embedVar2.add_field(name=x,value=commands_discription[i],inline=True)
  await message.author.dm_channel.send(embed=embedVar2)
  if message.author.id in admins:
    embedVar1 = discord.Embed(title="Admin Commands")
    i=-1
    for x in admin_commands:
      i=i+1
      embedVar1.add_field(name=x,value=admin_commands_discription[i]+" usage: "+admin_commands_usage_discription[i],inline=True)
    await message.author.dm_channel.send(embed=embedVar1)

  return
  #Old help message replaced with new one above ^^^. If you are sad that the old help message is gone, please contact RenDev and he will listen to your dispute
  await message.author.dm_channel.send("Help is on the way!")
  helpmsg = "prefix is JDBot*, commands are:\n "+all_commands
  embed_message = discord.Embed(title="About(commands):", description=helpmsg)
  await message.author.dm_channel.send(embed=embed_message)

  helpmsg2 = "prefix is JDBot*, More commands are:\n "+all_commands2

  embed_message = discord.Embed(title="About(commands):",description=helpmsg2)

  await message.author.dm_channel.send(embed=embed_message)
  
  embed_message = discord.Embed(title="About(legal):",description=legal_info)

  await message.author.dm_channel.send(embed=embed_message)

   
    

admins = [
  168422909482762240,
  269904594526666754,
  717822288375971900,
  357006546674253826,
  723179380058357860,
]

get_updates = [
  168422909482762240,
  660295633223024671,
  717822288375971900,
  357006546674253826 #rendev
]

#adding an id(if you have access to the source code and want to fork it, credit us, getting your discord id is easy, replace ours with the ones you are playing to use)

send_channel = [
  556242984241201167, #my server
  730940969196847164,
  722675262256316488, #one for you to use if you want to
]

from_to_channel={
  488487653608521768:556242984241201167,
}


user_sleeptime = {
  168422909482762240:"21 0 0",
  717822288375971900:"21 0 0",

}


user_waketime = {
  168422909482762240:"6 0 0",
  717822288375971900:"6 0 0",

}

user_timezone = {
  168422909482762240:"America/New_York",
  717822288375971900:"America/New_York",


}


id_override = [
  168422909482762240,

]

birthday_functions = {
  269904594526666754:"7 19",
  168422909482762240:"7 3",



}

#support channels(get contacted of a support message)

#commands with embed: help, mail, support, about, update(will soon)

@client.event
async def on_message(message):

  
  pass_yes2 = 0

  pass_yes = 0

  sleep_time = "no"
  
  user = message.author

  time = message.created_at

  time99 = time.astimezone(timezone(time_location)).strftime("%m/%d/%Y, %H:%M:%S")

  for x in user_timezone:

    time_location99 = user_timezone[x]

    if x == message.author.id:

      time55 = time.astimezone(timezone(time_location99)).strftime("%m %d %Y %H %M %S")

      sleep_time = "yes"

  for z in birthday_functions:

    for x in user_timezone:

      time_location99 = user_timezone[x]

      dates = birthday_functions[z]

      guess = time.astimezone(timezone(time_location99)).strftime("%m %d %Y %H %M %S")

      #didn't know which birthday certain users might have...

      guess_1 = int(guess.split(" ")[0])

      guess_2 = int(guess.split(" ")[1])

      if z == message.author.id and x == message.author.id:

        user_month = int(dates.split(" ")[0])

        user_month2 = int(dates.split(" ")[1])

        if user_month == guess_1 and user_month2 == guess_2:

          if (message.author.dm_channel is None):

            await message.author.create_dm()

          await message.author.dm_channel.send("Happy Birthday, hope it's a good one, sorry for the random DM though....")

  #Birthday and sleep stuff ^ (deleted the old code in: https://repl.it/@JDJGInc_Offical/JDJGBotSupreme#unused_stuff/unused_code.py)


  #CHANNEL LINKER COMMANDS
  if not message.author.bot: #Channel Link Message Repeater
    if not message.content.startswith(discordprefix):
      ret_str = str(user) +": "+GlobalLinker.FilterMessage(message)
      await RankSystem.UpdateScore(message) #For the rank system
      for gChan in DatabaseConfig.db.g_link_testing.find():
        if message.channel.id == gChan['chan_id']:
          for gChan in DatabaseConfig.db.g_link_testing.find():
            if message.guild.id != gChan['ser_id']:
              embedVar = discord.Embed(title=message.guild.name)
              embedVar.add_field(name=str(message.author),value=str(GlobalLinker.FilterMessage(message)),inline=True)
              await client.get_channel(gChan['chan_id']).send(embed=embedVar)
      for chanId in DatabaseControl.GetLinkedChannelsList(message.channel.id):
        await client.get_channel(chanId).send(ret_str)
        if len(message.attachments) !=0: #attachment Code
          picture = str(message.attachments[0].url)
          await client.get_channel(chanId).send(picture)
  if message.content.startswith(discordprefix+"GetChannelId") and not message.author.bot:
    await message.channel.send(message.channel.id)
    return
  if message.content.startswith(discordprefix+"link_this") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    DatabaseControl.AddChannelLink(message.channel.id,n1)
    await message.channel.send("This channel was linked to "+ str(client.get_channel(n1)))
    return   
  if message.content.startswith(discordprefix+"link_channel") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    n2 = str(message.content.split(" ")[2])
    n2 = DatabaseControl.to_ChannelId(n2)
    await message.channel.send(DatabaseControl.AddChannelLink(n1,n2))
    return
  if message.content.startswith(discordprefix+"delete_link") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    n2 = str(message.content.split(" ")[2])
    n2 = DatabaseControl.to_ChannelId(n2)
    await message.channel.send(DatabaseControl.DeleteChannelLink_ChanNum(n1,n2))
    return
  if message.content.startswith(discordprefix+"GetLinked") and not message.author.bot:
    n1 = str(message.content.split(" ")[1])
    n1 = DatabaseControl.to_ChannelId(n1)
    await message.channel.send(DatabaseControl.GetLinkedChannels(client,n1))
    return
#RANK SYSTEM COMMANDS
  if message.content.startswith(discordprefix+"rank") and not message.author.bot:
    await RankSystem.GetStatus(message)
    #await message.channel.send(RankSystem.CheckIfExisting(user))
    return
  if message.content.startswith(discordprefix+"dev_rank") and not message.author.bot:
    await RankSystem.DevGetStatus(client,message)
    #await message.channel.send(RankSystem.CheckIfExisting(user))
    return
  if message.content.startswith(discordprefix+"get_user") and not message.author.bot:
    await message.channel.send(RankSystem.GetUserByName(client,message))
    return
  if message.content.startswith(discordprefix+"lead") and not message.author.bot:
    await RankSystem.GetTop10(client,message)
    return
  if message.content.startswith(discordprefix+"toggle") and not message.author.bot:
    args = message.content.split(" ")[1]
    if args == "level_msg":
      await message.channel.send(RankSystem.ToggleLevelUpMsg(message))
    return
#GLOBAL LINKER
  if message.content.startswith(discordprefix+"global") and not message.author.bot:
    await message.channel.send(GlobalLinker.AddGlobalLink(client,message))
    return
#UPDATE NOTIFY
  if message.content.startswith(discordprefix+"update") and message.author.id in admins and not message.author.bot:
    await UpdateNotify.UpdateNote(message,client)
    
    return
#OTHER STUFF
  if message.content.startswith(discordprefix+"help") and not message.author.bot:
    await help(message)
    return

  if message.content.startswith(discordprefix+"rm") and not message.author.bot:
    await message.channel.send(random_message())
    return

  if message.content.startswith(discordprefix+"guild_get") and not message.author.bot:

    current_guild = message.guild
    

    #Just add more features I guess? - like being able to disable the owner id like the Mee6 serverinfo command?

    #Example here: https://discord.com/channels/736422329399246990/736424228026450021/739518057768026147

    #https://discordpy.readthedocs.io/en/latest/api.html#guild

    await message.channel.send(current_guild)

    return

  #if message.content.startswith(discordprefix+"os") and not message.author.bot:

    #version_info = "0.0.1"

    #for now anyway

    #Port this program to discord.py soon...

    #operating_system = "DiscordOS"

    #await client.chanel.send("\n Booting",operating_system)

    #on = True

    #logon = str(author.name)

    #os_commands = [
      #"cls",
      #"clear",
      #"exit",
      #"break",
      #"log off",
      #"list commands",
      #"random number",
      #"ver",
      #"version",
      #"time",
      #"username",
      #"date",
      #"datetime",
      #"help",
      #"type",

    #]

  

    #command_subsystem = [
      ##"r", #Read - Default value. Opens a file for reading, error if the file does not exist
      #"a", #Append - Opens a file for appending, creates the file if it does not exist
      #"w", #Write - Opens a file for writing, creates the file if it does not exist
      #"x", # Create - Creates the specified file, returns an error if the file exist
      #"t", #Text - Default value. Text mode
      #"b", # Binary - Binary mode (e.g. images)

    #]

    #https://www.w3schools.com/python/ref_func_open.asp

    #while on == True:

      #display_name = logon+"@"+operating_system+":"

      #command_console = input(display_name)

      #print("\n")

      #if command_console == "cls" or command_console == "clear":

        #clear_code.clear()

      #if command_console == "exit" or command_console == "break" or command_console == "log off":

        #print("\n Logging out of console")

        #break
    
      #if command_console == "list commands":

        #command_amount = len(os_commands)

        #command_count = 0

        #while command_count < command_amount:

          #print(os_commands[command_count])

          #command_count = command_count+1

      #if command_console == "random number":

        #number_one = input("Starting number:")

        #number_two = input("\n Ending number:")

        #incomplete code(JDJG Bot has it anyway)

        #good_or_bad=type(number_one)

        #https://note.nkmk.me/en/python-check-int-float/#:~:text=float%20has%20is_integer()%20method,an%20integer%2C%20and%20False%20otherwise.&text=For%20example%2C%20a%20function%20that,function%20returns%20False%20for%20str%20.

      #if good_or_bad == "str":

        #print("Not good")

      #if command_console == "time":

        #time_info = (datetime.datetime.now(timezone(time_location)).strftime("%H:%M:%S"))

        #print(time_info)

      #if command_console == "date":

        #value_search = "%m/%d/%Y"

        #time_info = (datetime.datetime.now(timezone(time_location)).strftime(value_search))

        #print(time_info)

    
      #if command_console == "datetime":

        #value_search = "%m/%d/%Y %H:%M:%S"

        #time_info = (datetime.datetime.now(timezone(time_location)).strftime(value_search))

        #print(time_info)

    
    #if command_console == "ver" or command_console == "version":

      #print(version_info)

    #if command_console == "username":

      #usage = logon

     #print(usage)

    #if command_console.startswith("type"):

      #file_info = open(file_name,flag_info)

      #rest_command = [len(command_console+"type")]

      #total_number = len(rest_command)

      #if rest_command == "help":

        #total_count = 0

        #number_amount=len(command_subsystem)


        #while total_count < number_amount:

          #print(command__subsystem[total_count])

          #total_count = total_count + 1

      #if total_number == 1 and not rest_command == "help":

        #print("\n That's not enough information")

        

  #if not command_console in os_commands or not command_console.startswith(command_console):

    #print("\n not A valid command")

  #print("\n")

  #now ported to https://repl.it/@JDJGInc_Offical/JDJGBotSupreme#JDJG_os.py

  #og code at https://repl.it/@JDJGInc_Offical/Python-os-Console#main.py (I will write the rest here....)



  if message.content.startswith(discordprefix+"ad") and not message.author.bot:
    await message.channel.send(ad())
    return

  if message.content.startswith(discordprefix+"leave guild") and message.author.id in admins and not message.author.bot:

    guild_info = client.get_guild(int(message.content.split(" ")[2]))

    await guild_info.leave()

    return

  if message.content.startswith(discordprefix+"status") and message.author.id in admins and not message.author.bot:
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(message.content[len(discordprefix+"status "):]))
    return


  if message.content.startswith(discordprefix+"rn") and not message.author.bot:
    try:
      number_one = int(message.content.split(" ")[1])
      number_two =  int(message.content.split(" ")[2])
    except:
      await message.channel.send("That is not a number! I shall default to: 1-100")
      number_one = 0
      number_two = 100


    if number_one > number_two:
      await message.channel.send("Smaller number first")
    
    random_number = random.randint(number_one, number_two)
  
    random_number_message = "A random number from %d to %d is : %d." % (number_one, number_two, random_number)
    await message.channel.send(random_number_message)
    return

  if message.content.startswith(discordprefix+"about") and not message.author.bot:
    embed_message = discord.Embed(title="About(commands):", description=all_commands)

    user_send2 = message.author
    if (user_send2.dm_channel is None):
      await user_send2.create_dm()

    await user_send2.send(embed=embed_message)

    embed_message2 = discord.Embed(title="About(credits):", description=credits)
    await user_send2.send(embed=embed_message2)

    helpmsg2 = "prefix is JDBot*, More commands are:\n "+all_commands2

    embed_message = discord.Embed(title="About(commands):",description=helpmsg2)

    await message.author.dm_channel.send(embed=embed_message)

    embed_message = discord.Embed(title="About(legal):",description=legal_info)

    await message.author.dm_channel.send(embed=embed_message)

    return

  if message.content.startswith(discordprefix+"time") and not message.author.bot:
    await message.channel.send(datetime.datetime.now(timezone(time_location)).strftime("%m/%d/%Y, %H:%M:%S"))
    return
    
  if message.content.startswith(discordprefix+"say") and not message.author.bot:
    current_message = message.content[len(discordprefix+"say"):]
    if current_message == "":
      return

    await message.delete()
    await message.channel.send(current_message)
    return

  if message.content.startswith(discordprefix+"support DM ") and not message.author.bot:
    support_msg = message.content[len(discordprefix+"support DM "):]
    for adID in admins:
      try:
        admin_user = client.get_user(adID)

        if (admin_user.dm_channel is None):
          await admin_user.create_dm()

        support_msg2 = "Message from <@%d> (%d) : %s" % (message.author.id, message.author.id, support_msg)
        who_sent = str(message.author)
        embed_message = discord.Embed(title=who_sent, description=support_msg2)

        await admin_user.send(embed=embed_message)
      except:
        print("Error processesing user:", adID)
      
      return

  if message.content.startswith(discordprefix+"backup_emojis") and not message.author.bot:

    guild_search = client.get_guild(736422329399246990)

    backup_emoji1= 748753645138608239

    guild_1 = client.get_guild(backup_emoji1)

    backup_emoji2 = 748753770476732499

    guild_2 = client.get_guild(backup_emoji2)

    guild_emoji_fetch = guild_search.emojis
    i = -1
    for obj in guild_emoji_fetch:
      
      response = requests.get(str(obj.url))
      img = response.content
      #resp = urllib3.PoolManager().request('GET',str(obj.url))
     # image99 = BeautifulSoup(resp.data)
    
      if(i<50):
        if str(obj.animated) == "True":
          await guild_1.create_custom_emoji(name = str(obj.name),image=img)
        if str(obj.animated) == "False":
          i = i-1
      if(i>=50):
        if str(obj.animated) == "False":
          await guild_2.create_custom_emoji(name = str(obj.name),image=img)
        if str(obj.animated) == "True":
          i =  i-1


    return
  


  if message.content.startswith(discordprefix+"log off") and message.author.id in admins and not message.author.bot:
    await message.channel.send("Shutting off")
    await client.logout()
    return
  

  if message.content.startswith(discordprefix+"update ") and message.author.id in admins and not message.author.bot:
    update_msg = message.content[len(discordprefix+"update "):]
    update_msg_embed = discord.Embed(title="New Update:", description=update_msg)
    for updateID in get_updates:
      get_updates_epic = client.get_user(updateID)

      if (get_updates_epic.dm_channel is None):
        await get_updates_epic.create_dm()
      await get_updates_epic.send(embed=update_msg_embed)
    return


  if message.content.startswith(discordprefix+"support channel") and not message.author.bot:
    support_msg = message.content[len(discordprefix+"support channel"):]
    normal_username = str(message.author)

    user_info = "Message from\n ("+str(message.author.id)+")\n"+normal_username+":"
    embed_message = discord.Embed(title=user_info, description=support_msg)

    for cid in send_channel:
      await client.get_channel(cid).send(embed=embed_message)

    return


  if message.content.startswith(discordprefix+"coin") and not message.author.bot:
    guess_dice = message.content[len(discordprefix+"coin "):]
    value = random.choice([True,False])

    win = False
    if guess_dice.lower().startswith("h") and value:
      win = True
    elif guess_dice.lower().startswith("t") and not value:
      win = True

    elif guess_dice.lower().startswith("h") and not value:
      win = False
    elif guess_dice.lower().startswith("t") and value:
      win = False

    else:
      await message.channel.send("Was that a choice?")
      return
    
    the_results = "The coin flipped: "+("heads" if value else "tails")+", and you had: "+guess_dice
    
    if win:
      the_results += ". You win!"
      embed_message = discord.Embed(title="coin flip", description=the_results)
      await message.channel.send(embed=embed_message)
      await message.channel.send(":partying_face:")
    else:
      the_results += ". You lose :("
      embed_message = discord.Embed(title="coin flip", description=the_results)
      await message.channel.send(embed=embed_message)
      await message.channel.send(":frowning:")
    return

  if message.content.startswith(discordprefix+"webhook update") and not message.author.bot and message.author.id in jdjg_id:

    update_color = 35056

    await message.delete()

    url_grab = str(os.environ['webhook1'])

    url_grab2 = str(os.environ['webhook99'])

    message_info = message.content[len(discordprefix+"webhook update"):]

    url_grab_ultra = [url_grab,url_grab2]

    webhook = discord_webhook.DiscordWebhook(url=url_grab_ultra)

    embed = discord_webhook.DiscordEmbed(title='Update',color=update_color)

    speacil_icon = 'https://media.discordapp.net/attachments/491419169842135059/732821876488798249/fisheye.png'

    embed.add_embed_field(name='Update Info:', value=message_info)

    embed.set_timestamp()

    embed.set_author(name="JDJG's Update",icon_url=speacil_icon)

    embed.set_footer(text="JDJG's Updates")

    webhook.add_embed(embed)

    webhook.execute()

    return

  if message.content.startswith(discordprefix+"insult") and not message.author.bot:

    await message.channel.send("Preparing insult......")

    await message.channel.send("Please wait...(also why would you want to insult yourself?)")

    insult_request = insult_response()

    await message.channel.send(insult_request)

    return
  
  if message.content.startswith(discordprefix+"tweet") and not message.author.bot:
    tweet_username = message.content.split(" ")[1]

    value_here = int(message.content.split(" ")[2])
    
  

    if value_here > 20:
      value_here = 20
      await message.channel.send("are you insane? Trust me I can DM a lot of tweets... swapping to 20")



    consumer_key= os.environ['tweet_key']

    consumer_secret=os.environ['tweet_secret']

    access_token=os.environ['tweet_access']

    access_token_secret=os.environ['tweet_token']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=tweet_username,count=value_here)

    for info in tweets:
      tweet_stuff = info.text

      tweet_username99 = "Loads of Tweets from: @"+tweet_username+" with "+str(value_here)+" messages from them."

      embed_info = discord.Embed(title=tweet_username99, description=tweet_stuff)

      if (message.author.dm_channel is None):
        await message.author.create_dm()
      await message.author.dm_channel.send(embed=embed_info)



    return


  if message.content.startswith(discordprefix+"webhook") and not message.author.bot:

    webhook_url = message.content.split(" ")[1]

    message_info = message.content.split(" ")[2]

    author_info = str(message.author)+"'s Message"
    

    await message.delete()

    update_color = 35056

    webhook = discord_webhook.DiscordWebhook(url=webhook_url)

    embed = discord_webhook.DiscordEmbed(title=author_info,color=update_color)


    embed.add_embed_field(name=author_info, value=message_info)

    embed.set_timestamp()

    webhook.add_embed(embed)
    
    webhook.execute()

    return

  if message.content.startswith(discordprefix+"hey") and not message.author.bot and user.guild_permissions.administrator == True:

    await message.channel.send("Hey you have a lot of abilities...")

    await message.channel.send("Accessing every speacil command for you.. - this basically unlocks every command for you")

    try:

      command = message.content.split(" ")[1]

      function_here = message.content.split(" ")[2]

    except:

      function_here = ""

      command = ""

    await message.delete()

    if command == "vc" and not function_here == "":

      await message.channel.send("Joining a voice channel(requires an id)")


      await message.guild.create_voice_channel(function_here)

      return

    if command == "mc" and not function_here == "":

      await message.channel.send("Makes a channel in your server with the name you want...")

      

      channel = await message.guild.create_text_channel(function_here)

      return

    if not command == "vc" or not command == "mc" and not function_here == function_here:

      await message.channel.send("Not a valid command...")

    return

  if message.content.startswith(discordprefix+"apply bloopers") and not message.author.bot:

    apply_message = message.content[len(discordprefix+"apply bloopers"):]

    await message.delete()

    for x in application_user:

      apply_user = client.get_user(x)

      if (apply_user.dm_channel is None):
        await apply_user.create_dm()

      author_id =str(message.author.id)

      who_sent = "Application from: \n"+str(message.author)+"\n with the id of "+author_id+"\n:"

      embed_message = discord.Embed(title=who_sent, description=apply_message)

      await apply_user.send(embed=embed_message)

    
    return
      
      
  if message.content.startswith(discordprefix+"radical") and not message.author.bot:

    try:

      num_int = int(num)

      root_int = int(root)

    except:

      num = int(1)

      root_int = int(1)
      
      await message.channel.send("Why would you use something that isn't a number, try again")



    root_answer = num_int**(1/root_int)

    final_information = "result of "+str(num)+" radical "+str(root_int)+" is: "+str(root_answer)

    await message.channel.send(final_information)

    return


  if message.content.startswith(discordprefix+"power") and not message.author.bot:

    num = message.content.split(" ")[1]

    root = message.content.split(" ")[2]

    try:

      num_int = int(num)

      root_int = int(root)

    except:

      num = int(1)

      root_int = int(1)

      await message.channel.send("Why would you use something that isn't a number, try again")

    ans = (num_int**root_int)

    final_information = "result of "+str(num)+" to the power of "+str(root_int)+" is: "+str(ans)

    await message.channel.send(final_information) 

    return

  if message.content.startswith(discordprefix+"works") and not message.author.bot:

    number_here = random.randint(1,100)

    name_1 = message.content.split(" ")[1]

    name_2 = message.content.split(" ")[2] 

    values = name_1+" Works with "+name_2+"at a rate of "+str(number_here)+"%"

    await message.channel.send(values)

    return

  if message.content.startswith(discordprefix+"wc") and not message.author.bot and user.guild_permissions.manage_webhooks == True:

    webhook_name =  webhook_url = message.content.split(" ")[1]

    content_message = message.content.split(" ")[2]

    await message.delete()
       
    await message.channel.send("Making Webhooks with your manage permissions(safety reasons)")

    await message.channel.create_webhook(name=webhook_name,reason=content_message)

    await message.channel.send("You could have made your own(orginally it would have DMed this value to you but that didn't(it can't DM the url yet.) edit the webhook in this channel to get an image")

    return

  if message.guild is None and not message.author.bot:

    user_info = "User: "+str(message.author)+"\n("+str(message.author.id)+")\n:"
    embed_message = discord.Embed(title=user_info, description=message.content)
 
    await client.get_channel(738912143679946783).send(embed=embed_message)
    
    return
  
  for channel_x in from_to_channel:
    if message.channel.id == channel_x:

      channel_id = from_to_channel[channel_x]

      await client.get_channel(channel_id).send(message.content)
      #break


  if message.content.startswith(discordprefix+"color") and not message.author.bot:

    try:
      convert_from = message.content.split(" ")[1].lower()
      convert_to = message.content.split(" ")[2].lower()
      convert_value = message.content.split(" ")[3].lower()
    except:
      await message.channel.send("Not enough arguments")
      return


    if convert_from == "rgb":
      if convert_value.startswith("("):
        convert_value = convert_value[1:-1]
      triple = convert_value.split(",")
      for i in range(3):
        triple[i] = int(triple[i])
        
    elif convert_from == "hex":
      if convert_value.startswith("#"):
        convert_value = convert_value[1:]
      triple = [convert_value[0:2],convert_value[2:4],convert_value[4:]] #OBOE?
      for i in range(3):
        triple[i] = int(triple[i],16)

    elif convert_from == "decimal":
      triple = discord.Colour(int(convert_value)).to_rgb()

    else:
      await message.channel.send("unknown format: '%s'" % convert_from)
      return

    if convert_to == "rgb":
      converted_value = "(%d,%d,%d)" % tuple(triple)

    elif convert_to == "hex":
      converted_value = "#%02X%02X%02X" % tuple(triple)

    elif convert_to == "decimal":
      c = discord.Colour.from_rgb(*triple)
      converted_value = str(c.value)

    else:
      await message.channel.send("unknown format: '%s'" % convert_to)
      return

    await message.channel.send("Converted from: "+convert_from+". To: "+convert_to+". "+converted_value)

    return
  
  if message.content.startswith(discordprefix+"emote ") and not message.author.bot:

    emote_wanted = message.content[len(discordprefix+"emote "):]

    #returned_info = client.emojis.find(emote_wanted)
    
    emojiNearest = sorted(client.emojis, key=lambda x: SequenceMatcher(None, x.name, emote_wanted).ratio())[-1]

    #await message.channel.send(returned_info)
    await message.channel.send(emojiNearest)

    return

  if message.content.startswith(discordprefix+"servers") and message.author.id in admins and not message.author.bot:
    send_list = [""]
    guild_list = ["%d %s %d %s" % (len(g.members), g.name, g.id, (g.system_channel or g.text_channels[0]).mention) for g in client.guilds]

    for i in guild_list:
      if len(send_list[-1] + i) < 1000:
        send_list[-1] += i + "\n"
      else:
        send_list += [i + "\n"]
    
    if (message.author.dm_channel is None):
      await message.author.create_dm()

    await message.author.dm_channel.send("\n Servers:")

    for i in send_list:

      await message.author.dm_channel.send(i)

      
      
    return

  if message.content.startswith(discordprefix+"message time") and not message.author.bot:

    await message.channel.send(time99)

    return

  if message.content.startswith(discordprefix+"mail") and not message.author.bot:
    try:
      user = message.mentions[0]
      mail_msg = message.content.split(" ",2)[-1]
    except:
      try:
        user = client.get_user(int(message.content.split(" ",2)[1]))
        mail_msg = message.content.split(" ",2)[-1]
        if user is None:
          pass
          #user does not exist
      except:
        # was the userID not an int?
        pass
    
    await message.channel.send("Sending mail....")
    #i just want a way to seperate the id or possible mention and see if the bot can decide between both ones
    #will be able to select which user to go to id or mention like JDBot*mail <user id or mention> <message> - user command
    author_id = str(message.author.id)
    who_sent = "Mail from: \n"+str(message.author)+"\n with the id of "+author_id+"\n:"
    mail_msg2 = message.content.split(" ",2)[-1]
    embed_message = discord.Embed(title=who_sent, description=mail_msg2)

    if (user.dm_channel is None):
      await user.create_dm()
    await user.send(embed=embed_message)
    return

  if message.content.lower().startswith('fooz'):
    try:
      evalStr = eval(message.content[4:])
      if evalStr is None or len(str(evalStr)) == 0:
        await message.channel.send("Successful.")
      else:
        await message.channel.send(str(evalStr))
    except Exception as e:
      pass
    return

  for banned_word in banned_words:
    if banned_word in message.content:
      await message.delete()
      await message.channel.send(determine())

  if message.content.startswith(discordprefix+"link") and not message.author.bot:
    channel_one = int(message.content.split(" ")[1])
    channel_two = int(message.content.split(" ")[2])
    from_to_channel[channel_one] = channel_two

    try:
      channel_msg = message.content.split(" ", 3)[3]  # everything after the 3rd space is all one string
    except:
      channel_msg = ""

    if channel_msg == "":
      await message.channel.send("Linker set up")
    else:
      await message.channel.send("Message setup message for the link is: "+channel_msg)
    return

  if message.content.startswith(discordprefix+"clear") or message.content.startswith(discordprefix+"purge"):
    await message.delete()
    user = message.author

    if user.guild_permissions.manage_messages:
      try:
        amount = int(message.content.split(" ")[1])
      except:
        #arguement not an integer
        amount = 0
        pass

      if amount > 100:
        await message.channel.send("Too high set to 100(Just decided that randomly)")
        amount = 100                     

      await message.channel.purge(limit = amount)
    return

  #case for if all other commands did not work

  if message.content.startswith(discordprefix+"compliment") and not message.author.bot:

    await message.channel.send("Sending compliment.....")

    await message.channel.send(":D Alright let's send this data over...")

    compliment_response = yes_49()

    result_here = ":mariodance:"+compliment_response

    await message.channel.send(result_here)

    return

  if message.content.startswith(discordprefix+"Arithmetic") and not message.author.bot:

    og_number = int(message.content.split(" ")[1])

    per_times = int(message.content.split(" ")[2])

    number_times = int(message.content.split(" ")[3])

    number_result = og_number+per_times*(number_times-1)
    
    await message.channel.send("Result of: \n"+str(og_number)+" + "+str(per_times)+" * ("+str(number_times)+" - 1) = "+str(number_result))
    return

  if (message.content.startswith(discordprefix+"user-find") or message.content.startswith(discordprefix+"user_find"))and not message.author.bot:

    rankID = int(message.content.split(" ")[1])

    #seperates id

    user99 = client.get_user(rankID)

    #gets the user

    user_name = user99.name

    #gets name

    user_id = str(user99.id)
    
    #gets id
    
    discriminator99 = user99.discriminator

    #gets ending bit like: #3439

    avatar99 = user99.avatar

    #avatar hash

    bot_decide = user99.bot

    #if it's a bot(bool expression)

    if bot_decide == True:

      await message.channel.send("That's a bot")

    if bot_decide==False:

      await message.channel.send("Yes, it's a user")


      full_name = str(user_name)+"#"+str(discriminator99)

      #makes it say the full name

      await message.channel.send(full_name)

      #prints the username

      hash_check = "The avatar hash of that user is: "+str(avatar99)

      #hash of the avatar
      
      await message.channel.send(hash_check)

      await message.channel.send(user_id)

    return

  if message.content.startswith(discordprefix+"invite") and not message.author.bot:

    await message.channel.send("Testing link: https://discordapp.com/oauth2/authorize?client_id=702243652960780350&scope=bot&permissions=8")

    await message.channel.send("normal invite: https://discordapp.com/oauth2/authorize?client_id=702238592725942374&scope=bot&permissions=8")

    return


  if message.content.startswith(discordprefix) and not message.author.bot:
    support_msg = "user tried to excute command(doesn't exist): "+str(message.content)
    normal_username = str(message.author)
    user_info = "%s (%d):" % (normal_username, message.author.id)
    embed_message = discord.Embed(title=user_info, description=support_msg)
    await client.get_channel(738912143679946783).send(embed=embed_message)

    if (message.author.dm_channel is None):
      await message.author.create_dm()
    
    await message.author.dm_channel.send(support_msg)

    return
  if message.content.startswith(discordprefix+"suspend") and message.author.id in admins and not message.author.bot:
    await message.channel.send("testing bot")
    return

#RENDEV'S CODE...NO TOUCH
@client.event
async def on_message_delete(message):
  if message.author.bot:
   return
  await message.channel.send("Message was Deleted")
  if(message.content.startswith("deleteMe")):
   await client.delete_message(message)
@client.event
async def on_message_edit(before,after):
  print("*")
  message = await find_message(after,before)
  embedVar = discord.Embed(title=after.guild.name)
  embedVar.add_field(name=str(after.author),value=str(GlobalLinker.FilterMessage(after)),inline=True)
  await message.edit(embed=embedVar)
async def find_message(messageC,messageB):
  i=0
  print("Hello")
  for chan in DatabaseConfig.db.g_link_testing.find():
    i=i+1
    print(i)
    channel = client.get_channel(chan['chan_id'])
    print("Chan_id: "+ str(channel.id) + "  :  "+str(messageB.channel.id) )
    if channel.id != messageB.channel.id:
      async for mess in channel.history():
        try:
          embed_content_in_dict = mess.embeds[0].to_dict()
          print(embed_content_in_dict['fields'][0]['value'])
          if messageB.content==embed_content_in_dict['fields'][0]['value']:
            print("HELLO"+embed_content_in_dict['fields'][0]['name'])
            if embed_content_in_dict['fields'][0]['name'] == messageB.author:
          #if mess.created_at.minute == messageB.created_at.minute:
              return mess
        except:
          banana=0
        


    


from_to_channel = {}

banned_words = [
  'faggot',
  'retard',
  'pussy',
  'bastard',
  'nigga',

] 

banned_response = [ 
  'Do you really need to curse?',
  'the f word and s words work but really using racial slurs, why?(still not the best idea)',
  'Ugh....',
]

response_banned = []

def determine():
  global response_banned
  if len(response_banned) == 0:
    response_banned = banned_response
    random.shuffle(response_banned)
  return "\n"+response_banned.pop()

response_answers_yes = [
  "You are nice to me :D, Thank you :D",
  "Hope your life is good :D",
  "People can trust you...",
  "Thank You for your help.",
  "Loading epic dance for you....",
  ":mariodance: is how you make me....",
]

response_yes = []

def yes_49():

  global response_yes

  if len(response_yes) == 0:

    response_yes = response_answers_yes

    random.shuffle(response_yes)

  return "\n"+response_yes.pop()

#for banned words a.k.a slurs and such (don't open if you aren't a programmer - or easily offended)

insult_doom94 = [
  "Look I can insult better than some people, but at least I don't willing send it to people unlike you, who wants it",
  "Geez, You could better stuff with your time",
  "Sorry you were too slow for a request... but SERIOUSLY WHY DO YOU NEED TO INSULT YOURSELF?",
  "Sorry for not wanting to insult you :rolling_eyes: loading... yoshi banner hammer...",
  "You are so bad you deserve to get banned(JDJG doesn't approve of this message",
  "Some people get custom tailored stuff, now you don't because you Didn't ask. MWHAAA!",
  "Loading yoshi ban hammer.... :yoshihammer:",
  ".______________________. Geez you made me unable to comment about you, you're that evil...",
  "Some people like being evil, but why? Being good is better...(trust me)",
  "We ran out of insults for you, because frankly we don't care..",


]

insultdoom96 = []

sleep_response99 = []

def sleep():
  global sleep_response99

  if len(sleep_response99) == 0:

    sleep_response99 = sleep_response

    random.shuffle(sleep_response99)

  return "\n"+sleep_response99.pop()


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

def insult_response():
  global insultdoom96
  if len(insultdoom96) == 0:
  
    insultdoom96 = insult_doom94
    random.shuffle(insultdoom96)

  return "\n"+insultdoom96.pop()


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

credits = """Programmer - Nomic Zorua#6488 
Programmer - JDJG Inc. Official#3493 
Programmer - Shadi#7879(for ranks and such+and some cool new features)- bit of help from him(thank You :D) and korikasyn#0001, as well as RenDev
#2616.
Invite link is https://discordapp.com/oauth2/authorize?client_id=702238592725942374&scope=bot&permissions=8
coded in Python
Open source on https://repl.it/@JDJGInc_Offical/JDJGBotSupreme (check it out) - it's open source so you can see how it works.. Want to help? DM JDJG Inc. Official#3439 and join the support server
We promise it follows(if our bot gets hacked, we will immediately change the token and tell us ourselves, or just join our support server(this makes it easier), some features will be moved to databases, one it makes it possible to store and keeps data private. If you ask what data we have on you, that might take a bit, but our token is stored safetly, as long as none of the project managers leak the info or repl.it isn't hacked(or anything else). the Bot is fine.
Github: https://github.com/JDJGInc/JDJGBotSupreme """

legal_info = """Documents:

https://discord.com/developers/docs/legal

https://discord.com/developers/docs/policy

Api Reference:

https://discord.com/developers/docs/reference

Last info:

https://discord.com/developers/docs/store-distribution-agreement

The support server(Discord's):

https://discord.com/invite/discord-developers(discord's developer server(for people like me and Nomic..))

Please contact us if you feel in anyway we might not be following these rules....(this is so we both can be sure we're fine)

We also tell you all the functions it does.. No we don't sell this information, if you do plan to donate, just ask. Though JDJG doesn't really need it..

Alt bot invite:

https://discordapp.com/oauth2/authorize?client_id=702243652960780350&scope=bot&permissions=8

24/7 Hosting by LinuxTerm#8880 (thank you :D)

https://discord.gg/sHUQCch - for another support center"""

sleep_response = [
  "You should sleep, now.... if you do then sleep well",
  "trust me sleep is imporant",
  "Being tired sucks(I felt it many times before)",
  "Sure life is limited but seriously it's actually not bad...",
  "When it's too late for you, you know your commands are disabled, why? well it's so you don't keep on staying up...",
  "Commands are returned after you wake up(it's two way)",
  "Commands were disabled for you right now",
  "Sleep and I will see you Tommorow",
  "Mods have been notified",
  "Why won't you sleep?",
  "go to sleep dude...",
  ]



ad_some = []

def ad():
  global ad_some
  if len(ad_some) == 0:
    ad_some = ad_all
    random.shuffle(ad_some)
  return "\n"+ad_some.pop()


token_grab = os.environ['Discordtoken']

client.run(token_grab) 


#token_grab uses Discordtoken - for 24/7 bot and Discordtoken2 for testing purposes

#(nightly bot - current open source code)
