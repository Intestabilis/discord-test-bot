import discord
from discord.ext import commands
import random

description = '''test bot for adding numbers.'''

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    "Adds two numbers together."
    await ctx.send(left + right)



bot.run(token)
