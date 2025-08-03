
#Template Cog


import discord
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="ping", description="Replies with the bot's latency.")
    async def ping(self, ctx):
        latency = self.bot.latency * 1000
        await ctx.respond(f"Pong! Latency is {latency:.2f}ms")

    @discord.slash_command(name="hello", description="Say hello to the bot!")
    async def hello(self, ctx):
        await ctx.respond(f"Hello, {ctx.author.mention}!")

def setup(bot):
    bot.add_cog(Template(bot))
