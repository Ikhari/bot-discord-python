import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Memuat token dari file .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Mengatur intents (penting untuk Discord API versi terbaru)
intents = discord.Intents.default()
intents.message_content = True  # Mengaktifkan intents yang diperlukan

# Membuat instance bot dengan prefix perintah '!'
bot = commands.Bot(command_prefix='!', intents=intents)

# Event ketika bot berhasil terhubung ke server
@bot.event
async def on_ready():
    print(f'{bot.user.name} telah terhubung ke Discord!')
    await bot.change_presence(activity=discord.Game(name="Menjaga Server"))

# Command untuk menyapa pengguna
@bot.command(name='halo', help='Bot akan menyapa Anda.')
async def halo(ctx):
    await ctx.send(f'Halo, {ctx.author.mention}!')

# Command untuk membersihkan sejumlah pesan
@bot.command(name='bersihkan', help='Menghapus sejumlah pesan dari kanal.')
@commands.has_permissions(manage_messages=True)
async def bersihkan(ctx, jumlah: int):
    await ctx.channel.purge(limit=jumlah + 1)
    pesan = await ctx.send(f'{jumlah} pesan telah dihapus.')
    await pesan.delete(delay=5)

# Command untuk kick member
@bot.command(name='kick', help='Mengeluarkan anggota dari server.')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, alasan=None):
    await member.kick(reason=alasan)
    await ctx.send(f'Anggota {member.mention} telah dikeluarkan. Alasan: {alasan}')

# Command untuk ban member
@bot.command(name='ban', help='Memblokir anggota dari server.')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, alasan=None):
    await member.ban(reason=alasan)
    await ctx.send(f'Anggota {member.mention} telah diblokir. Alasan: {alasan}')

# Command untuk unban member
@bot.command(name='unban', help='Membuka blokir anggota dari server.')
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, nama):
    banned_users = await ctx.guild.bans()
    nama_user, tag = nama.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (nama_user, tag):
            await ctx.guild.unban(user)
            await ctx.send(f'Anggota {user.mention} telah dibuka blokirnya.')
            return
    await ctx.send(f'Anggota dengan nama {nama} tidak ditemukan.')

# Command untuk menampilkan cuaca (contoh integrasi API)
@bot.command(name='cuaca', help='Menampilkan informasi cuaca terkini.')
async def cuaca(ctx, *, kota):
    # Contoh sederhana tanpa benar-benar memanggil API
    await ctx.send(f'Informasi cuaca untuk {kota} tidak tersedia saat ini.')

# Command permainan sederhana
@bot.command(name='tebak', help='Permainan tebak angka.')
async def tebak(ctx, angka: int):
    import random
    angka_rahasia = random.randint(1, 10)
    if angka == angka_rahasia:
        await ctx.send('Selamat! Tebakan Anda benar.')
    else:
        await ctx.send(f'Sayang sekali, angka yang benar adalah {angka_rahasia}.')

# Menjalankan bot
bot.run(TOKEN)
