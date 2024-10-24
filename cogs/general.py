import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='halo', help='Bot akan menyapa Anda.')
    async def halo(self, ctx):
        await ctx.send(f'Halo, {ctx.author.mention}!')

def setup(bot):
    bot.add_cog(General(bot))
