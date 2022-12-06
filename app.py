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
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)
        for f in os.listdir('./cogs'):
            if f.endswith('.py'):
                await self.load_extension(f'cogs.{f[:-3]}')

client = Tickler()
client.run('MTA0ODQyNjgwNjgxNjAxNDM0Nw.GFRVPA.ZYHnpGsd5DIVi_li287P5y-CeBj14sK5CRyajo')