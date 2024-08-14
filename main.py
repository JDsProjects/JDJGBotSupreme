import logging
import os
import re
import sys
import traceback

import aiohttp
import asyncpg
import discord
import dotenv
from dotenv import load_dotenv
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
        self.db = None
        self.session = None

    async def start(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()

        try:
            self.db = await asyncpg.create_pool(self.db_key)
            self.linked_data = await self.db.fetch("SELECT * FROM global_link")
            self.linked_channels = [c.get("channel_id") for c in self.linked_data]
        except Exception as e:
            print(f"Error connecting to database: {e}")
            self.db = None

        await super().start(*args, **kwargs)

    async def close(self):
        if self.session:
            await self.session.close()
        if self.db:
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


def main():
    db_key = os.getenv("DB_key")
    token = os.getenv("TOKEN")

    if db_key is None or token is None:
        load_dotenv()
        db_key = os.getenv("DB_key")
        token = os.getenv("TOKEN")

    bot.db_key = db_key
    bot.run(token)


if __name__ == "__main__":
    main()
