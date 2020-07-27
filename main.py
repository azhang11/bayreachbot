
import discord
from discord import member
from discord.ext import commands, tasks
import datetime
from discord.utils import get
from itertools import cycle
import os
import time
import schedule
import asyncio

client = commands.Bot(command_prefix = '.')
#client.load_extension("cogs.database")
client.load_extension("cogs.sql")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def cap(ctx):
    await ctx.send("https://www.youtube.com/watch?v=srnG8ztQLd0")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {client.latency * 1000}ms")

@client.command()
async def lookup(ctx, member: discord.Member = None):

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp = ctx.message.created_at)

    embed.set_author(name = f"User Info = {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

    embed.add_field(name = "ID:", value = member.id)
    embed.add_field(name = "Guild name:", value = member.display_name)

    embed.add_field(name = "Created at:", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name = "Joined at:", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name = f"Roles ({len(roles)})", value = " ".join([role.mention for role in roles]))
    embed.add_field(name = "Top role:", value = member.top_role.mention)

    embed.add_field(name = "Bot?", value = member.bot)

    await ctx.send(embed = embed)



client.run("NzM3MTAzMjM2MDg2ODkwNTg3.Xx4e4g.kgVRwzv1xuOtjgAU6hCucdd38hI")
