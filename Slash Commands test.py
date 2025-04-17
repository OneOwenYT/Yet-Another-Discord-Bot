import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import datetime, time

# .ENV FILES SEEM MESSED UP/BROKEN FOR ME, IF YOU KNOW HOW TO FIX IT PLEASE MESSAGE ME
import os #needed for the os.getenv() function to work and the on_ready event's 2nd print thing to work
#from dotenv import load_dotenv
#load_dotenv()
#TOKEN = os.getenv('DISCORD_BOT_TOKEN')
#print(f"Token is: {TOKEN}")
#Imports the token from the .env file, since its a .env file it will not be uploaded to github and stuff like that, you could just put your token in the token area at the bottom but its not reccomended

from KEYS import *
#Imports important keys

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
    print(" ____________________________________________________________________________________________________________________________________________")
    print(f'| Python script working directory in: {os.listdir()} |')
    print("|--------------------------------------------------------------------------------------------------------------------------------------------/")
    print(f'| Logged in as {client.user} |')
    print(r'\______________________________________/')
    
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:   
        print(e)

@client.tree.command(name="ping", description="Check the bot's latency.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(client.latency * 1000)}ms!", ephemeral=True)

@client.tree.command(name="test", description="Tests to see if the bot can send a message in the channel the command was sent in.")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("This is a test to see if this bot can send messages here!")

@client.tree.command(name="badpermsinfo", description="Tests to see if the bot can send a message in the channel the command was sent in.")
async def badperms(interaction: discord.Interaction):
    await interaction.response.send_message("This is a message to inform you that users have the permission for USE_EXTERNAL_APPS, this allowers users like me to use apps like this! Its reccomended to remove this permission and only let trusted members use this as it can be used to send messages that you may not want, those messages could involve raiding stuff, pings, and other generally bad things, if you want to remove this permission, go to your server settings, then roles, then the role that has this permission, and remove it from there! This was automatically turned on because discord doesnt really tell you about when they add new features that may be harmful.")

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