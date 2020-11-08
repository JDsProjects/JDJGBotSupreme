import re
import aiohttp
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