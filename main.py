import discord
import asyncio
import requests
import json
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = discord.Intents.all(), command_prefix='$')

@client.event
async def on_ready():
    print('Successfully logged in')

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
