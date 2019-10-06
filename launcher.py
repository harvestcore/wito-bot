import discord
import urllib.request
import os
import asyncio


TOKEN = 'APP TOKEN'

client = discord.Client()

@client.event
@asyncio.coroutine
def on_message(message):
    #the bot doesnt talk to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        yield from client.send_message(message.channel, msg)

    if message.content.startswith('!ping'):
        msg = 'Pong !!'.format(message)
        yield from client.send_message(message.channel, msg)

    if message.content.startswith('!loli'):
        msg = 'No se permiten lolitas en este repositorio'.format(message)
        yield from client.send_file(message.channel, './loli.jpg')
        os.remove('./loli.jpg')

    if message.content.startswith('!pacman'):
        msg = 'kiere un pokito¿¿¿¿¿ :p'.format(message)
        yield from client.send_message(message.channel, msg)

    if message.content.startswith('!test'):
        msg = 'Este comando es un test'.format(message)
        yield from client.send_message(message.channel, msg)
        
    if message.content.startswith('!exit'):
        msg = 'Cerrando bot bip bup'.format(message)
        yield from client.send_message(message.channel, msg)
        sys.exit()

@client.event
@asyncio.coroutine
def on_ready():
    print('--- STARTED BOT ---')
    print('NaM-Bot Started')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
