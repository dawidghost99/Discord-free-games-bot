import games as g
import discord
from dotenv import load_dotenv
import os
import time

import discord
import asyncio


token = "<unique token here>"



pastGames = []







def pushNotification():
    presentGames = []
    allNewGames = []

    steamURLS = g.Steam()
    ubisoftURLS = g.Ubisoft()
    HBURLS= g.HumbleBundle()
    epicURLS = g.EpicGames()

    presentGames = steamURLS + ubisoftURLS + HBURLS + epicURLS

    if presentGames != pastGames:
        newGames = []
        for item in presentGames:
            if item not in pastGames:
                newGames.append(item)
        for link in newGames:
            allNewGames.append(link)
        del(pastGames[:])
        for game in presentGames:
            pastGames.append(game)

    else:
          del(presentGames[:])
    if not allNewGames:
        return 
    else:
        return allNewGames

    



class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'We have logged in as {client.user}')

    
    async def on_message(self, message):  # event that happens per any message.

        # each message has a bunch of attributes. Here are a few.
        # check out more by print(dir(message)) for example.
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")



    


        #steam games
        if(message.content == "free steam games"):
            steamurls = g.Steam()
            for link in steamurls:
                await message.channel.send(link)
                time.sleep(0.5)

        #ubisoft games    
        if (message.content == "free ubisoft games"):
            ubisoftURLS = g.Ubisoft()
            for link in ubisoftURLS:
                await message.channel.send(link)
                time.sleep(0.5)
            
        # humble bundle games
        if(message.content == "free humble bundle games" or message.content == "hb"):

            hublebundleURLS = g.HumbleBundle()
            for link in hublebundleURLS:
                await message.channel.send(link)
                time.sleep(0.5)



        #epic games
        if(message.content == "free epic games" or message.content == "eg"):
            epicgamesURL = g.EpicGames()
            for link in epicgamesURL:
                await message.channel.send(link)
                time.sleep(0.5)




        #all games 
        if(message.content == "all free games"):

            steamurls = g.Steam()
            for link in steamurls: 
                await message.channel.send(link)
                time.sleep(0.5)

            ubisoftURLS = g.Ubisoft()
            for link in ubisoftURLS:
                await message.channel.send(link)
                time.sleep(0.5)

            hublebundleURLS = g.HumbleBundle()
            for link in hublebundleURLS:
                await message.channel.send(link)
                time.sleep(0.5)

            epicgamesURL = g.EpicGames()
            for link in epicgamesURL:
                await message.channel.send(link)
                time.sleep(0.5)



        #help message    
        if (message.content == "<@!711662247012859944>"):
            await message.channel.send("This is a bot that tells you all the free games available from Steam, Ubisoft, Epic games and Humble Bundle")
            time.sleep(2)
            await message.channel.send("You can type:")
            await message.channel.send("'free steam games'")
            await message.channel.send("'free ubisoft games'")
            await message.channel.send("'free epic games'")
            await message.channel.send("'free humble bundle games'")
            await message.channel.send("'@Free Games Bot' for help")
            time.sleep(1)
            await message.channel.send("this bot has been created by the almighty Dawid")


        if(message.content == "new games are out!" or message.content == "push" ):
            newGames = pushNotification()
            for game in newGames:
               await message.channel.send(game)
            

    
    async def my_background_task(self):
        await self.wait_until_ready()
        
        
        while not self.is_closed():
            text_channel_list = []
            for server in Client.servers:
                for channel in server.channels:
                    if channel.type == 'Text':
                        text_channel_list.append(channel)

            for x in range(len(text_channel_list)):
                channel = self.get_channel(text_channel_list[x]) # channel ID goes here
                newGames = pushNotification()
                if (len(newGames)>0 ):
                    for game in newGames:
                        await message.channel.send(game)

            del(text_channel_list[:])

            await asyncio.sleep(10) # task runs every 24 hours //86400
    
client = MyClient()
client.run(token)
