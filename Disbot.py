import discord
import random
import math
import os
from random import randrange
from keep_me_alive import keep_alive

client = discord.Client()

happy_messages = ["You’re off to great places",
                  "Your success mountain is waiting, so get on your way.",
                  "You always pass failure on the way to success.",
                  "No one is perfect - that’s why pencils have erasers.",
                  "Winning doesn’t always mean being first. Winning means you’re doing better than you’ve done before.",
                  "You’re braver than you believe, and stronger than you seem, and smarter than you think.",
                  "It always seems impossible until it is done."
                  "Keep your face to the sunshine and you cannot see a shadow.",
                  "Once you replace negative thoughts with positive ones, you’ll start having positive results.",
                  "Positive thinking will let you do everything better than negative thinking will.",
                  "Winning is fun, but those moments that you can touch someone’s life in a very positive way are "
                  "better. "
                  ]
Bot_greetings_1 = ["hey bot", "hey boi", "hey doge boi", "hey doge bot", "hello bot", "hello boi", "hello doge boi",
                   "hello doge bot", "hi bot", "hi boi", "hi doge boi", "hi doge bot", "hey doge", "hi doge",
                   "hello doge", "poda"]

Bot_greetings_2 = ["good job doge", "well done doge", "you are a good boi doge"]

Doge_greetings = ["Hello master", "I was waiting for you", "hello", "hi", "Wat do you want idiot", "shut up"]

Doge_happy = ["Awww thank you!", "thank you master", "I will always obey you!"]

SunTzuQuotes = ["Be extremely subtle, even to the point of formlessness",
                "Let your plans be dark as night, and when you're ready,"
                " fall like a thunderbolt",
                "All men can see the tactics whereby I conquer, But what none can see is the strategy out of which "
                "victory is evolved",
                "The opportunity of defeating the enemy is provided by the enemy himself",
                "If you know the enemy and know yourself, you need not fear the results of 100 battles",
                "Appear weak when you are strong and strong when you are weak", "Dying is for losers",
                "Sweat more during peace", "get rekt noob",
                "Whatever you do, dont reveal all your techniques all in a youtube video you moron",
                "All war is deception",
                "don't believe everything a bot says"]
ROB_greetings = ["Hello Wide Putin", "How u doin?", "I am kim jong un", "trump is better than u", ]
hurt = ["poop",
        "dung",
        "rotten",
        "idiot",
        "stupid",
        "you suc",
        "low life",
        "shit",
        "crap",
        "loser"
        "u suc"
        ]
bruv = ["no u", "bruv", "dude no", "lol no", "yo fam chill he'll come in a bit"]


emojis = {
    ":yubullyme:":"<:yubullyme_:823182635543167016> ",
    ":ytho:":"<:ytho:809445359888760903>",
    ":yourtimehascome:":"<:yourtimehascome:842007392320225280>",
    ":wearetrapped:":"<:wearetrapped:834772665306578964>",
    ":UNSHUT:":"<:UNSHUT:822704982780149831>",
    ":thumbsupcat:":"<:thumbsupcat:809416615590101012>",
    ":surprisedpikachufaces:":"<:surprisedpikachufaces:822705907338969088>",
    ":spanishguy:":"<:spanishguy:809445312867467284>",
    ":spam:":"<:spam:810881209667682325>",
    ":SHUT:":"<:SHUT:823226874770751498>",
    ":shrek:":"<:shrek:811810436235788355>",
    ":Sadcat:":"<:Sadcat:809418467580444722>",
    ":phtoooo:":"<:phtoooo:830085584948953088>",
    ":panik:":"<:panik:810881666805268511>",
    ":ohmygawd:":"<:ohmygawd:813790932381073488>",
    ":ohcomeon:":"<:ohcomeon:826350441871966208>",
    ":nou:":"<:nou:822706727908016148>",
    ":not_funny:":"<:not_funny:844259065671712788>",
    ":nobully:":"<:nobully:823948467268747305>",
    ":nice:":"<:nice:814502223115452446>",
    ":nani:":"<:nani:822706256757522452>",
    ":letmethink:":"<:letmethink:809445199457550386>",
    ":Laughcry:":"<:Laughcry:809453871087747123>",
    ":itstoolate:":"<:itstoolate:824243113421307914>",
    ":itsbigbraintime:":"<:itsbigbraintime:809445405514268742>",
    ":imagine2:":"<:imagine2:811810530025013268>",
    ":imagine:":"<:imagine:811810571442716733>",
    ":ididntmeantosaythat:":"<:ididntmeantosaythat:818141109166407730>",
    ":iamtotallyfine:":"<:iamtotallyfine:809445069412106280>",
    ":iamnotgonnahurtyouatall:":"<:iamnotgonnahurtyouatall:824243545690472458>",
    ":Iamfine:":"<:Iamfine:810754237390389268>",
    ":iamconfused:":"<:iamconfused:814724278469132298>",
    ":hmmm:":"<:hmmm:825027611888975872>",
    ":hehe:":"<:hehe:822706064138174474>",
    ":frustration:":"<:frustration:811810480900538408>",
    ":fear:":"<:fear:825027462840844329>",
    ":doge_1:":"<:doge_1:809240577920073729>",
    ":cryingnoisesintensifies:":"<:cryingnoisesintensifies:822705432702877737>",
    ":buddhamode:":"<:buddhamode:817729168497704980>",
    ":aysheri:":"<:aysheri:816664207730671686>",
    ":awww:":"<:awww:809445128560443425>",
    ":AaAarGHHHH:":"AaAarGHHHH"
}

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

SHUT = emojis[":SHUT:"]

@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return
    for word in Bot_greetings_2:
        if word in msg:
            await message.channel.send(random.choice(Doge_happy))
    for word in hurt:
        if word in msg:
            await message.channel.send(SHUT)
    if msg.startswith(',suntzu quote'):
        await message.channel.send(random.choice(SunTzuQuotes))
    if "inspirational" in msg:
        await message.channel.send(random.choice(happy_messages))
    if "wish" in msg:
        msg_a = msg.split()
        msg_len = len(msg_a)
        person = str(msg_a[1])
        if msg_len == 4:
          n = int(msg_a[2])
          if n>20:
            await message.channel.send(random.choice(bruv))
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
            for word in Bot_greetings_1:
                if word in msg:
                    await message.channel.send(random.choice(Doge_greetings))
    if "casino" in msg:
        await message.channel.send("let's play the doge casino bois, I and you will select a number between 1 and 10, ")

    if "sqrt" in msg:
        a = msg.split("(")
        b = a[1]
        c = b.split(")")
        d = int(c[0])
        e = sqrt(d)
        await message.channel.send(e)
    if "!" in msg:
        if "!poll" in msg:
            s = msg.split()
            a = s[0]
            p = "!poll"
            poll_emojis = ['✅','❌']            
            if a == p:
                for emojis in poll_emojis:
                    await message.add_reaction(emojis)
        else:
            a = msg.split("!")
            b = int(a[0])
            c = factorial(b)
            await message.channel.send(c)
    if "sum" in msg:
        if ",w" not in msg:
            s = msg.split()
            a = int(s[2])
            b = int(s[4])
            c = sum(a, b)
            await message.channel.send(c)
    if "random" in msg:
      n = [1,2,3,4,5,6,7,8,9,0]
      await message.channel.send(random.choice(n))
    



keep_alive()
token = os.environ['key']
client.run(token)
