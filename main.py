import discord
import asyncio
import requests
import json
import random
from StatusAPI import get_status
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
    
    if message.content.startswith('!status'):
        status = get_status()
        embed = discord.Embed(title='Server Status', color=15105570)
        embed.add_field(name='IP-Adresse', value=status['addr'])
        embed.add_field(name='Version', value=status['ver'])
        embed.add_field(name='Spieler Online ', value=status['players'])
        embed.set_footer(text='If there are any issues, contact kuglatec#5088')
        await message.channel.send(embed=embed)
