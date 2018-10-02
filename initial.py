import discord

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

@client.event
async def on_ready():
    print('Wito-Bot on Duty')
    print(client.user.name)
    print(client.user.id)
    print('------')