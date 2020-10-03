import discord
def sendDM(message, targetUser):
  embed = discord.Embed(title = "Incoming Message!")
  embed.add_field(name =  str(message.author),value = message)
  if (targetUser.dm_channel is None):
    await targetUser.create_dm()
  await targetUser.send(embed=embed)