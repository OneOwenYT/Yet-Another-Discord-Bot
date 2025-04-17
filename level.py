from values import *
import discord
from discord.ext import commands
import datetime, time
import json

commandsGiveXP = 1
fixedLeveling = 1
exponetialLeveling = 0

startingLevel = 1

class Level(commands.Cog):
    def __init__(self, client):
        self.client = client
        global startTime
        startTime = time.time()

    @commands.Cog.listener()
    async def on_ready(self):
        print("level.py is loaded. P2")

    @commands.Cog.listener()
    async def on_message(self, message):
        if Leveling == 1:
            if message.author.bot:
                return
            
            if commandsGiveXP >= 1:
                if message.content.startswith("%"):
                    return

            with open("data/levelData.json", "r") as f:
                levelData = json.load(f)

            if str(message.author.id) not in levelData:
                levelData[str(message.author.id)] = {}
                levelData[str(message.author.id)]['Messages sent'] = 1
                levelData[str(message.author.id)]['Level'] = startingLevel

                with open("data/levelData.json", "w") as f:
                    json.dump(levelData, f, indent=8)

            levelData[str(message.author.id)]['Messages sent'] += 1
            messagesSent = levelData[str(message.author.id)]['Messages sent']
            currentLevel = levelData[str(message.author.id)]['Level']
    
            leveled_up = False

            if fixedLeveling >= 1 and messagesSent >= 50:
                levelData[str(message.author.id)]['Level'] += 1
                levelData[str(message.author.id)]['Messages sent'] = 0

                leveled_up = True

            if exponetialLeveling >= 1:
                if currentLevel < 10 and currentLevel >= 25:
                    currentLevelMathed = currentLevel * 5
                elif currentLevel >= 25 and currentLevel < 50:
                    currentLevelMathed = currentLevel * 10
                elif currentLevel >= 50 and currentLevel < 100:
                    currentLevelMathed = currentLevel * 10
                elif currentLevel >= 100:
                    currentLevelMathed = currentLevel * 20

                user = message.author
                if currentLevel == 1:
                    role = discord.utils.get(user.guild.roles, name="----- Level Roles -----")
                    await message.author.add_roles(role, reason=None, atomic=True)
                elif currentLevel == 10:
                    await message.author.add_roles(1359435975364710543)

                if messagesSent >= 25 + currentLevelMathed:
                    levelData[str(message.author.id)]['Level'] += 1
                    levelData[str(message.author.id)]['Messages sent'] = 0

                    leveled_up = True
            
            if leveled_up == True:
                newLevel = levelData[str(message.author.id)]['Level']
                if exponetialLeveling >= 1:
                    await message.channel.send(f"{message.author.name} has leveled up to {newLevel}! You can level up every {currentLevelMathed} messages!")
                elif fixedLeveling >= 1:
                    await message.channel.send(f"{message.author.name} has leveled up to {newLevel}! You can level up every 50 messages!")
                print(f"{message.author.name} has leveled up to {newLevel}!")


            with open("data/levelData.json", "w") as f:
                json.dump(levelData, f, indent=8)

    @commands.command(name='LevelUptime')
    async def _uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)

async def setup(client):
    await client.add_cog(Level(client))

#   TaggodonYT's leveling system code#    @commands.Cog.listener()
#    async def on_message(self, message):

#        if Leveling != 1 or message.author.bot:
#            return
#        
#        if commandsGiveXP >= 1 and message.content.startswith("%"):
#            return
#
#        with open("data/levelData.json", "r") as f:
#            levelData = json.load(f)
#
#        user_id = str(message.author.id)
#
#        if user_id not in levelData:
#            levelData[user_id] = {'Messages sent': 0, 'Level': startingLevel}
#
#        levelData[user_id]['Messages sent'] += 1
#        messagesSent = levelData[user_id]['Messages sent']
#        currentLevel = levelData[user_id]['Level']
#    
#        leveled_up = False
#
#        if fixedLeveling == 1 and messagesSent >= 50:
#            levelData[str(message.author.id)]['Level'] += 1
#            levelData[str(message.author.id)]['Messages sent'] = 0
#            leveled_up = True
#
#        elif exponetialLeveling == 1 and messagesSent >= (25 + currentLevel * 10):
#            levelData[str(message.author.id)]['Level'] += 1
#            levelData[str(message.author.id)]['Messages sent'] = 0
#            leveled_up = True
#
#        if leveled_up:
#            newLevel = levelData[str(message.author.id)]['Level']
#            channel = self.client.get_channel(1327658983976079510)
#            embedVar = discord.Embed(title=f"{message.author.name} has Leveled up!", color=0xD90000)
#            embedVar.add_field(name="New Level:", value=f"{newLevel}", inline=False)
#            embedVar.set_footer(text="Level up every 50 messages!")
#            await channel.send(embed=embedVar)
#
#
#            with open("data/levelData.json", "w") as f:
#                json.dump(levelData, f, indent=8)
#   My leveling system code

#    @commands.Cog.listener()
#    async def on_message(self, message):

#        if Leveling == 1:
#            if message.author.bot:
#                return
#            
#            if commandsForXP >= 1:
#                if message.content.startswith("%"):
#                    return
#
#            with open("data/levelData.json", "r") as f:
#                levelData = json.load(f)
#
#            if str(message.author.id) not in levelData:
#                levelData[str(message.author.id)] = {}
#                levelData[str(message.author.id)]['Messages sent'] = 1
#                levelData[str(message.author.id)]['Level'] = startingLevel
#
#                with open("data/levelData.json", "w") as f:
#                    json.dump(levelData, f, indent=8)
#
#            levelData[str(message.author.id)]['Messages sent'] += 1
#            messagesSent = levelData[str(message.author.id)]['Messages sent']
#            currentLevel = levelData[str(message.author.id)]['Level']
#    
#            if fixedLeveling == 1:
#                if messagesSent >= 50:
#                    levelData[str(message.author.id)]['Level'] += 1
#                    levelData[str(message.author.id)]['Messages sent'] = 0
#
#                    newLevel = levelData[str(message.author.id)]['Level']
#
#                    channel = self.bot.get_channel(levelChannel)
#                    embedVar = discord.Embed(title=f"{message.author.name} has Leveled up!", description="", color=0xD90000)
#                    embedVar.add_field(name="New Level:", value=f"{newLevel}", inline=False)
#                    embedVar.set_footer(text="Would you like to level up aswell? You can level up every 50 messages!", icon_url=None)
#                    await channel.send(embed=embedVar)
#
#            if exponetialLeveling == 1:
#                currentLevelMathed = currentLevel * 10
#                if messagesSent >= 25 + currentLevelMathed:
#                    levelData[str(message.author.id)]['Level'] += 1
#                    levelData[str(message.author.id)]['Messages sent'] = 0
#
#                    channel = self.bot.get_channel(levelChannel)
#                    embedVar = discord.Embed(title=f"{message.author.name} has Leveled up!", description="", color=0xD90000)
#                    embedVar.add_field(name="New Level:", value=f"{newLevel}", inline=False)
#                    embedVar.set_footer(text="Would you like to level up aswell? You can level up every 50 messages!", icon_url=None)
#                    await channel.send(embed=embedVar)
#
#
#            with open("data/levelData.json", "w") as f:
#                json.dump(levelData, f, indent=8)