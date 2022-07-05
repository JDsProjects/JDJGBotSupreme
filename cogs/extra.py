from discord.ext import commands
import discord, random

class Extra(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(brief = "says nook nook and shows an image")
  async def pingu(self, ctx):
    embed = discord.Embed(description = f"nook nook", color = random.randint(0, 16777215))
    embed.set_image(url = "https://i.imgur.com/Z6NURwi.gif")
    embed.set_author(name = f"Pingu has been summoned by {ctx.author}:", icon_url = ctx.author.avatar_url)
    await ctx.send("nook nook", embed = embed)

async def setup(bot):
  await bot.add_cog(Extra(bot))
