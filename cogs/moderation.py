import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bersihkan', help='Menghapus sejumlah pesan dari kanal.')
    @commands.has_permissions(manage_messages=True)
    async def bersihkan(self, ctx, jumlah: int):
        await ctx.channel.purge(limit=jumlah + 1)
        pesan = await ctx.send(f'{jumlah} pesan telah dihapus.')
        await pesan.delete(delay=5)

    @commands.command(name='kick', help='Mengeluarkan anggota dari server.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, alasan=None):
        await member.kick(reason=alasan)
        await ctx.send(f'Anggota {member.mention} telah dikeluarkan. Alasan: {alasan}')

    @commands.command(name='ban', help='Memblokir anggota dari server.')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, alasan=None):
        await member.ban(reason=alasan)
        await ctx.send(f'Anggota {member.mention} telah diblokir. Alasan: {alasan}')

    @commands.command(name='unban', help='Membuka blokir anggota dari server.')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, nama):
        banned_users = await ctx.guild.bans()
        nama_user, tag = nama.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (nama_user, tag):
                await ctx.guild.unban(user)
                await ctx.send(f'Anggota {user.mention} telah dibuka blokirnya.')
                return
        await ctx.send(f'Anggota dengan nama {nama} tidak ditemukan.')

# Menambahkan cog ke bot
def setup(bot):
    bot.add_cog(Moderation(bot))
