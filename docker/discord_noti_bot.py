import discord
import nest_asyncio
import socket
import requests
import re

nest_asyncio.apply()

CHANNEL_ID = '1194122219543089166'
TOKEN = 'MTE5NDEyOTI3MzE2NzAyNDI2OQ.GNWQ3b.e0dfHmPFrBr0rKnlRfd14mlmAaOcWPZFcAtam0'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("대기중.."))
    print("봇 실행됨!")
    print(client.user.name)
    print(client.user.id)
    
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!현재ip":
        req = requests.get("http://ipconfig.kr")
        out_addr = re.search(r'IP Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
        await message.channel.send(out_addr) 

client.run(TOKEN)