import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os


Client = discord.Client() 
client = commands.Bot(command_prefix = "?") 


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") 

@client.event
async def on_message(message):
    if message.content == "Hello":
        time.sleep(2)
        await client.send_message(message.channel, random.choice(["Whats up guys", "Hello", "Hey", "What is going on"])) 
        if message.content == "How are you":
            await client.send_message(message.channel, random.choice(["ok", "good"])) 
    
client.run(os.getenv('TOKEN'))
