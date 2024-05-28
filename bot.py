import atexit

import discord

from discord.ext import commands
from fluent import asyncsender as sender

description = '''test bot for adding and subtracting numbers.'''


fluentd_host = "localhost"
fluentd_port = 8080
logger = sender.FluentSender('app', host=fluentd_host, port=fluentd_port)



intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    result = left + right
    logger.emit('add operation', {'username': f"{ctx.author}", 'result': f"{result}"})
    await ctx.send(result)

@bot.command()
async def subtract(ctx, left: int, right: int):
    result = left - right
    logger.emit('subtract operation', {'username': f"{ctx.author}", 'result': f"{result}"})
    await ctx.send(result)

bot.run(token)

atexit.register(logger.close())
