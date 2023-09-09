import discord
from discord.ext import commands
import random,requests,json
links=json.load(open('gifs.json'))
intents = discord.Intents.all()
intents.members=True
client = commands.Bot(command_prefix='!',intents=intents)
r=random.randint(1,3)

@client.event
async def on_ready():
    print("The bot is working")
    print("--------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello I am Jason")
@client.command(name="gif", aliases=["play","feed","sleep"])
async def Gif(ctx):
    await ctx.send(random.choice(links[ctx.invoked_with]))
@client.event
async def joinmember():
    channel=client.get_channel(1137023437869695037)
    await channel.send("Welcome!")
    await channel.send("https://tenor.com/view/welcome-gif-26434438")
@client.event
async def remove_member():
    channel=client.get_channel(1137023437869695037)
    await channel.send("goodbye!")
    await channel.send("https://tenor.com/search/goodbye-gifs")



client.run('MTE0ODkzNDQ5Mzk3NDA0NDc2Mg.GpdqoV.1uWqoJI2h_vothgpPJdNTOzWOBCG94cyk9b6_Y')
