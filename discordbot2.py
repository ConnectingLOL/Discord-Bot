import discord
import os
from discord.ext import commands
from tokenignore  import token
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def rastgele(ctx):
    dosya_liste = os.listdir('images')
    # dosya_liste = ["mem1.png", "mem2.png", "mem3.png"]
    rastgele = random.choice(dosya_liste)
    with open("images/"+rastgele, "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

