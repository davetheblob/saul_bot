# bot.py
from cgitb import text
import os
import asyncio
from aiohttp import payload_type

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix=['Call ', 'call '], case_insensitive=True)

@client.event
async def on_ready():
    #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected'
        #f'{guild.name}(id: {guild.id})'
    )
    

#@client.event
#async def on_typing(channel, user, when):
#    await channel.send(f'Shut up, {user.display_name}.')

@client.command(pass_context = True)
async def Saul(ctx):
    if (ctx.author.voice and not ctx.voice_client):
        channel = ctx.message.author.voice.channel
        print(f'{ctx.channel.id}')
        if (ctx.channel.id == 997203369057857616 or ctx.channel.id == 905916365813198888):
            voice = await channel.connect()
            source = FFmpegPCMAudio('sound.mp3')
            player = voice.play(
                source,
                after = lambda e: asyncio.run_coroutine_threadsafe(ctx.guild.voice_client.disconnect(), client.loop)
            )
            await ctx.channel.send(file=discord.File('gif.gif'))
    elif ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        


#@client.command(pass_context = True)
#async def leave(ctx):
#    if (ctx.voice_client):
#        await ctx.guild.voice_client.disconnect()

client.run(TOKEN)