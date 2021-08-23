import discord
from discord.ext import commands
from discord.utils import get
from googleapiclient.discovery import build
from datetime import datetime
import os
import random

TOKEN = os.environ['DISCORD_TOKEN']
client = commands.Bot(command_prefix=';')
api_key = os.environ['PSE']
server = get(client.guilds)

@client.event
async def on_connect():
    print('Bot terhubung...')

@client.event
async def on_disconnect():
    print('Bot terputus...')

@client.event
async def on_ready():
    server_count = 0
    print(f'{client.user} telah terhubung dengan beberapa server:')
    for server in client.guilds:
        print(f'- {server.name} (id:{server.id})')
        server_count = server_count + 1


async def on_message(message): 
  if message.author == client.user:
      return  

@client.command(name='pi', help='Sambutan untuk para mahasiswa.')
async def pi(ctx):
    ucapan = [
        'Selamat mengerjakan PI guys @everyone',
        'Tetap semangat guys, jangan menyerah.',
        'GASS terus aja dospemnya sampe SIDANG !!!',
        'Jangan lupa etika ketika bimbingan guys'
    ]
    respon = random.choice(ucapan)
    await ctx.send(respon)

@client.command(name='show', help='Untuk mencari gambar.')
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build('customsearch', 'v1', developerKey=api_key).cse()
    hasil = resource.list(
        q=f'{search}', cx='a1dbccf8343835fb1', searchType='image'
    ).execute()
    url = hasil['items'][ran]['link']
    embed1 = discord.Embed(title='Hasil pencarian', timestamp=datetime.utcnow())
    embed1.set_image(url=url)
    fields = [('Nama',f'{search.title()}',True),
              ('Sumber',f'[Tekan disini]({url})',True)]
    for name, value, inline in fields:
      embed1.add_field(name=name, value=value, inline=inline)
    embed1.set_author(name='Bot PI Discord')
    embed1.set_footer(text='diakses pada')
    await ctx.send(embed=embed1)

client.run(TOKEN)