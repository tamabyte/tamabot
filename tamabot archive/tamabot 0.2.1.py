# tamabot.py
# version 0.2.1 dated 04/08/2021

import discord
from discord.ext import commands
import random

TOKEN = "ODcwMjk1MzIzNDAxMTI1OTQ4.YQKrrg.swNkHUabcy0q2nN2Yi0gUBA7YVw"

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    a = 0
    if a == 0:
        if user_message.lower() == 'hi':
            await message.channel.send(f'sup {username}')
            return
        elif user_message.lower() == 'hello':
            await message.channel.send(f'sup {username}')
            return
        elif user_message.lower() == 'sup':
            await message.channel.send(f'sup back at u, {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'fuck off wanker!')
            return
        elif user_message.lower() == 'also':
            await message.channel.send(f"also also, shut the fuck up bro no one cares, go marry tama stupid bitch")
            return

#commands
@client.command()
async def greet(ctx):
    username_cmd = str(ctx.author).split("#")[0]
    await ctx.send(f"sup {username_cmd}")

@client.command()
async def joke(ctx):
    await ctx.send("you're the joke stupid bitch")

client.run(TOKEN)