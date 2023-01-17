import discord
from time import sleep

from discord.ext import commands

MY_GUILD = discord.Object(id='950937956682698862')

class Tickle(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.hybrid_command(name='tickle', aliases=["t"])
    @commands.has_role('new role')
    async def tickle(self, ctx, duration: int):
        for x in range(0, duration):
            sleep(1)
            await ctx.send('Tickle\n')
    
    @commands.command(name="sync")
    async def sync(self, ctx):
        ctx.bot.tree.copy_global_to(guild=MY_GUILD)
        await ctx.bot.tree.sync(guild=MY_GUILD)

async def setup(bot: commands.Bot):
    await bot.add_cog(Tickle(bot))