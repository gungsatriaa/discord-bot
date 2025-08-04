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
            "- DOUBLE ACTION ×5\n"
            "- NAVY REVOLVER ×3\n"
            "- MICRO SMG x2\n"
            "- TEC-9 x1\n"
            "- PELURU SPESIAL ×1800\n"
            "- HEAVY ARMOR ×150"
        ),
        inline=False
    )

    embed.add_field(
        name="**2. PAKET ELITE 50K**",
        value=(
            "- DOUBLE ACTION ×7\n"
            "- NAVY REVOLVER ×7\n"
            "- MARKSMAN PISTOL ×4\n"
            "- MICRO SMG ×4\n"
            "- TEC-9 ×4\n"
            "- CARBINE RIFLE ×2\n"
            "- AK-47 ×2\n"
            "- BULLPUP SHOTGUN ×1\n"
            "- PELURU SPESIAL ×4000\n"
            "- HEAVY ARMOR ×650"
        ),
        inline=False
    )

    embed.add_field(
        name="**3. PAKET PLATINUM 100K**",
        value=(
            "- DOUBLE ACTION ×10\n"
            "- NAVY REVOLVER ×10\n"
            "- MARKSMAN PISTOL ×6\n"
            "- MICRO SMG ×5\n"
            "- TEC-9 ×6\n"
            "- CARBINE RIFLE ×4\n"
            "- AK-47 ×3\n"
            "- BULLPUP SHOTGUN ×3\n"
            "- BULLPUP RIFLE ×3\n"
            "- PELURU SPESIAL ×5600\n"
            "- HEAVY ARMOR ×800"
        ),
        inline=False
    )

    embed.add_field(
        name="**4. PAKET SULTAN 200K**",
        value=(
            "- DOUBLE ACTION ×15\n"
            "- NAVY REVOLVER ×15\n"
            "- MARKSMAN PISTOL ×7\n"
            "- MICRO SMG ×8\n"
            "- TEC-9 ×9\n"
            "- CARBINE RIFLE ×7\n"
            "- AK-47 ×7\n"
            "- BULLPUP SHOTGUN ×6\n"
            "- BULLPUP RIFLE ×6\n"
            "- PELURU SPESIAL ×7700\n"
            "- HEAVY ARMOR ×1000"
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
