import discord

yetkiler = discord.Intents.default()

yetkiler.message_content = True

bot = discord.Client(intents=yetkiler)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('/merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('/bye'):
        await message.channel.send(":waving_hand:")
    else:
        await message.channel.send(message.content)
        
