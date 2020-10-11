from_to_channel = {}

from_to_channel={
  488487653608521768:556242984241201167,
}

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

for channel_x in from_to_channel:
    if message.channel.id == channel_x:

      channel_id = from_to_channel[channel_x]

      await client.get_channel(channel_id).send(message.content)
      #break
