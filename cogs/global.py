from discord.ext import commands

# area to start designing global chat.


class Global(commands.Cog):
    "Global Chat commands"

    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Global(bot))
