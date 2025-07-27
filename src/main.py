
import os
from dotenv import load_dotenv
import discord

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

COG_DIR = "./src/cogs"
cogs = [os.path.splitext(cog)[0] for cog in os.listdir(COG_DIR) if cog != "__init__.py" and cog.endswith('.py')]

bot = discord.Bot(intents=discord.Intents.default())

@bot.event
async def on_ready():
    print("Bot Ready")

def main():
    for cog in cogs:
        try:
            bot.load_extension(f"cogs.{cog}")
            print(f"Loaded {cog}")
        except Exception as e:
            print(f"Failed to load {cog}.py")

    bot.run(BOT_TOKEN)

if __name__ == "__main__":
    main()