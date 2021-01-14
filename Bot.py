import discord
import json

from dbconnect import DBconnect

client = discord.Client()
conn = DBconnect.create_connection("player_info3.db")
DBconnect.create_table(conn)

with open('config.json', 'r') as file:
    data = json.load(file)
    token = data["discord_key"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('gamblino'):

        content = message.content.split()

        if(content[1] == ("adduser")):
            DBconnect.insert_data(conn,message.author.id,0)
            await message.channel.send("Adding "+message.author.display_name+" to the DB")
        elif(content[1] == ("checkbal")):
            bal = DBconnect.find_data(conn, message.author.id)
            balStr = message.author.display_name+" your current credit balance is "+str(bal[1])
            await message.channel.send(balStr)
        else:
            await message.channel.send("What's up " + message.author.display_name)


        #await message.channel.send('What\'s up '+ message.author.display_name+'?')
        #await message.channel.send('Your unique ID is: '+str(message.author.id))


client.run(token)
