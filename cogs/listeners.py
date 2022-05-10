from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Ready")
        print(f"Logged in as {self.bot.user}")
        print(f"Id: {self.bot.user.id}")


async def setup(bot):
    await bot.add_cog(Events(bot))
