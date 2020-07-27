from http import server

import discord
import schedule as schedule
from discord import guild, client, Client
from discord.ext import commands, tasks
import sqlite3
import asyncio
import functools
import datetime
import time
from itertools import cycle
import asyncio
from datetime import timezone, tzinfo, timedelta



class SQLDatabase (commands.Cog):
    def __init__(self, client):
        self.client = client

    conn = sqlite3.connect("bayreach.sqlite")
    c = conn.cursor()

    @commands.Cog.listener()
    async def on_ready(self):
        print("SQL Database is online.")

    @commands.command()
    async def sqlping(self, ctx):
        await ctx.send("SQLPong!")

    @commands.command()
    async def log(self, ctx, hours):
        con = sqlite3.connect('bayreach.sqlite')
        c = con.cursor()

        c.execute(f"SELECT * FROM users WHERE name = {ctx.author.id}")
        if c.fetchone() is None:
            c.execute(f"INSERT INTO users VALUES ({ctx.author.id}, {hours})")
            await ctx.send(f"{ctx.author.mention} has successfully logged {hours} hours.")
        else:
            c.execute(f"SELECT hours FROM users WHERE name = {ctx.author.id}")
            add_hours = functools.reduce(lambda sub, ele: sub * 10 + ele, c.fetchone())
            add_hours += float(hours)

            c.execute(f"UPDATE users SET hours = {add_hours} WHERE name = {ctx.author.id}")
            await ctx.send(f"{ctx.author.mention} has successfully logged {hours} hours.")

        con.commit()
        con.close()

    @commands.command()
    async def stats(self, ctx):
        con = sqlite3.connect('bayreach.sqlite')
        c = con.cursor()

        c.execute(f"SELECT * FROM users WHERE name = {ctx.author.id}")

        if c.fetchone() is None:
            await ctx.send(f"{ctx.author.mention} has no hours logged!")
        else:
            c.execute(f"SELECT hours FROM users WHERE name = {ctx.author.id}")
            cur_hours = functools.reduce(lambda sub, ele: sub * 10 + ele, c.fetchone())
            await ctx.send(f"{ctx.author.mention} has {cur_hours} lifetime hours.")

        con.commit()
        con.close()


def setup(client):
    client.add_cog(SQLDatabase(client))