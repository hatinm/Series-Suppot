import discord
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
     await client.change_presence(game=discord.Game(name='b!help | b!modcall', type = 3))
     print('Ready, Freddy.')

@client.event
async def on_message(message):
    if message.content.startswith("-support"):
        em = discord.Embed(title = "Call!", description='The following person has requested support \n Please note to ask them about what happened and proof of that!**If they fake called mute them for 10 minutes!**`To claim this call do -claim  and to end the call run -end`\n User who called:'+message.author.mention, footer = 'Burgerizzr Call System 2019 <&/532985783229874236>', colour = 0x00d6e5 )
        await client.send_message(client.get_channel('552655874544369664'), 'CALL!', embed=em)
        await client.send_message(message.author, "I have called support for you, please provide proof to the moderator answering your call! **If you fake called, You will be muted for 10 minutes!**")
        await client.send_message(client.get_channel('545595317031010325'), 'User' +message.author.mention)
    if message.content.startswith("-end"):
        await client.send_message(client.get_channel('552655874544369664'),  ' The Previous Call ended! \n User who accepted the call:'+message.author.mention)
        await client.send_message(client.get_channel('556832372243300362'), 'User has claimed the call' +message.author.mention)
    if message.content.startswith("-claim"):
        await client.send_message(client.get_channel('552655874544369664'),  ' The Previous Call Was Accepted! \n Please Create a ticket with there needs and update it! \n User who accepted the call:'+message.author.mention)
        await client.send_message(message.author, "Thank you for your activity!")
        await client.send_message(client.get_channel('556832372243300362'), 'User has claimed the call' +message.author.mention)


client.run("NTU2ODUyOTYwNzU2NDk4NDMy.D2_xmQ.2ZcOzGk6jIEeef0jUOhpu3jrrcQ")
