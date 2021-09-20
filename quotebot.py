import discord
from discord import message
from discord.ext import commands
import random
import os

#initialize bot
#Set command prefix
bot = commands.Bot(command_prefix = '.', description='.bothelp for commands')

#create event
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('your mom xD'))
    print("Bot ready...")

#test command
@bot.command()
async def ping(ctx):
    #retrieve latency of bot
    latency = bot.latency
    #send latency to user
    await ctx.send(latency)
@bot.event

#print cooldown error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = "**I'm on cooldown**, please wait {:.2f}s daddy :)".format(error.retry_after)
        await ctx.send(msg)


@bot.command()
#command list
async def bothelp(ctx):
    await ctx.send(
        "Here are a list of my commands:"
        "\n"
        "\n**.quote** - generate a random quote"
        "\n**.addquote** - add your own quote"
        "\n**.lastquote** - print the last added quote"
        "\n**.randomnumber** - print a random number"
        "\n**.rps** - play a game of rock, paper, scissors against me"
        )


@bot.command()
#set quote command
async def addquote(ctx):
    await ctx.send("Please enter your quote in the following format - 'quote.... - author'")
    text_file = open("quotes.txt", "a")
    msg = await bot.wait_for("message")
    text_file.write(f"\n{msg.content}")
    text_file.close
    await ctx.send("Quote Added!")

@bot.command()
#retrieve last added
async def lastquote(ctx):
    f=open("quotes.txt", "r")
    lines = f.readlines()
    await ctx.send(lines[-1])
    f.close()

@bot.command()
#random number generator
async def randomnumber(ctx):
    await ctx.send(f"The random number is {random.randint(0, 100)}")

moves = ['rock', 'paper', 'scissors']
#rock paper scissors 
@bot.command()
async def rps(ctx):
    game = True
    global moves
    await ctx.send("Game Started: Please type 'rock', 'paper', or 'scissors'")
    player = await bot.wait_for("message")
    computer = random.choice(moves)
    if computer == player.content:
        await ctx.send(f"The bot chose {computer}, it's a tie!")
    elif computer == 'scissors' and player.content == 'paper':
        await ctx.send(f"The bot chose {computer}, you lost!")
    elif computer == 'paper' and player.content == 'rock':
        await ctx.send(f"The bot chose {computer}, you lost!")
    elif computer == 'rock' and player.content == 'scissors':
        await ctx.send(f"The bot chose {computer}, you lost!")
    elif player == 'quit':
        await ctx.send("Qutting game, see you next time!")
    else:
        await ctx.send(f"The bot chose {computer}, you win!")

    
#set cooldwon
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
#quote command
async def quote(ctx):
    f=open("quotes.txt", "r")
    lines = f.readlines()
    await ctx.send(random.choice(lines))
    f.close()


#with open('badwords.txt', 'r') as f:
#    global badwords  
#    words = f.read()
#    badwords = words.split()
#
#with open('greetings.txt', 'r') as f:
#    global greetings  
#    words = f.read()
#    greetings = words.split()

#@bot.event
#async def on_message(message):
#    if message.author == bot.user or message.author.bot:
#        return
#
#    for word in badwords:
#        if word in message.content:
#            await message.reply(f"Hey {message.author.mention}, don't fucking use that language you fat nasty cunt", mention_author=True)
#    for word in greetings:
#       if word in message.content:
#            await message.reply(f"Hello {message.author.mention}, ur so sexy ;)", mention_author=True)
#    await bot.process_commands(message)

#run event
bot.run('ODg4MTkwNjY0NDM1Njk5NzEy.YUPGBA.tVA4j3kkN_iwkdc_DMCfZC-iA_o')
