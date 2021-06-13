import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import os
from googleapiclient.discovery import build
import random

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']

client = commands.Bot(command_prefix=';')

@client.event
async def on_ready():
    server_count = 0
    server = get(client.guilds)
    print(f'{client.user} sedang terhubung dengan beberapa server:')
    for server in client.guilds:
          print(f'- {server.name} (id:{server.id})')
          server_count = server_count + 1

@client.command(name='pi', help='Sambutan untuk para mahasiswa.')
async def pi(ctx):
    ucapan = [
        'Selamat mengerjakan PI guys. @everyone',
        'Tetap semangat guys, jangan menyerah. @everyone',
        'GASS terus aja dospem sampe SIDANG !!! @everyone', 'BOT KNTL'
    ]

    respon = random.choice(ucapan)
    await ctx.send(respon)

client.run(TOKEN)