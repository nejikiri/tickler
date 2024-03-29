import os
import discord

from time import sleep
from discord.ext import commands

MY_GUILD = discord.Object(id='950937956682698862')

class Tickler(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def on_ready(self):
        print('Ticklers ready!') 

    async def setup_hook(self) -> None:
        for f in os.listdir('./cogs'):
            if f.endswith('.py'):
                await self.load_extension(f'cogs.{f[:-3]}')

client = Tickler()
client.run('MTAxNzE2NDgyNjAyOTYwNDk0NQ.GV-a0X.KTakS1DVNgAoNwr2ljLjYTt53CsaCJOW6D1gq0')