import discord
from time import sleep

from discord.ext import commands

class Tickle(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(name='tickle')
    @commands.has_role('new role')
    async def tickle(self, ctx, duration: int):
        for x in range(0, duration):
            sleep(1)
            await ctx.send('Tickle\n')

async def setup(bot: commands.Bot):
    await bot.add_cog(Tickle(bot))