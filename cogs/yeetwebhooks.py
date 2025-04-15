from values import *
import discord
from discord.ext import commands
import datetime, time

class YeetWebhooks(commands.Cog):
    def __init__(self, client):
        self.client = client
        global startTime
        startTime = time.time()

    @commands.Cog.listener()
    async def on_ready(self):
        print("yeetwebhooks.py is loaded. P2")

    @commands.command()
    @commands.has_any_role(1357177872548368505)
    async def DeleteWebhooks(self, ctx):
        guild = ctx.guild
        webhooks = await guild.webhooks()
        for webhook in webhooks:
            try:
                await webhook.delete()
            except discord.Forbidden:
                await ctx.send(f"Permission denied to delete webhook: {webhook.name}.")
                print(f"Permission denied to delete webhook: {webhook.name} in guild: {guild.name}.")
            except discord.HTTPException as e:
                await ctx.send(f"Failed to delete webhook: {webhook.name}.")
                print(f"Failed to delete webhook: {webhook.name} in guild: {guild.name}: {e}")

    @commands.command(name='yeetwebhooksUptime')
    async def _uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)


async def setup(client):
    await client.add_cog(YeetWebhooks(client))