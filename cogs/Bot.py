import random
import time

import discord
from discord.ext import commands


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

    @commands.command(brief="gives you an invite to invite the bot.", aliases=["inv"])
    async def invite(self, ctx):
        normal_inv = discord.utils.oauth_url(self.bot.user.id, permissions=discord.Permissions(permissions=8))
        minimial_invite = discord.utils.oauth_url(
            self.bot.user.id, permissions=discord.Permissions(permissions=70635073)
        )

        normal_inv_slash = discord.utils.oauth_url(
            self.bot.user.id, permissions=discord.Permissions(permissions=8), scopes=("bot", "applications.commands")
        )
        minimial_invite_slash = discord.utils.oauth_url(
            self.bot.user.id,
            permissions=discord.Permissions(permissions=70635073),
            scopes=("bot", "applications.commands"),
        )

        embed = discord.Embed(title="Invite link:", color=random.randint(0, 16777215))
        embed.add_field(
            name=f"{self.bot.user.name} invite:",
            value=f"[{self.bot.user.name} invite url]({normal_inv}) \nNon Markdowned invite : {normal_inv}",
        )
        embed.add_field(name="Minimial permisions", value=f"{ minimial_invite}")

        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.set_footer(
            text=f"not all features may work if you invite with minimal perms, if you invite with 0 make sure these permissions are in a Bots/Bot role."
        )

        view = discord.ui.View()

        view.add_item(
            discord.ui.Button(
                label=f"{self.bot.user.name}'s Normal invite", url=normal_inv, style=discord.ButtonStyle.link
            )
        )
        view.add_item(
            discord.ui.Button(
                label=f"{self.bot.user.name}'s Minimial Permisions Invite",
                url=minimial_invite,
                style=discord.ButtonStyle.link,
            )
        )

        view.add_item(
            discord.ui.Button(
                label=f"{self.bot.user.name}'s Normal Invite(Slash)",
                url=normal_inv_slash,
                style=discord.ButtonStyle.link,
                row=2,
            )
        )
        view.add_item(
            discord.ui.Button(
                label=f"{self.bot.user.name}'s Minimial Permisions(Slash)",
                url=minimial_invite_slash,
                style=discord.ButtonStyle.link,
                row=2,
            )
        )

        await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Bot(bot))
