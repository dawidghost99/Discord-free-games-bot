"""

import games as g
import discord
from dotenv import load_dotenv
import os
import time

from datetime import datetime
from threading import Timer


#x=datetime.today()
#y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
#delta_t=y-x

#secs=delta_t.total_seconds()


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

    






token = "NzExNjYyMjQ3MDEyODU5OTQ0.XsGS0g.UxFksdU5RaM_xRhi_26PLL4HoYs" # I've opted to just save my token to a text file. 

client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")



    #t = Timer(secs, pushNotification)
    #t.start()
    


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
            


client.run(token)

"""