get_updates = [
  168422909482762240,
  660295633223024671,
  717822288375971900,
  357006546674253826 #rendev
]

if message.content.startswith(discordprefix+"update") and message.author.id in admins and not message.author.bot:
    update_msg = message.content[len(discordprefix+"update"):]
    update_msg_embed = discord.Embed(title="New Update:", description=update_msg)
    for updateID in get_updates:
      get_updates_epic = client.get_user(updateID)

      if (get_updates_epic.dm_channel is None):
        await get_updates_epic.create_dm()
      await get_updates_epic.send(embed=update_msg_embed)
    return