import discord
import random
import os
import math
from keep_me_alive import keep_alive
from someRandomFunctions.Scientific_calculator import Scientific_calc as sc
from someRandomFunctions.Messages import Responses as r
from someRandomFunctions.datechainnotsus import dateGen as dG
import time as t
# Test change
client = discord.Client()


CommonOperations = ["+", "-", "*", "/"]
rad = math.pi / 180

def scientific_calc(query):
        answer = sc.scientific_calc(query)
        return answer

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

SHUT = r.emojis[":SHUT:"]

@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return
    for word in r.Bot_greetings_2:
        if word in msg:
            await message.channel.send(random.choice(r.Doge_happy))
    for word in r.hurt:
        if word in msg:
            await message.channel.send(SHUT)
    if msg.startswith(',suntzu quote'):
        await message.channel.send(random.choice(r.SunTzuQuotes))
    if "inspirational" in msg:
        await message.channel.send(random.choice(r.happy_messages))
    if "wish" in msg:
        msg_a = msg.split()
        msg_len = len(msg_a)
        person = str(msg_a[1])
        if msg_len == 4:
          n = int(msg_a[2])
          if n>20:
            await message.channel.send(random.choice(r.bruv))
          else:
            n = int(msg_a[2])
            for i in range(n):
                await message.channel.send("hello " +    person + "!")
            
        
    if "say" in msg:
        if "right now" in msg:
            a = msg.split()
            b = a[1]
            await message.channel.send(b)
    if "doge" in msg:
        if "are you okay" in msg:
            await message.channel.send("Yes master, I am fine")
        elif "source code" in msg:
            await message.channel.send("https://github.com/SuperComputer29/disbot-new-")
        else:
            for word in r.Bot_greetings_1:
                if word in msg:
                    await message.channel.send(random.choice(r.Doge_greetings))


    if "random" in msg:
      n = [1,2,3,4,5,6,7,8,9,0]
      await message.channel.send(random.choice(n))

    
    if "calculate" in msg:
        a = msg.split()
        a.pop(0)
        n = len(a)
        def strAdd(x):
            if x == 1:
                return str(a[0])
            else:
                return str(a[x-1]) + " " + str(strAdd(x-1))

        user_input = strAdd(n)
        answer = sc.scientific_calc(user_input)
        await message.channel.send(answer)
    
    if "inititate skeem" in msg:
        a = msg.split()
        time = a[2]
        date = dG()
        await message.channel.send(f"the time that you specified is {time} and the date today is {date}")
        while True:
            current_t = t.localtime()
            current_clock = t.strftime("%H%M", current_t)
            if current_clock == time:
                await message.channel.send(date)
                exit(0)

keep_alive()
token = os.environ['key']
client.run(token)
