import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('gamblino'):
        await message.channel.send('What\'s up?')

client.run('NzM5ODczNjMwODE2Njk4NTAx.XygzAw.JVBq0HgU_nxlXdRMhAiZa1og3cU')