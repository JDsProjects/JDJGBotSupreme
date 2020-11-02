async with aiohttp.ClientSession() as cs:
  async with cs.get(url) as r:
    image=await r.read()
    f = open("reverse.png","wb")
    f.write(image)
    f.close()