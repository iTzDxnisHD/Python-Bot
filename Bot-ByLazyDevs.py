import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import time

client = commands.Bot(command_prefix = '~')
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://discord.gg/NEDjJK ❤"))

@client.command()
async def ping (ctx):
	await ctx.send(f':ping_pong: **Pong! Dein Ping beträgt:** {round(client.latency * 1000)}ms')
	
client.run("Bot-Token")