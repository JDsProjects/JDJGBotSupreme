import re
import aiohttp
import ClientConfig
import discord
import emojis
import random
client = ClientConfig.client
async def get(message):
  images = []
  full_emojis=re.findall(r':\w*:\d*',message.content)
  custom_emoji_ids = [(e.split(':')[2].replace('>', '')) for e in full_emojis]
  extentions = ["gif","png"]
  for e in custom_emoji_ids:
    ex_vaild = bool(0)
    for ex in extentions:
      url = "https://cdn.discordapp.com/emojis/"+str(e)+"."+str(ex)
      async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as tmpImage:
          if(tmpImage.status)==200 and not ex_vaild:
            images.append(url)
            ex_vaild = bool(1)
  return images

def get2(message):
  names = []
  full_emojis=re.findall(r':\w*:\d*',message.content)
  custom_emoji_names = [(e.split(':')[1].replace('>', '')) for e in full_emojis]
  for e in custom_emoji_names:
    names.append(e)
  return names

async def get_emoji_id(emoji_id):
  images = []
  extentions = ["gif","png"]
  custom_emoji_ids = []
  custom_emoji_ids.append(emoji_id)
  for e in custom_emoji_ids:
    ex_vaild = bool(0)
    for ex in extentions:
      url = "https://cdn.discordapp.com/emojis/"+str(e)+"."+str(ex)
      async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as tmpImage:
          if(tmpImage.status)==200 and not ex_vaild:
            images.append(url)
            ex_vaild = bool(1)
  return images

async def default_emojis(message):
  emojis_return = []
  emoji_count=emojis.count(message.content,unique=False)
  if emoji_count > 0:
    emojis_return = emojis.get(message.content)
  if emoji_count == 0:
    for message_wanted in await message.channel.history(limit=100).flatten():
        emoji_count=emojis.count(message_wanted.content,unique=False)
        if emoji_count != 0:
          emojis_return = emojis.get(message_wanted.content) 

  if len(emojis_return) == 0:
    await message.channel.send("no default emoji found")
  import twemoji_parser
  for x in emojis_return:
    emojis_used=emojis.decode(x)
    emojis_used=emojis_used.replace(":","")
    url = await twemoji_parser.emoji_to_url(x)
    for a in x:
      digit = (f"{hex(ord(a))}").lstrip("0x")
      unicode = f"\\U{digit:>08}"
      unicode_site = f"http://www.fileformat.info/info/unicode/char/{digit}"
      embed=discord.Embed(title="Default Emote:",url=unicode_site,color=random.randint(0, 16777215))
      embed.add_field(name="Name:",value=emojis_used)
      embed.add_field(name="Unicode:",value=unicode)
      embed.add_field(name="unicode url",value=f"[site]({unicode_site})")
      embed.add_field(name="Credit:",value=f"[[Site 1]](https://emojis.readthedocs.io/en/latest/api.html) [[Site 2]](https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/meta.py#L250-L264)")
      embed.set_image(url=url)
      embed.set_footer(text=f"click the title for more unicode data")
    await message.channel.send(embed=embed)