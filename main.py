import discord
import random
import asyncio
import requests
import os
import time

client = discord.Client()



@client.event

async def on_ready():
  
  print("Bot is ready")
  

  

  
  
  
client.run(os.environ['Discordtoken'])