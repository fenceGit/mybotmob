from discord.ext import commands
import discord
from discord import app_commands
import random
import os
from datetime import timedelta

@app_commands.command(name="mute", description="mute a user")
@app_commands.default_permissions(manage_roles=True)
@app_commands.describe(member="member to mute")
async def mute(interaction: discord.Interaction, member: discord.Member, duration: int):
  timedelta(minutes=duration)
  if member.top_role >= interaction.user.top_role:
    await interaction.response.send_message(f"YOU REALLY THINK YOU CAN MUTE {member.mention}")
    return
  await interaction.response.defer()
  timeout = discord.utils.utcnow() + timedelta(minutes=duration)
  await member.timeout(timeout)
  await interaction.followup.send(f"{member.mention} has been punished for {duration} minutes")

@app_commands.command(name="unmute", description="unmute the user you punished for not being a good boy")
@app_commands.default_permissions(moderate_members=True)
@app_commands.describe(member="member to unmute")
async def unmute(interaction: discord.Interaction, member: discord.Member):
  if member.timed_out_until is None:
    await interaction.response.send_message(f"{member.mention} was never muted")
    return
  await member.timeout(None)
  await interaction.response.send_message(f"{member.mention} has been unmuted was it a false reason is he REALLY A GOOD BOY?")
