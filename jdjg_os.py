import ClientConfig
import random
import discord
async def os(message):
  client = ClientConfig.client
  times_ran = 0
  version_info = "0.0.1"
  operating_system = "DiscordOS"
  await message.channel.send(f"Booting {operating_system}")
  #on = True
  display_name = (f"{message.author.name}@{operating_system}")
  def check(m):
    return m.author.id == client.os_user
  info = await client.wait_for("message",check=check)
  if info.content.startswith("exit") or info.content.startswith("log off"):
    client.os_user = "None"

  if info.content.startswith("ver") or info.content.startswith("version"):

    await info.channel.send(f" Version: {version_info}")