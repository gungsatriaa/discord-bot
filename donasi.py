import discord
from discord.ext import commands

# Ganti dengan token bot kamu jika file ini dijalankan terpisah
TOKEN = 'MTM4Nzc1NTgwNzQ4Mjg0MzE1OA.GQyt2z.LcXKijvdCjYrrvp2oV00zOnIRU-FwjAqaKmEtg'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def donasi(ctx):
    embed = discord.Embed(
        title="💸 **PAKET DONASI BANTAIZONE** 💸",
        color=discord.Color.green()
    )

    embed.add_field(
        name="**1. PAKET STANDART 20K**",
        value=(
            "- NAVY REVOLVER ×2\n"
            "- DOUBLE ACTION ×5\n"
            "- PELURU SPESIAL ×2000\n"
            "- HEAVY ARMOR ×1000"
        ),
        inline=False
    )

    embed.add_field(
        name="**2. PAKET ELITE 50K**",
        value=(
            "- NAVY REVOLVER ×4\n"
            "- DOUBLE ACTION ×8\n"
            "- PELURU SPESIAL ×4000\n"
            "- HEAVY ARMOR ×2000"
        ),
        inline=False
    )

    embed.add_field(
        name="**3. PAKET PLATINUM 100K**",
        value=(
            "- NAVY REVOLVER ×6\n"
            "- DOUBLE ACTION ×12\n"
            "- PELURU SPESIAL ×6000\n"
            "- HEAVY ARMOR ×4000"
        ),
        inline=False
    )

    embed.add_field(
        name="**4. PAKET SULTAN 200K**",
        value=(
            "- NAVY REVOLVER ×10\n"
            "- DOUBLE ACTION ×20\n"
            "- PELURU SPESIAL ×10.000\n"
            "- HEAVY ARMOR ×8000"
        ),
        inline=False
    )

    embed.set_footer(
        text="Donasi untuk membantu perkembangan server. Open ticket untuk donasi.",
        icon_url="https://cdn.discordapp.com/attachments/1387432917818540103/1387760824654888960/bzarena.png?ex=6891463b&is=688ff4bb&hm=b87317c7b0913b381f89edb0f1d4313d3e4a307b9199c71e81e5eedcb5ef0c10&"
    )

    embed.set_author(
        name="BANTAIZONE ARENA",
        icon_url="https://cdn.discordapp.com/attachments/1387432917818540103/1387760824654888960/bzarena.png?ex=6891463b&is=688ff4bb&hm=b87317c7b0913b381f89edb0f1d4313d3e4a307b9199c71e81e5eedcb5ef0c10&"
    )

    await ctx.send(embed=embed)

bot.run(TOKEN)
