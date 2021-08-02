from discord.ext import commands
import discord, random, bisect

class Dice(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(brief="a command to roll d20",aliases=["roll20"])
  async def dice_roll20(self,ctx):
    embed_message = discord.Embed(title=f" Rolled a {random.randint(1,20)}", color=random.randint(0, 16777215),timestamp=(ctx.message.created_at))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/AivZBWP.png")
    embed_message.set_author(name=f"d20 Rolled by {ctx.author}:",icon_url=(ctx.author.avatar_url))
    embed_message.set_image(url="https://i.imgur.com/9dbBkqj.gif")
    await ctx.send(embed=embed_message)

  @commands.command(brief="a command to roll d6",aliases=["roll6"])
  async def dice_roll6(self,ctx):
    embed_message = discord.Embed(title=f" Rolled a {random.randint(1,6)}", color=random.randint(0, 16777215),timestamp=(ctx.message.created_at))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/AivZBWP.png")
    embed_message.set_author(name=f"d6 Rolled by {ctx.author}:",icon_url=(ctx.author.avatar_url))
    embed_message.set_image(url="https://i.imgur.com/6ul8ZGY.gif")
    await ctx.send(embed=embed_message)

  @commands.command(brief="a command to roll d10",aliases=["roll10"])
  async def dice_roll10(self,ctx):
    embed_message = discord.Embed(title=f" Rolled a {random.randint(1,10)}", color=random.randint(0, 16777215),timestamp=(ctx.message.created_at))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/AivZBWP.png")
    embed_message.set_author(name=f"d10 Rolled by {ctx.author}:",icon_url=(ctx.author.avatar_url))
    embed_message.set_image(url="https://i.imgur.com/gaLM6AG.gif")
    await ctx.send(embed=embed_message)

  @commands.command(brief="a command to roll d100",aliases=["roll100"])
  async def dice_roll100(self,ctx):
    embed_message = discord.Embed(title=f" Rolled a {random.randint(1,100)}", color=random.randint(0, 16777215),timestamp=(ctx.message.created_at))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/AivZBWP.png")
    embed_message.set_author(name=f"d100 Rolled by {ctx.author}:",icon_url=(ctx.author.avatar_url))
    embed_message.set_image(url="https://i.imgur.com/gaLM6AG.gif")
    await ctx.send(embed=embed_message)

  @commands.command(brief="a command to roll d12",aliases=["roll12"])
  async def dice_roll12(self,ctx):
    embed_message = discord.Embed(title=f" Rolled a {random.randint(1,12)}", color=random.randint(0, 16777215),timestamp=(ctx.message.created_at))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/AivZBWP.png")
    embed_message.set_author(name=f"d12 Rolled by {ctx.author}:",icon_url=(ctx.author.avatar_url))
    embed_message.set_image(url="https://i.imgur.com/gaLM6AG.gif")
    await ctx.send(embed=embed_message)

  @commands.command(brief="a command to roll d8",aliases=["roll8"])
  async def dice_roll8(self,ctx):
    embed_message = discord.Embed(title=f" Rolled a {random.randint(1,8)}", color=random.randint(0, 16777215),timestamp=(ctx.message.created_at))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/AivZBWP.png")
    embed_message.set_author(name=f"d8 Rolled by {ctx.author}:",icon_url=(ctx.author.avatar_url))
    embed_message.set_image(url="https://i.imgur.com/gaLM6AG.gif")
    await ctx.send(embed=embed_message)

  @commands.command(brief="a command to roll d4",aliases=["roll4"])
  async def dice_roll4(self,ctx):
    embed_message = discord.Embed(title=f" Rolled a {random.randint(1,4)}", color=random.randint(0, 16777215),timestamp=(ctx.message.created_at))
    embed_message.set_footer(text = f"{ctx.author.id}")
    embed_message.set_thumbnail(url="https://i.imgur.com/AivZBWP.png")
    embed_message.set_author(name=f"d4 Rolled by {ctx.author}:",icon_url=(ctx.author.avatar_url))
    embed_message.set_image(url="https://i.imgur.com/gaLM6AG.gif")
    await ctx.send(embed=embed_message)

  @commands.command(brief = "sees how compatitable something is(two things)")
  async def works(self, ctx, *args : commands.clean_content):

    if len(args) < 2:
      return await ctx.send("you didn't give me enough objects to checks the status of two items and make sure to have two objects.")

    item1 = args[0]
    item2 = args[-1]

    item_relationship = random.randint(1, 100)

    responses = ["They don't work well together at ALL :angry:", "They work quite poorly together...", "They work kinda good together, maybe", "They work REALLY good together, wow. Nice.", "Let them collaborate anytime."]

    breakpoints = [51, 70, 89, 100, 101]
    i = bisect.bisect(breakpoints, item_relationship)
    resp = responses[i]

    embed = discord.Embed(title = f"How well does {item1} and {item2} work together?",  description = f"They work at a rate {item_relationship}% \n**{resp}**", color = random.randint(0, 16777215), timestamp = ctx.message.created_at)

    embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url))

    embed.set_footer(text = f"{ctx.author.id}")

    await ctx.send(embed = embed)
  
def setup(client):
  client.add_cog(Dice(client))