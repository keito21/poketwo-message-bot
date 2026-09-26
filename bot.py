import discord
from discord.ext import commands, tasks
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")

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
    auto_message.start()

@tasks.loop(seconds=45)
async def auto_message():
    channel_id = os.getenv("CHANNEL_ID")

    if not channel_id:
        return

    channel = bot.get_channel(int(channel_id))

    if channel:
        await channel.send(random.choice(messages))

bot.run(TOKEN)
