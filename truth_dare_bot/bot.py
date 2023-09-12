import discord
from discord.ext import commands
import random
#Enter your bot token as a string
bot_token=''
truths=[]
dares=[]
data=open('data.txt')
for line in data:
    arr=line.split(':')
    if arr[0]=='Truth' or arr[0]=='truth':
        truths.append(arr[1].strip())
    else:
        dares.append(arr[1].strip())
count1=0
count2=0
for i in truths:
    count1+=1
for i in dares:
    count2+=1
intents=discord.Intents.default()
intents.members=True
intents.message_content=True
mybot=commands.Bot(command_prefix='$',intents=intents)
@mybot.event
async def on_ready():
    print("I am ready! ")
@mybot.command()
async def aid(ctx):
    await ctx.send('''Here are a list of commands
1.$aid-           you just invoked this command.
2.$t or $truth-   to play truth or dare by generating a truth question.
3.$d or $dare-    to play truth or dare by generating a dare question.
4.$truth or dare- to play truth or dare by either generating a truth or dare question.''')
@mybot.command()
async def truth(ctx,arg1='',arg2=''):
    if arg1=='or' and arg2=='dare':
        r=random.randint(-1,2)
        if r==0:
            i=random.randint(-1,count1)
            mes=truths[i]
            await ctx.send(mes)
        else:
           i=random.randint(-1,count2)
           mes=dares[i]
           await ctx.send(mes) 
    elif arg1=='' and arg2=='':
        i=random.randint(-1,count1)
        mes=truths[i]
        await ctx.send(mes) 
    else:
        pass
@mybot.command()
async def dare(ctx):
    i=random.randint(-1,count2)
    mes=dares[i]
    await ctx.send(mes) 
@mybot.command()
async def t(ctx):
    i=random.randint(-1,count1)
    mes=truths[i]
    await ctx.send(mes) 
@mybot.command()
async def d(ctx):
    i=random.randint(-1,count2)
    mes=dares[i]
    await ctx.send(mes)
mybot.run(bot_token)
