import discord
import urllib.request
import os

TOKEN = 'APP TOKEN'

client = discord.Client()

@client.event
async def on_message(message):
    #the bot doesnt talk to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!ping'):
        msg = 'Pong !!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!loli'):
        urllib.request.urlretrieve('https://i.redd.it/jcn2v6seyyo01.jpg', './loli.jpg')
        await client.send_file(message.channel, './loli.jpg')
        os.remove('./loli.jpg')

@client.event
async def on_ready():
    print('NaM-Bot on Duty')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
