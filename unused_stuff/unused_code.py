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