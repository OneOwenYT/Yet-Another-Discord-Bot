from values import *
import discord
from discord.ext import commands
import datetime, time
import json
import random

numberOfLevelsInJson = 1

class Backrooms(commands.Cog):
    def __init__(self, client):
        self.client = client
        global startTime
        startTime = time.time()

    @commands.Cog.listener()
    async def on_ready(self):
        print("backrooms.py is loaded. P2")

    @commands.command()
    async def BackroomsCommands(self, ctx):
        if BackroomsCommands >= 1:
            embedVar = discord.Embed(title="Backrooms Commands:", description="Prefix: %", color=0xD90000)
            embedVar.add_field(name="RandomLevel:", value="Aliases: LuckyLevel . Gives you a random level from 0-100, plus some secret levels (if you get it your really unlucky)", inline=False)
            embedVar.add_field(name="Level:", value=f"gives you information from the official backrooms wiki. There are currently {numberOfLevelsInJson} levels documented in the command (if you'd like to help us expand our levels documentation please reach out to the maintainer of this bot!).", inline=False)
            embedVar.add_field(name="DNDCredits:", value="1", inline=False)
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("Sorry but this command is disabled.")

    @commands.command()
    async def RandomLevel(self, ctx):
        randomLevel = random.randint(0, 103)
        if randomLevel == 101:
            randomLevel = r'RUN FOR YOUR LIFE'
        elif randomLevel == 102:
            randomLevel = r'Level 666: Welcome To Hell'
        elif randomLevel == 103:
            randomLevel = r'The Frontrooms'

        ctx.send(f"Your lucky level is: {randomLevel}")

        if randomLevel < numberOfLevelsInJson:
            ctx.send("Sadly we dont have that level documented yet though, if you'd like to help us expand our levels documentation please reach out to the maintainer of this bot!")

    @commands.command()
    async def Level(self, ctx, level: str):
        try:
            level = level.lower()

            if level.isdigit():
                level = int(level)
            elif level in ("run for your life", "run"):
                level = 101
            elif level in ("welcome to hell", "level 666", "666"):
                level = 102
            elif level in ("frontrooms", "the frontrooms"):
                level = 103

            with open("data/backroomsLevels.json", "r") as f:
                backroomsLevels = json.load(f)

            level = str(level)

            if level not in backroomsLevels:
                await ctx.send("Sorry, we don't have that level documented yet.")
                return

            embedVar = discord.Embed(title=backroomsLevels[level]['name'], description=f"Classification: {backroomsLevels[level]['classification']}, Entities: {backroomsLevels[level]['entities']}.", color=0xD90000)
            embedVar.add_field(name="Description:", value=backroomsLevels[level]['description'], inline=False)
            embedVar.add_field(name="Entrances:", value=backroomsLevels[level]['entrances'], inline=False)
            embedVar.add_field(name="Exits:", value=backroomsLevels[level]['exits'], inline=False)

            numberOfExtra = int(backroomsLevels[level]['amount of embeds'])
            for embed_num in range(1, numberOfExtra + 1):
                embedVar.add_field(name="Extra Information:", value=backroomsLevels[level][f'embed {embed_num}'], inline=False)

            embedVar.set_footer(text=f"Extra: {backroomsLevels[level]['extra']}, Link: {backroomsLevels[level]['link']}.")
            await ctx.send(embed=embedVar)
        except TypeError:
            await ctx.send("Please provide a level number or name.")

    @commands.command(name='BackroomsUptime')
    async def _uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)

async def setup(client):
    await client.add_cog(Backrooms(client))