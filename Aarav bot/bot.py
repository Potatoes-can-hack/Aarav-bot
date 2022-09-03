import discord
import random

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = 'hi', description = 'Say hello maccha')
async def hi(ctx):
    await ctx.respond('Hi da maccha da')

@bot.slash_command(name = 'about-me', description = 'My biography')
async def me(ctx):
    await ctx.respond('I am chungus\nand needs therapy\ndesperately\n...')

@bot.slash_command(name = 'bye', description = 'Say bye ')
async def me(ctx):
    await ctx.respond('Bye da maccha da')

@bot.slash_command(name = 'joke', description = 'funny')
async def me(ctx):
    await ctx.respond('Hehehehe\nFunny joke, Funny joke\n(I dont know a joke)\n...')

bot.run(TOKEN)