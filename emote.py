import re
import requests
def get(message):
  images = []
  full_emojis=re.findall(r':\w*:\d*',message.content)
  # custom_emoji_names = [(e.split(':')[1].replace('>', '')) for e in full_emojis]
  custom_emoji_ids = [(e.split(':')[2].replace('>', '')) for e in full_emojis]
  extentions = ["gif","png"]
    #print(custom_emoji_names)
    #print(custom_emoji_ids)
  for e in custom_emoji_ids:
    ex_vaild = bool(0)
    for ex in extentions:
      url = "https://cdn.discordapp.com/emojis/"+str(e)+"."+str(ex)
      tmpImage = requests.get(url)
      if(str(tmpImage)!="<Response [415]>") and not ex_vaild:
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