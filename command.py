import discord
import os
from discord.ext import commands
import random
from discord import app_commands
from discord import Interaction


@app_commands.command(name="ping", description="This does nothing but say pong")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message("pong")

@app_commands.command(name="channel_add", description="creates a channel")
@app_commands.default_permissions(manage_channels=True)
@app_commands.describe(channel_name="name of the channel")
async def channel_add(interaction: discord.Interaction, channel_name: str):
  guild = interaction.guild
  await guild.create_text_channel(channel_name)
  await interaction.response.send_message(f"Channel {channel_name} created")

@app_commands.command(name="embed", description="creates an embed")
@app_commands.describe(title="Title you wanna set", description="description you wanna set")
async def embed(interaction: discord.Interaction, title: str, description: str):
  embed = discord.Embed(title=title, description=description)
  await interaction.response.send_message(embed=embed)
  
  


  

                     

  
