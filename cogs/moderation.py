from values import *
import discord
from discord.ext import commands
import datetime, time
import json


class MOD(commands.Cog):
    def __init__(self, client):
        self.client = client
        global startTime
        startTime = time.time()

    @commands.Cog.listener()
    async def on_ready(self):
        print("moderation.py is loaded. P2")

    @commands.command()
    async def Warn(self, ctx, userID : int, *, reason):
        with open("data/moderationData.json", "r") as f:
            moderationData = json.load(f)

        if str(userID) not in moderationData:
            moderationData[str(userID)] = {}
            moderationData[str(userID)]['Warns'] = 0
            moderationData[str(userID)]['Warn 1'] = "Empty"
            moderationData[str(userID)]['Warn 2'] = "Empty"
            moderationData[str(userID)]['Warn 3'] = "Empty"
            moderationData[str(userID)]['Messages sent'] = 0
            moderationData[str(userID)]['Commands sent'] = 0

            with open("data/moderationData.json", "w") as f:
                json.dump(moderationData, f, indent=8)

        moderationData[str(userID)]['Warns'] += 1

        if moderationData[str(userID)]['Warn 1'] == "Empty":
            moderationData[str(userID)]['Warn 1'] == reason
        elif moderationData[str(userID)]['Warn 2'] == "Empty":
            moderationData[str(userID)]['Warn 2'] == reason
        elif moderationData[str(userID)]['Warn 3'] == "Empty":
            moderationData[str(userID)]['Warn 3'] == reason
        else:
            await ctx.send("User has already been warned 3 times.")
            return

        with open("data/moderationData.json", "w") as f:
            json.dump(moderationData, f, indent=8)

    @commands.command()
    async def RemoveWarn(self, ctx, userID : int, warnNumber : int):
        with open("data/moderationData.json", "r") as f:
            moderationData = json.load(f)

        if str(userID) not in moderationData:
            moderationData[str(userID)] = {}
            moderationData[str(userID)]['Warns'] = 0
            moderationData[str(userID)]['Warn 1'] = "Empty"
            moderationData[str(userID)]['Warn 2'] = "Empty"
            moderationData[str(userID)]['Warn 3'] = "Empty"
            moderationData[str(userID)]['Messages sent'] = 0
            moderationData[str(userID)]['Commands sent'] = 0

            with open("data/moderationData.json", "w") as f:
                json.dump(moderationData, f, indent=8)

        if moderationData[str(userID)]['Warns'] > 0:
            moderationData[str(userID)]['Warns'] -= 1
        else:
            await ctx.send("User has no warns.")
            return

        if warnNumber == 1:
            moderationData[str(userID)]['Warn 1'] == "Empty"
        elif warnNumber == 2:
            moderationData[str(userID)]['Warn 2'] == "Empty"
        elif warnNumber == 3:
            moderationData[str(userID)]['Warn 3'] == "Empty"
        else:
            await ctx.send("User has already been warned 3 times.")
            return

        with open("data/moderationData.json", "w") as f:
            json.dump(moderationData, f, indent=8)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.startswith("%"):
            messageIsCommand = True
        else:
            messageIsCommand = False

        with open("data/moderationData.json", "r") as f:
            moderationData = json.load(f)

        if str(message.author.id) not in moderationData:
            moderationData[str(message.author.id)] = {}
            moderationData[str(message.author.id)]['Warns'] = 0
            moderationData[str(message.author.id)]['Warn 1'] = "Empty"
            moderationData[str(message.author.id)]['Warn 2'] = "Empty"
            moderationData[str(message.author.id)]['Warn 3'] = "Empty"
            moderationData[str(message.author.id)]['Messages sent'] = 0
            moderationData[str(message.author.id)]['Commands sent'] = 0

            with open("data/moderationData.json", "w") as f:
                json.dump(moderationData, f, indent=8)

        if messageIsCommand == True:
            moderationData[str(message.author.id)]['Commands sent'] += 1
        elif messageIsCommand == False:
            moderationData[str(message.author.id)]['Messages sent'] += 1

        with open("data/moderationData.json", "w") as f:
            json.dump(moderationData, f, indent=8)

    @commands.command(name='ModerationUptime')
    async def _uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)

async def setup(client):
    await client.add_cog(MOD(client))