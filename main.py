import discord 
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot("/", intents=intents)

@bot.event
async def on_ready():
    print("Bot ligado")

#mensagem de boas-vindas
@bot.event
async def on_member_join(member):
    channel_id = 1390807035636875427
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"Bem-vindo, {member.mention}! 🌷")

#mensagem de saída
@bot.event
async def on_member_remove(member):

    channel_id = 1393722105883004948
    channel = bot.get_channel(channel_id)
    if channel: 
        await channel.send(f"👋 {member.mention} saiu do servidor!")

bot.run("#adicionar o token do bot")