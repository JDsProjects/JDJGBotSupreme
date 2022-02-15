from discord.ext import commands
import time
import discord

class Bot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="sends pong and the time it took to do so.")
    async def ping(self, ctx):
        start = time.perf_counter()
        message = await ctx.send("Ping")
        end = time.perf_counter()

        embed = discord.Embed(title="Bot Ping Data", color=15428885, timestamp=ctx.message.created_at)

        embed.add_field(name="Bot Latency:", value=f"{round((end - start)*1000)} MS", inline=False)

        embed.add_field(name="Websocket Response time:", value=f"{round(self.bot.latency*1000)} MS", inline=False)

        await message.edit(content=f"Pong", embed=embed)

def setup(bot):
    bot.add_cog(Bot(bot))