#tamabot
#version v0.2.3 demo 15/08/2021

import discord
from discord.ext import commands
from webserver import keep_alive
import os
import random
import asyncio


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

@client.event
async def status_cycle():
    await client.wait_until_ready()
    statuses = ["a game", f"on {len(client.guilds)} servers | >help", "your mom"]
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(10)
client.loop.create_task(status_cycle())


#commands
@client.command()
async def greet(ctx):
    username_cmd = str(ctx.author).split("#")[0]
    await ctx.send(f"sup {username_cmd}")

@client.command()
async def joke(ctx):
    await ctx.send("you're the joke stupid bitch")

#hosting
keep_alive()
my_secret = os.environ['TOKEN']


client.run(my_secret)
