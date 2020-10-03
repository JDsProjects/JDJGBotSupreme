user_timezone = {
  168422909482762240:"America/New_York",
  717822288375971900:"America/New_York",
}

user_waketime = {
  168422909482762240:"6 0 0",
  717822288375971900:"6 0 0",

}

user_sleeptime = {
  168422909482762240:"21 0 0",
  717822288375971900:"21 0 0",

}

birthday_functions = {
  269904594526666754:"7 19",
  168422909482762240:"7 3",
}

pass_yes2 = 0

pass_yes = 0

sleep_time = "no"

#used with as well https://repl.it/@JDJGInc_Offical/JDJGBotSupreme#unused_stuff/unused_code.py

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

if sleep_time == "yes" and not message.author.id in id_override:

    for x in user_sleeptime:

      time_info = user_sleeptime[x]

      if x == message.author.id:   

        pass_yes2 = 1

        user_sleeptime1 = int(time_info.split(" ")[0])

        user_sleeptime2 = int(time_info.split(" ")[1])

        user_sleeptime99 = int(time_info.split(" ")[2])

        hour = int(time55.split(" ")[3])

        minute = int(time55.split(" ")[4])

        second = int(time55.split(" ")[5])

      for y in user_waketime:

       if y == message.author.id:

          pass_yes = 1
        
          time_end = user_waketime[y]

          user_sleeptime4 = int(time_end.split(" ")[0])

          user_sleeptime5 = int(time_end.split(" ")[1])

          user_sleeptime6 = int(time_end.split(" ")[2])

        if pass_yes == 1 and pass_yes2 == 1:

          if hour > user_sleeptime1 - 1   or hour < user_sleeptime4 -1:

            if minute > user_sleeptime2 -1 or minute < user_sleeptime5 - 1:

              if second -1 > user_sleeptime99 or second < user_sleeptime6 -1:
      
                if (message.author.dm_channel is None):

                  await message.author.create_dm()

                message_used = sleep()

                if message_used == "":

                  message_used = "sleep dude...."

                await user.dm_channel.send(message_used)

                return