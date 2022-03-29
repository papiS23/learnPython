import discord
import logging
import os


logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.'):
        await message.channel.send(message.content[1:])


client.run(os.environ['TOKEN'])