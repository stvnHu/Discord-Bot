
#Template Cog


from discord.ext import commands
from discord import app_commands

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(description="Replies with a greeting.")
    async def hello(self, interaction):
        await interaction.response.send_message(f"Hello, {interaction.user}!")

    @app_commands.command(description="Replies with the bot's latency.")
    async def ping(self, interaction):
        latency = self.bot.latency * 1000
        await interaction.response.send_message(f"Latency: {latency:.2f}ms")

async def setup(bot):
    await bot.add_cog(Template(bot))
