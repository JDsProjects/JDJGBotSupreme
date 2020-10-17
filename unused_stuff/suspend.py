if message.content.startswith(discordprefix+"suspend") and message.author.id in admins and not message.author.bot:
    await message.channel.send("suspending bot")
    
    await client.logout()

    while True:

      command_usage=input("\n Command:")

      if command_usage.lower() == "log off":

        print("\n turning off")

        break

      if command_usage.lower() == "log on":

        call_function()

        break

    return

def call_function():

  client.run(token_grab)

#code doesn't work.