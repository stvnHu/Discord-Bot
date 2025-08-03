
from pathlib import Path
from dotenv import dotenv_values
import discord

ROOT_DIR = Path(__file__).parent.parent
COG_DIR = ROOT_DIR / "src" / "cogs"
cogs = [cog.stem for cog in COG_DIR.iterdir() if cog.suffix == ".py" and cog.stem != "__init__"]

BOT_TOKEN = dotenv_values(ROOT_DIR / ".env").get("BOT_TOKEN")
bot = discord.Bot(intents=discord.Intents.default())

@bot.event
async def on_ready():
    print("Bot Ready")

def main():
    for cog in cogs:
        try:
            bot.load_extension(f"cogs.{cog}")
            print(f"Loaded {cog}.py")
        except Exception as e:
            print(f"Failed to load {cog}.py")

    bot.run(BOT_TOKEN)

if __name__ == "__main__":
    main()
