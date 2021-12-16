import discord
import random
import math
import os
from random import randrange
from keep_me_alive import keep_alive
from Scientific_Calculator import scientific_calc
from Messages import Responses as r
# Test change
client = discord.Client()

def sqrt(n):
    a = randrange(10)
    for i in range(500):
        a = (n + a ** 2) / (2 * a)
    return a


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def sum(a, b):
    if a > b:
        return 0
    else:
        return b + sum(a, b - 1)


CommonOperations = ["+", "-", "*", "/"]
rad = math.pi / 180


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
            await message.channel.send("https://github.com/SuperComputer29/Disbot/blob/main/Disbot.py")
        else:
            for word in r.Bot_greetings_1:
                if word in msg:
                    await message.channel.send(random.choice(r.Doge_greetings))


    if "!" in msg:
        if "!poll" in msg:
            s = msg.split()
            a = s[0]
            p = "!poll"
            poll_emojis = ['✅','❌']            
            if a == p:
                for emojis in poll_emojis:
                    await message.add_reaction(emojis)


    if "sum" in msg:
        s = msg.split()
        a = int(s[2])
        b = int(s[4])
        c = sum(a, b)
        await message.channel.send(c)


    if "random" in msg:
      n = [1,2,3,4,5,6,7,8,9,0]
      await message.channel.send(random.choice(n))

    
    if "calculate" in msg:
        scientific_calc()
        
keep_alive()
token = os.environ['key']
client.run(token)
