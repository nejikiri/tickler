import os
import discord

from time import sleep
from discord.ext import commands

class Tickler(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="||", intents=discord.Intents.all())

    async def on_ready(self):
        print('Ticklers ready!')

    async def setup_hook(self) -> None:
        for f in os.listdir('./cogs'):
            if f.endswith('.py'):
                await self.load_extension(f'cogs.{f[:-3]}')

client = Tickler()
client.run('MTA0ODQyNjgwNjgxNjAxNDM0Nw.GWgtjm.6Yi55Ezfx4qnXmJH5RNW1pNhRbLpDd9N-dN_jA')