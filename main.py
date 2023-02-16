import logging
import os
import re
import sys
import traceback

import aiohttp
import asyncpg
import discord
import dotenv
from discord.ext import commands

from cogs import EXTENSIONS


async def get_prefix(bot, message):
    extras = ["jd/", "j/"]

    comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
    match = comp.match(message.content)
    if match is not None:
        extras.append(match.group(1))

    return commands.when_mentioned_or(*extras)(bot, message)


class JDJGBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def start(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()
        self.db = await asyncpg.create_pool(os.getenv("DB_key"))

        # self.linked_data = await self.db.fetch("SELECT * FROM linked_chat")
        # self.linked_channels = [c.get("channel_id") for c in self.linked_data]

        # change this to be different(unique global chat table name, with linked channels like the orginal method)

        # grab from guild_bans - guild bans
        # bans - user bans (blacklist)

        await super().start(*args, **kwargs)

    async def close(self):
        await self.session.close()
        await self.db.close()
        await super().close()

    async def setup_hook(self):
        for cog in EXTENSIONS:
            try:
                await self.load_extension(f"{cog}")

            except commands.errors.ExtensionError:
                traceback.print_exc()


bot = JDJGBot(command_prefix=(get_prefix), intents=discord.Intents.all())


@bot.event
async def on_error(event, *args, **kwargs):
    more_information = sys.exc_info()
    error_wanted = traceback.format_exc()
    traceback.print_exc()
    # print(more_information[0])


logging.basicConfig(level=logging.INFO)
bot.run(os.environ["TOKEN"])
