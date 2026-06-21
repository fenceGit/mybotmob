import discord
from discord.ext import commands
import os
from command import ping, channel_add, embed
from mod import mute, unmute
import json
with open("badwords.json", "r") as f:
    data = json.load(f)
    badwords = data["bad_words"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.tree.add_command(ping)
bot.tree.add_command(channel_add)
bot.tree.add_command(mute)
bot.tree.add_command(unmute)
bot.tree.add_command(embed)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")
    print("Slash commands synced.")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if any(word in message.content.lower() for word in badwords):
        await message.delete()
        await message.channel.send("Mind your language! cussing is bad >:(")
return
    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))
