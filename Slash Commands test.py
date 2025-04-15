import discord
from discord import app_commands
from discord.ext import commands
import os
import asyncio
import datetime, time
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

client = commands.Bot(command_prefix = '%', intents=intents)

@client.event
async def on_ready():
    global startTime
    startTime = time.time()
#    os.chdir(r'C:\Users\070LE\OneDrive\Desktop\code stuff\py\MTF Unit Proccesing bot\main.py') # Not needed as VSC had a setting ticked to block py applications to access other files, this had block cogs from working but hadnt stopped the "import X from X" to not work :/ , **ONLY CHANGE THIS VVALUE IF YOU NEED IT**.
    print(" __________________________________________________________________________________________________________________")
    print(f'| Python script working directory in: {os.listdir()} |')
    print("|------------------------------------------------------------------------------------------------------------------/")
    print(f'| Logged in as {client.user} |')
    print(r'\______________________________________/')
    
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:   
        print(e)

@client.tree.command(name="ping", description="Check the bot's latency.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(client.latency * 1000)}ms!")

@client.tree.command(name="uptime", description="Tells you the bots uptime.")
async def uptime(interaction: discord.Interaction):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await interaction.response.send_message(f"Bots uptime is: {uptime}.", ephemeral=True)

#Functions

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename} is loaded. P1")
#The thing above will load all the cogs in the cogs folder, if you want to load a specific cog, just do client.load_extension("cogs.cog_name") and remove the for loop.

async def main():
    async with client:
        await load()   #cogs moment
        await client.start(TOKEN)

asyncio.run(main())