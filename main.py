from values import *
#Imports values needed for information and to tell whether not to run certain commands

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
#Imports the token from the .env file, since its a .env file it will not be uploaded to github and stuff like that, you could just put your token in the token area at the bottom but its not reccomended

import discord
from discord import app_commands
from discord.ext import commands
import requests
import asyncio
import datetime, time
import json
import random

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

    while statsInStatus:
        await client.change_presence(activity=discord.Game(f"latency is {round(client.latency * 1000)}ms."))
        await asyncio.sleep(10)
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await client.change_presence(activity=discord.Game(f"Bot uptime: {uptime}."))
        await asyncio.sleep(10)
        
    while fakeCryptoPriceChange == 1:
            with open("data/ecoData2.json", "r") as f:
                userEco = json.load(f)

            if FakeCryptoPrice is None:
                FakeCryptoPrice = FakeCryptoPrice

            if FakeCryptoPrice not in userEco:
                userEco[FakeCryptoPrice] = {}
                userEco[FakeCryptoPrice]['Balance'] = fakeCryptoPrice2

                with open("data/ecoData2.json", "w") as f:
                    json.dump(userEco, f, indent=8)

            curentPrice = userEco[FakeCryptoPrice]['Price']
            channel = client.get_channel(messageLoggingChannel)
            await channel.send(f"Fake Crypto Price changed to:{curentPrice}.")
            
            await asyncio.sleep(10)


#Settings are in "values.py"

@client.command()
async def DebugCommands(ctx):
    embedVar = discord.Embed(title="Debug Commands:", description="Prefix: %", color=0xD90000)
    embedVar.add_field(name="Debug Commands:", value="Requires Administrator permissions to use.", inline=False)
    embedVar.add_field(name="Values:", value="Returns the common values of the bot.", inline=False)
    embedVar.add_field(name="DebugMode:", value="Toggles the debugMode of the bot, 1 = on, 0 = off.", inline=False)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def Values(ctx):
    if debugMode >= 1:
        await ctx.send(f"latency is {round(client.latency * 1000)}ms, CMD Values: debugMode:{debugMode}, spamCommand:{spamCommand}, pingCommand:{pingCommand}, giveRoleCommand:{giveRoleCommand}, purgeCommand:{purgeCommand}, jokeCommand:{jokeCommand}, joinAndleaveEvent:{joinAndleaveEvent}, printLatencyAuto:{printLatencyAuto}, timePerAutoPrintBotLatency:{timePerAutoPrintBotLatency}, printBotLatencyOnCommandUse:{printBotLatencyOnCommandUse}, maxPurgeAmount:{maxPurgeAmount}, maxSpamCommandAmount:{maxSpamCommandAmount}, returnMessageAfterPurge:{returnMessageAfterPurge}, requiredRoleIdForRoleCommand:{requiredRoleIdForRoleCommand}, jokeURL:{jokeURL}, logging:{commandLogging}, sendData:{sendData}, logData:{logData}, welcomeChannel:{welcomeChannel}, errorLogging:{errorLogging}, commandLogging:{commandLogging}, printLatencyAuto:{printLatencyAuto}, timePerAutoPrintBotLatency:{timePerAutoPrintBotLatency}, printBotLatencyOnCommandUse:{printBotLatencyOnCommandUse}, errorLoggingChannel:{errorLoggingChannel}, commandLoggingChannel:{commandLoggingChannel}.")
    else:
        await ctx.send("debugMode is currently off.")

@client.command()
@commands.has_permissions(administrator=True)
async def Status(ctx, Text : str):
    if debugMode >= 1:
        game = discord.Game(f"{Text}")
        await client.change_presence(status=discord.Status.idle, activity=game)
    else:
        await ctx.send("debugMode is currently off.")


@client.command(aliases=["WhereIsHe", "WIH", "OmniMan", "OMNIMAN","Omni-Man", "OMNI-MAN"])
async def WHEREISHE(ctx):
    if debugMode >= 1:
        if ctx.voice_client:
            voice_client = ctx.voice_client

            source = discord.FFmpegPCMAudio(source=r"sounds\WHERE IS HE.mp3")

            voice_client.play(source)

        await ctx.send("WHERE IS HE")
        await asyncio.sleep(1)
        await ctx.send("WHERE IS OMNI-MAN")
        await asyncio.sleep(1)
        await ctx.send("AHHHHHHHHHHHHHHHHHHHH")
        await asyncio.sleep(2)
        await ctx.send("WHERE IS HE")
        await asyncio.sleep(1)
        await ctx.send("WHERE IS OMNI-MAN")
        await asyncio.sleep(1)
        await ctx.send("WHERE IS OMNI-MAN")
        await asyncio.sleep(1)
        await ctx.send("WHERE IS HE")
        await asyncio.sleep(1.5)
        await ctx.send("AHHHHHHHHHHHHHHHHHHHH")
        await asyncio.sleep(1)
        await ctx.send("WHERE IS OMNI-MAN")
        await asyncio.sleep(1.25)
        await ctx.send("AHHHHHHHHHHHHHHHHHHHH")
        await ctx.send("**kirby falling gif sfx**")
        await ctx.send("https://tenor.com/view/fall-kirby-drop-falling-deep-gif-17081698")
    else:
        await ctx.send("debugMode is currently off.")

@client.command(aliases=["AYS"])
async def AreYouSure(ctx):
    if debugMode >= 1:
        await ctx.send("Are you sure?")

        if ctx.voice_client:
            voice_client = ctx.voice_client

            source = discord.FFmpegPCMAudio(source=r"sounds\Sure.mp3")

            voice_client.play(source)
    else:
        await ctx.send("debugMode is currently off.")

@client.command()
@commands.has_permissions(administrator=True)
async def DebugMode(ctx, trueORfalse: int):
    global debugMode
    if ableToToggleDebugMode >= 1:
        if trueORfalse >= 1:
            debugMode = 1
            await ctx.send(f"debugMode set to:{debugMode}")
        else:
            debugMode = 0
            await ctx.send(f"debugMode set to:{debugMode}")

#Commands
#TO ADD: Command for sector HQ to give strikes, moderation commands for staff, and other things ig.

@client.command()
async def Commands(ctx):
    embedVar = discord.Embed(title="Commands:", description="Prefix: %", color=0xD90000)
    embedVar.add_field(name="General Commands:", value="Requires no permissions to use.", inline=False)
    embedVar.add_field(name="Credits:", value="Returns the info for the credits of the bot.", inline=False)
    embedVar.add_field(name="Ping:", value="Returns the ping of the bot.", inline=False)
    embedVar.add_field(name="Data:", value="Returns the Uptime, amount of Commands used, amount of Events used, and amount of Errors logged.", inline=False)
    embedVar.add_field(name="Joke:", value="Tells you a joke.", inline=False)
    embedVar.add_field(name="Join:", value="Joins the current VC the user who used the command.", inline=False)
    embedVar.add_field(name="Leave:", value="If the bot is inside of a VC it will leave the VC.", inline=False)
    embedVar.add_field(name="Play:", value="Plays a mp3 file LINKED (it must be linked not just attached).", inline=False)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def Data(ctx):
    if sendData >= 1:
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        print(f"Uptime:{uptime}, commands used:{commandsUsed}, Events used:{eventsUsed}, Errors logged:{errorsLogged}.")
        embedVar = discord.Embed(title="Data:", description="The Data of the bot currently.", color=0xD90000)
        embedVar.add_field(name="Uptime:", value=f"{uptime}", inline=False)
        embedVar.add_field(name="Commands used:", value=f"{commandsUsed}", inline=False)
        embedVar.add_field(name="events used:", value=f"{eventsUsed}", inline=False)
        embedVar.add_field(name="Errors ocurred:", value=f"{errorsLogged}", inline=False)
        embedVar.add_field(name="Bot messages sent:", value=f"{botMessagesSent}", inline=False)
        await ctx.send(embed=embedVar)
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_permissions(administrator=True)
async def AdminData(ctx):
    if sendData >= 1:
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        print(f"Uptime:{uptime}, commands used:{commandsUsed}, Events used:{eventsUsed}, Errors logged:{errorsLogged}.")
        embedVar = discord.Embed(title="Data:", description="The Data of the bot currently.", color=0xD90000)
        embedVar.add_field(name="Uptime:", value=f"{uptime}", inline=False)
        embedVar.add_field(name="Commands used:", value=f"{commandsUsed}", inline=False)
        embedVar.add_field(name="events used:", value=f"{eventsUsed}", inline=False)
        embedVar.add_field(name="Errors ocurred:", value=f"{errorsLogged}", inline=False)
        embedVar.add_field(name="Bot messages sent:", value=f"{botMessagesSent}", inline=False)
        embedVar.add_field(name="Messages sent:", value=f"{messagesSent}", inline=False)
        embedVar.add_field(name="Messages edited:", value=f"{messagesEdited}", inline=False)
        embedVar.add_field(name="Messages deleted:", value=f"{messagesDeleted}", inline=False)
        await ctx.send(embed=embedVar)
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
async def Credits(ctx):
    embedVar = discord.Embed(title="Credits:", description="These are the credits for the commands or ideas for the server/bot.", color=0xD90000)
    embedVar.add_field(name="[TagGodOnYT](https://www.youtube.com/channel/UCXhjSFf8Sl7SyspA-WwyN6g):", value="Made the GiveRole Command, and helped with the leveling system.", inline=False)
    embedVar.add_field(name="Beg, Work, Balance Commands:", value="[Paradoxial](https://www.youtube.com/watch?v=1PkkwPVa0D4) (OneOwen has modified the code for it slightly aswell)", inline=False)
    embedVar.add_field(name="All other commands:", value="[OneOwen](https://www.youtube.com/@oneowen)", inline=False)
    embedVar.add_field(name='Sloote1 "Slot Machine":', value='Came up with the idea for the "SpamPing" command.', inline=False)
    embedVar.add_field(name='axol_32:', value='Reccomended adding voice related commands.', inline=False)
    embedVar.add_field(name="Stack Overflow community:", value='Credit for being amazing people who are willing to help new people and everyone else in the community.', inline=False)
    embedVar.add_field(name="Discord.py docs:", value='Credit for being an amazing rescource along the way while learning python.', inline=False)
    await ctx.send(embed=embedVar)

@client.command()
async def Ping(ctx):
    if pingCommand >= 1:
        await ctx.send(f"Pong! In {round(client.latency * 1000)}ms.")
    else:
        await ctx.send("Sorry but this command is disabled.")

#Fun commands

@client.command()
async def Join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()

        await ctx.send("Connected!")

        randomNumber = random.randint(1, 10)
        if randomNumber == 1:
            voice_client = ctx.voice_client

            source = discord.FFmpegPCMAudio(source="sounds/connected.mp3")

            voice_client.play(source)
    else:
        await ctx.send("You are not in a voice channel.")

@client.command(aliases=["Disconnect", "Dc", "DC"])
async def Leave(ctx):
    randomNumber = random.randint(1, 10)
    if randomNumber == 1:
        voice_client = ctx.voice_client

        source = discord.FFmpegPCMAudio(source="sounds/sure.mp3")

        voice_client.play(source)

    await ctx.voice_client.disconnect()
    await ctx.send("Disconnected!")

@client.command()
async def Play(ctx, url):
    if ctx.voice_client:
        voice_client = ctx.voice_client

        source = discord.FFmpegPCMAudio(source=url)

        voice_client.play(source)

        await ctx.send("Playing!")
    else:
        await ctx.send("I am not in a voice channel.")

@client.command()
async def Roll(ctx, MaxNumber : int):
    if funCommands >= 1:
        await ctx.send(f"You rolled a {str(random.randint(1, MaxNumber))}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
async def Joke(ctx):
    if funCommands >= 1:
        if jokeCommand >= 1:
            try:
                response = requests.get(jokeURL)
                json.loads(response.text)

                await ctx.send(json.loads(response.text)['joke'])
                print("Joke Command used:" + json.loads(response.text)['joke'])
            except:
                await ctx.send("An error has occured, this may be with the web service used by the joke command, please try again later.")
        else:
            await ctx.send("Sorry but this command is disabled.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329049007498072125)
async def SpamPing(ctx, amount : int, UserID : int):
    if funCommands >= 1:
        if spamPingCommand >= 1:
            try:
                if amount > maxSpamCommandAmount:
                    amount = maxSpamCommandAmount
                count = 0
                while count < amount:
                    await ctx.send(f"This is a spam ping <@{UserID}> .")
                    count += 1
                print(f"{ctx.author} has used the Spam Ping command to ping {UserID} {amount} times in {ctx.channel}.")
            except:
                await ctx.send("Please provide a valid UserID.")
        else:
            await ctx.send("Sorry but this command is disabled.")

#Moderation commands

@client.command()
@commands.has_any_role(moderationRole1, moderationRole2, moderationRole3)
async def ModerationCommands(ctx):
    embedVar = discord.Embed(title="Moderation Commands:", description="Prefix: %", color=0xD90000)
    embedVar.add_field(name="Moderation Commands:", value="Requires different permissions per command to use.", inline=False)
    embedVar.add_field(name="GiveRole:", value="Gives specified user the role specified, example: %GiveRole <@676956811659575297> <@&1216315296080597073>. Requires administrator.", inline=False)
    embedVar.add_field(name="Purge:", value="Purged specified number of message in the channel its used in, limit of 50 messages. Requires manage_messages.", inline=False)
    embedVar.add_field(name="ChannelPurge:", value="Purged specified number of message in the channel its specified, example: %ChannelPurge 25 1293195064142598247, limit of 50 messages. Requires manage_messages.", inline=False)
    embedVar.add_field(name="Spam:", value="Spams specified amount of messages (only used for testing stuff). Requires administrator.", inline=False)
    embedVar.add_field(name="AdminData:", value="Sends out 3 seperate values from the original command, those values are: Messages sent, Messages edited, Messages deleted. Requires administrator.", inline=False)
    embedVar.add_field(name="Toggle:", value="Use Toggle[command name] to toggles specified commands, examples: %ToggleSpam %ToggleJoke %TogglePurge (both purge and channel purge will be toggled). Requires administrator.", inline=False)
    await ctx.send(embed=embedVar)

@client.command(pass_context=True)
async def GiveRole(ctx, member: discord.Member, role: discord.Role):
    if giveRoleCommand >= 1:
        if requiredRoleIdForRoleCommand not in [role.id for role in ctx.author.roles]:
            await ctx.send(f"You need the role with ID {requiredRoleIdForRoleCommand} to use this command.")
            return
        if role in member.roles:
            await ctx.send(f"{member.mention} already has the '{role.name}' role.")
            return
        await member.add_roles(role)
        await ctx.send(f"Successfully given the '{role.name}' role to {member.mention}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_permissions(manage_messages=True)
async def Purge(ctx, amount : int):
    if purgeCommand >= 1:
        if amount < 1:
            await ctx.send("You must delete at least one message.")
            return
        if amount > maxPurgeAmount:
            amount = maxPurgeAmount
        await ctx.channel.purge(limit= amount + 1) #the +1 autocorrects for the users message who sent it
        print(f"{ctx.author} used the purge command in {ctx.channel}.")
        if returnMessageAfterPurge >= 1:
            await ctx.send(f"{amount} message(s) purged")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_permissions(manage_messages=True)
async def ChannelPurge(ctx, amount : int, channelid : int):
    if purgeCommand >= 1:
        if amount < 1:
            await ctx.send("You must delete at least one message.")
            return
        if amount > maxPurgeAmount:
            amount = maxPurgeAmount
        channel = client.get_channel(channelid)
        await channel.purge()
        print(f"{ctx.author} used the purge command in {channel}.")
        if returnMessageAfterPurge >= 1:
            await ctx.send(f"{amount} message(s) purged")

@client.command()
@commands.has_any_role(1329048939831234561, 1216315296080597073)
async def Spam(ctx, amount : int):
    if spamCommand >= 1:
        if amount > maxSpamCommandAmount:
            amount = maxSpamCommandAmount
        count = 0
        while count < amount:
            await ctx.send("This is a spam message.")
            count += 1
        print(f"{ctx.author} has used the Spam command {amount} times in {ctx.channel}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

#Toggle Commands

@client.command()
@commands.has_any_role(1329048939831234561)
async def ToggleCog(ctx, yesOrNo: int, cogName: str):
    if yesOrNo >= 1:
        try:
            client.load_extension(f"cogs.{cogName}")
            await ctx.send("Cog is loaded")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found")
    elif yesOrNo == 0:
        try:
            client.unload_extension(f"cogs.{cogName}")
            await ctx.send(f"{cogName} is unloaded")
        except commands.ExtensionNotFound:
            await ctx.send(f"{cogName} not found.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def ToggleSpam(ctx):
    global spamCommand
    if toggleCommands >= 1:
        if spamCommand >= 1:
            spamCommand = 0
            await ctx.send(f"Spam cmd is: {spamCommand}.")
        else:
            spamCommand = 1
            await ctx.send(f"Spam cmd is: {spamCommand}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def ToggleSpamPing(ctx):
    global spamCommand
    if toggleCommands >= 1:
        if spamPingCommand >= 1:
            spamPingCommand = 0
            await ctx.send(f"Spam cmd is: {spamPingCommand}.")
        else:
            spamPingCommand = 1
            await ctx.send(f"Spam cmd is: {spamPingCommand}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def TogglePing(ctx):
    global pingCommand
    if toggleCommands >= 1:
        if pingCommand >= 1:
            pingCommand = 0
            await ctx.send(f"Ping cmd is: {pingCommand}.")
        else:
            pingCommand = 1
            await ctx.send(f"Ping cmd is: {pingCommand}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def ToggleGiveRole(ctx):
    global giveRoleCommand
    if toggleCommands >= 1:
        if giveRoleCommand >= 1:
            giveRoleCommand = 0
            await ctx.send(f"GiveRole cmd is: {giveRoleCommand}.")
        else:
            giveRoleCommand = 1
            await ctx.send(f"GiveRole cmd is: {giveRoleCommand}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def TogglePurge(ctx):
    global purgeCommand
    if toggleCommands >= 1:
        if purgeCommand >= 1:
            purgeCommand = 0
            await ctx.send(f"Purge cmd is: {purgeCommand}.")
        else:
            purgeCommand = 1
            await ctx.send(f"Purge cmd is: {purgeCommand}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def ToggleJoke(ctx):
    global purgeCommand
    if toggleCommands >= 1:
        if jokeCommand >= 1:
            jokeCommand = 0
            await ctx.send(f"Joke cmd is: {jokeCommand}.")
        else:
            jokeCommand = 1
            await ctx.send(f"Joke cmd is: {jokeCommand}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def ToggleJoinAndLeave(ctx):
    global joinAndleaveEvent
    if toggleCommands >= 1:
        if joinAndleaveEvent >= 1:
            joinAndleaveEvent = 0
            await ctx.send(f"joinAndLeave event is: {joinAndleaveEvent}.")
        else:
            joinAndleaveEvent = 1
            await ctx.send(f"koinAndLeave event is: {joinAndleaveEvent}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def ToggleCommandLogging(ctx):
    global commandLogging
    if commandLogging >= 1:
        if commandLogging >= 1:
            commandLogging = 0
            await ctx.send(f"commandLogging event is: {commandLogging}.")
        else:
            commandLogging = 1
            await ctx.send(f"commandLogging event is: {commandLogging}.")
    else:
        await ctx.send("Sorry but this command is disabled.")

@client.command()
@commands.has_any_role(1329048939831234561)
async def ToggleErrorLogging(ctx):
    global errorLogging
    if errorLogging >= 1:
        if errorLogging >= 1:
            errorLogging = 0
            await ctx.send(f"errorLogging event is: {errorLogging}.")
        else:
            errorLogging = 1
            await ctx.send(f"errorLogging event is: {errorLogging}.")
    else:
        await ctx.send("Sorry but this command is disabled.")



#Disabled Commands

#N/A

#Events

sendData  = 1       #Used for logging errors, bot messages, messages sent, commands used, and events used (must have logData and sendData active)
logData =  1        #Used for logging errors, bot messages, messages sent, commands used, and events used (must have logData and sendData active)
errorsLogged = 0    #Used for logging errors (must have logData and sendData active)
commandsUsed = 0    #Used for logging commands used (must have logData and sendData active)
eventsUsed = 0      #Used for logging events used (must have logData and sendData active)
messagesSent = 0    #Used for logging messages sent (must have logData and sendData active)
botMessagesSent = 0 #Used for logging bot messages sent (must have logData and sendData active)
messagesEdited = 0  #Used for logging messages edited (must have logData and sendData active)
messagesDeleted = 0 #Used for logging messages deleted (must have logData and sendData active)

@client.event
async def on_member_join(member):
    global eventsUsed
    if logData >= 1:
        eventsUsed += 1
    
    if joinAndleaveEvent >= 1:
        channel = client.get_channel(1293470642057773156)
        await channel.send(f"{member.mention} has joined the server")
    
    if printBotLatencyOnCommandUse >= 1:
        print(f"Event used, latency is {round(client.latency * 1000)}ms")

@client.event
async def on_member_remove(member):
    global eventsUsed
    if logData >= 1:
        eventsUsed += 1
    
    if joinAndleaveEvent >= 1:
        channel = client.get_channel(1293470642057773156)       
        await channel.send(f"{member.mention} has left the server")   
    
    if printBotLatencyOnCommandUse >= 1:
        print(f"Event used, latency is {round(client.latency * 1000)}ms")

@client.event
async def on_command(ctx):
    global commandsUsed
    global eventsUsed
    if commandLogging >= 1:
        channel = client.get_channel(commandLoggingChannel)
        await channel.send(f"Command '{ctx.command}' was used by '{ctx.author}' in '{ctx.channel}', ctx:{ctx}")
        print(f"Command '{ctx.command}' was used by '{ctx.author}' in '{ctx.channel}'")

    if logData >= 1:
        commandsUsed += 1
        eventsUsed += 1
        
    if printBotLatencyOnCommandUse >= 1:
        print(f"Event used, latency is {round(client.latency * 1000)}ms")

@client.event
async def on_command_error(ctx, error):
    global errorsLogged
    global eventsUsed
    if errorLogging >= 1:
        channel = client.get_channel(errorLoggingChannel)
        await channel.send(f"Command Error:{error}, ctx: Channel:{ctx.channel}, User:{ctx.author}, Command:{ctx.command}.")
        print(f"Command Error:{error}, Channel:{ctx.channel}, User:{ctx.author}, Command:{ctx.command}.")
    await ctx.send(f"Error:{error}, An error with command:{ctx.command} has ocured, please refer to the commands guide or ask for assistance.")

    if error == r'ClientException: Already playing audio.':
        ctx.send("I am already playing audio.")
    elif error == r"You are missing at least one of the required roles: '1329048939831234561'":
        ctx.send("You are missing the Toggle Perms role.")
    elif error == r"You are missing at least one of the required roles: '1329049007498072125'":
        ctx.send("You are missing the Extra Bot Perms role.")
    elif error == r"You are missing at least one of the required roles: '1357177872548368505'":
        ctx.send("You are missing the Admin Bot Perms role.")

    if logData >= 1:
        errorsLogged += 1
        eventsUsed += 1

@client.event
async def on_message(message):
    global botMessagesSent
    global eventsUsed
    global messagesSent

    randomNumber = random.randint(1, 100)
    if randomNumber == 1:
        for role in message.author.roles:
            if role.id == 1357170267301875853:
                await message.channel.send(f"<@{message.author.id}> is a poop nugget. :P")
                print(f"{message.author} is a poop nugget. :P")
    randomNumber2 = random.randint(1, 10)
    if randomNumber2 == 1:
        for role in message.author.roles:
            if role.id == 1357172046412386314:
                await message.channel.send(f"<@{message.author.id}> is a big ol' poop brick. :P")
                print(f"{message.author} is a poop brick. :P")
    randomNumber3 = random.randint(1, 100)
    if randomNumber3 == 1:
        for role in message.author.roles:
            if role.id == 1357180518126321864:
                await message.channel.send("Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy.")
                await message.channel.send("Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy.")
                await message.channel.send("Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy.")
                print(f"{message.author} is a rat.")
    
    if logData >= 1:
        if message.author == client.user:
            botMessagesSent += 1
            return
        eventsUsed += 1
        messagesSent += 1

    await client.process_commands(message)


@client.event
async def on_message_edit(before, after):
    global eventsUsed
    global messagesEdited
    if messageEditLogging >= 1:
        channel = client.get_channel(messageLoggingChannel)
        await channel.send(f"<@{after.author.id}>/{after.author} edited a message, Before:{before.content}, After:{after.content}.")
        embedVar = discord.Embed(title=f"<@{after.author.id}> edited a message", description="", color=0xD90000)
        embedVar.add_field(name=f"Before:{before.content}, After:{after.content},", value="", inline=False)
        await channel.send(embed=embedVar)

    if logData >= 1:
        eventsUsed += 1
        messagesEdited += 1

@client.event
async def on_message_delete(message):
    global eventsUsed
    global messagesDeleted
    if messageEditLogging >= 1:
        channel = client.get_channel(messageLoggingChannel)
        await channel.send(f"<@{message.author.id}>/{message.author} deleted a message, message delted:{message.content}.")
        embedVar = discord.Embed(title=f"<@{message.author.id}> deleted a message", description="", color=0xD90000)
        embedVar.add_field(name=f"Message content {message.content}", value="", inline=False)
        await channel.send(embed=embedVar)

    if logData >= 1:
        eventsUsed += 1
        messagesDeleted += 1


#Functions

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename} is loaded. P1")
#cogs moment

async def main():
    async with client:
        await load()   #cogs moment
        await client.start(TOKEN)

asyncio.run(main())