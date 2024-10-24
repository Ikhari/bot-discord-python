import discord
from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tebak', help='Permainan tebak angka.')
    async def tebak(self, ctx, angka: int):
        angka_rahasia = random.randint(1, 10)
        if angka == angka_rahasia:
            await ctx.send('Selamat! Tebakan Anda benar.')
        else:
            await ctx.send(f'Sayang sekali, angka yang benar adalah {angka_rahasia}.')

def setup(bot):
    bot.add_cog(Games(bot))
