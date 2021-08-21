from discord.ext import commands
import discord
import random
import os

class Events(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_guild_join(self, guild_fetched):
    channels = [channel for channel in guild_fetched.channels]
    roles = roles= [role for role in guild_fetched.roles]
    embed = discord.Embed(title="Bot just joined: "+str(guild_fetched.name), color=random.randint(0,16777215))
    embed.set_thumbnail(url = guild_fetched.icon_url)
    embed.add_field(name='Server Name:',value=f'{guild_fetched.name}')
    embed.add_field(name='Server ID:',value=f'{guild_fetched.id}')
    embed.add_field(name='Server region:',value=f'{guild_fetched.region}')
    embed.add_field(name='Server Creation Date:',value=f'{guild_fetched.created_at}')
    embed.add_field(name='Server Owner:',value=f'{guild_fetched.owner}')
    embed.add_field(name='Server Owner ID:',value=f'{guild_fetched.owner.id}')
    embed.add_field(name='Member Count:',value=f'{guild_fetched.member_count}')
    embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
    embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
    await self.bot.get_channel(738912143679946783).send(embed=embed)

  @commands.Cog.listener()
  async def on_guild_remove(self, guild_fetched):
    channels = [channel for channel in guild_fetched.channels]
    roles = roles= [role for role in guild_fetched.roles]
    embed = discord.Embed(title="Bot just left: "+str(guild_fetched.name), color=random.randint(0,16777215))
    embed.set_thumbnail(url = guild_fetched.icon_url)
    embed.add_field(name='Server Name:',value=f'{guild_fetched.name}')
    embed.add_field(name='Server ID:',value=f'{guild_fetched.id}')
    embed.add_field(name='Server region:',value=f'{guild_fetched.region}')
    embed.add_field(name='Server Creation Date:',value=f'{guild_fetched.created_at}')
    embed.add_field(name='Server Owner:',value=f'{guild_fetched.owner}')
    try:
      embed.add_field(name='Server Owner ID:',value=f'{guild_fetched.owner.id}')
    except:
      pass
    try:
      embed.add_field(name='Member Count:',value=f'{guild_fetched.member_count}')
    except:
      pass
    embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
    embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")

    await self.bot.get_channel(738912143679946783).send(embed=embed)
