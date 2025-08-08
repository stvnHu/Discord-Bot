
from pathlib import Path
from dotenv import dotenv_values
from openai import OpenAI
from discord.ext import commands
from discord import app_commands

ROOT_DIR = Path(__file__).parent.parent.parent
OPENAI_API_KEY = dotenv_values(ROOT_DIR / ".env").get("OPENAI_API_KEY")
AI = OpenAI(api_key=OPENAI_API_KEY)

class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Asks ChatGPT a question.")
    async def chatgpt(self, interaction, question: str):
        await interaction.response.defer()
        try:
            response = AI.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Keep responses under 1500 characters."},
                    {"role": "user", "content": question}
                ]
            )
            await interaction.followup.send(question + "\n\n" + response.choices[0].message.content)
        except Exception as e:
             await interaction.followup.send("Response failed.")

async def setup(bot):
    await bot.add_cog(ChatGPT(bot))
