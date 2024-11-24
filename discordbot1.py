import discord
import os
from discord.ext import commands
import random
from tokenignore import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

# -------------------------------- KOMUTLAR --------------------------------
@bot.command()
async def quiz(ctx):
    await ctx.send(f"Quizimiz başlamak üzere! Bakalım ne kadar çevreye duyarlısın.")
    puan = 0
    s = 0
    if puan == 0:
        x = random.randint(1, 5)
        if x == 1:
            y = await ctx.send(f"Yere cöp atıyormusun? Evet/Hayır") 
            if y == "Evet":
                await ctx.send(f"Ne kadar kötü! :(")
                s +=1
            elif y == "Hayır":
                await ctx.send(f"Güzel! +10 puan :)")
                puan += 10
                s +=1
        if x == 2:
            z = await ctx.send(f"Dışarıdayken yere cöp atıyormusun? Evet/Hayır") 
            if z == "Evet":
                await ctx.send(f"Ne kadar kötü! :(")
                s +=1
            elif z == "Hayır":
                await ctx.send(f"Güzel! +10 puan :)")
                puan += 10
                s +=1
        if x == 3:
            c = await ctx.send(f"Geri dönüşüm yapıyormusun? Evet/Hayır") 
            if c == "Hayır":
                await ctx.send(f"Ne kadar kötü! :(")
                s +=1
            elif c == "Evet":
                await ctx.send(f"Güzel! +10 puan :)")
                puan += 10
                s +=1
        if x == 4:
            v = await ctx.send(f"Evde yemeğin olmasına rağmen dışarda mı yemek yermisin? Evet/Hayır") 
            if v == "Evet":
                await ctx.send(f"Ne kadar kötü! :(")
                s +=1
            elif v == "Hayır":
                await ctx.send(f"Güzel! +10 puan :)")
                puan += 10
                s +=1
        if x == 5:
            b = await ctx.send(f"Yemeğini israf ediyormusun? Evet/Hayır") 
            if b == "Evet":
                await ctx.send(f"Ne kadar kötü! :(")
                s +=1
            elif b == "Hayır":
                await ctx.send(f"Güzel! +10 puan :)")
                puan += 10
                s +=1
    if s == 5:
        await ctx.send(f"Quizimiz bitti puanın hesaplanıyor") 
        if puan >= 40:
            await ctx.send(f"iyi böyle devam et")
        elif puan >= 20 or puan <= 30:
            await ctx.send(f"Daha iyi yaparsın! Eksiklerin var araştırman lazım!")
        elif puan <= 20:
            await ctx.send(f"Kötü yaptın... Hatalarını lütfen araştır!")
    
    

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


# Left one is the dice number, right one is the biggest number on dice (1 to max-number)
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

# YENİ KOMUT
@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def rastgele(ctx):
    dosya_liste = os.listdir('images')
    # dosya_liste = ["mem1.png", "mem2.png", "mem3.png", "mem4.png"]
    rastgele = random.choice(dosya_liste)
    with open("images/"+rastgele, "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run(token)
        
