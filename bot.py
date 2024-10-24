import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Memuat token dari file .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Mengatur intents
intents = discord.Intents.default()
intents.message_content = True

# Memuat prefix dari file
def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes.get(str(message.guild.id), '!')  # Default prefix '!' jika tidak ditemukan

# Membuat instance bot dengan dynamic prefix
bot = commands.Bot(command_prefix=get_prefix, intents=intents)

# Event ketika bot berhasil terhubung ke server
@bot.event
async def on_ready():
    print(f'{bot.user.name} telah terhubung ke Discord!')
    await bot.change_presence(activity=discord.Game(name="Menjaga Server"))

# Event ketika bot bergabung ke guild baru
@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'  # Mengatur default prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

# Event ketika bot keluar atau dihapus dari guild
@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id), None)

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

# Perintah untuk mengubah prefix
@commands.has_permissions(administrator=True)
@bot.command(name='setprefix', help='Mengubah prefix perintah bot.')
async def setprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix berhasil diubah menjadi `{prefix}`')

# Memuat cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Menjalankan bot
bot.run(TOKEN)
