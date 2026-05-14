import asyncio
from asyncio import wait_for
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from datetime import datetime, timezone
import random

utc_time = datetime.now(timezone.utc)
local_time = utc_time.astimezone()
quote_time=local_time.strftime('%I:%M %p')

print(f"It's {quote_time}")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

Handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
#quotes from our amazing friend
pascal_quotes=[
    ]
pascalisms = [

]
#discord channel id goes here
quote_channel=1
daily_quote_channel=1
general_channel=1

@bot.event
async def on_ready():
    quoting = bot.get_channel(quote_channel)

    await quoting.send("Hello all! Thank you for subscribing to OnlyPascals where you get premium content from me: The Real Pascal Perez. Im back online btw")



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    number_thing = random.randint(1, 10000)
    if message.author == "":
        await message.channel.send("jump")

    if "can i have a quote" in message.content.lower():
        random_pascal = random.randint(0, len(pascal_quotes) - 1)
        chat = bot.get_channel(quote_channel)
        await chat.send(f"{message.author.mention} quote {random_pascal+1}: " + pascal_quotes[random_pascal])

    if "bloody mary" in message.content.lower():
        await message.channel.send(
            f"hello i am appearing like bloody mary or whatever"
        )
        #secret message. 1 in 10000 chance to produce
    if number_thing == 2:
        await message.channel.send(
            f"{message.author.mention} gosh diddly darn it guy you found the secret message, AGAIN. https://tenor.com/view/game-changer-sam-reich-do-the-wenis-everybody-do-the-wenis-wenis-gif-8137946042093076907 "

        )
    if "onlypascal " in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} OHOHO YOU JUST SUMMONED ME.... THE PASCAL PEREZ"
        )
    elif "onlypascals" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} no you got it wrong its onlypascal"
        )

    if "quote 100" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} SHHH don't tell the FBI. Quote 100 isn't something the world should know about"
        )
    elif "pascal perez" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} hello yes its me.... the real Pascal Perez"
        )
    elif "i want to kiss pascal" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} no"
        )
    elif "don't want to kiss pascal" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} ok"
        )
    elif "goon" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} goon"
        )
    if "filler text" in message.content.lower():
        await message.channel.send(f"{message.author.mention}  filler text for now"
        )
    if "chainsaw man" in message.content.lower():
        await message.channel.send(f"{message.author.mention} now thats a name i haven't heard.... in a loong time."
     )
    if "girth" in message.content.lower():
        await message.channel.send(f"{message.author.mention}  'i am so girth, im birth' -me probably, since im pascal"
    )
    if "thanks pascal" in message.content.lower():
        await message.channel.send(f"{message.author.mention}  you are welcome bestie. slayyy or whatever. i am pascal perez"
    )
    if "Mmmm" in message.content.lower():
        await message.channel.send( "Mmmm"
    )
    await bot.process_commands(message)
    if "enlighten me pascal" in message.content.lower():
        random_pascal = random.randint(0, len(pascalisms) - 1)
        await message.channel.send(
        f"{message.author.mention} Sure! Here's Pascalism {random_pascal+1}: " + pascalisms[random_pascal]
        )
    await bot.process_commands(message)

bot.run(TOKEN, log_handler= Handler, log_level=logging.DEBUG)

