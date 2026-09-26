import discord
from discord.ext import commands, tasks
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

messages = [
    "👀",
    "😂",
    "lol",
    "😭",
    "✨",
    "hahaha",
    "what",
    "nice",
    "💀",
    "🤣"
]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    if not auto_message.is_running():
        auto_message.start()


@tasks.loop(seconds=5)
async def auto_message():
    if not CHANNEL_ID:
        print("ERROR: CHANNEL_ID is missing.")
        return

    try:
        channel = bot.get_channel(int(CHANNEL_ID))

        if channel is None:
            print(f"ERROR: Cannot find channel {CHANNEL_ID}")
            return

        print(f"Sending message to #{channel.name}")
        await channel.send(random.choice(messages))
        print("Message sent successfully.")

    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")


@auto_message.before_loop
async def before_auto_message():
    await bot.wait_until_ready()


bot.run(TOKEN)
