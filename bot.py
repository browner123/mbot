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
    if message.content != "Choose":
        await client.send_message(message.channel, random.choice(["What are you talking about?", "you lie", "that is not true", "maybe", "hmm i think you are right", "hmm"]))
    if message.content == "Choose":
        server = message.server.members
        user = list(server)
        x = random.randint(1, len(server) - 1)
        y = random.randint(3,9)
        time.sleep(y)
        await client.send_message(message.channel, str(user[x]) + ", if he does not play then ask me again")
    
client.run(os.getenv('TOKEN'))
