import discord

TOKEN = 'APP TOKEN'

client = discord.Client()

@client.event
async def on_message(message):
#the bot doesnt talk to itself