import discord
from discord.ext import commands GS

TOKEN = 'MTM4Nzc1NTgwNzQ4Mjg0MzE1OA.GQyt2z.LcXKijvdCjYrrvp2oV00zOnIRU-FwjAqaKmEtg'

intents = discord.Intents.default()
intents.message_content = True  # ← baris ini yang wajib

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def rules(ctx):
    embed = discord.Embed(
        title="📜 **RULES SERVER BANTAIZONE** 📜",
        description=(
    "**1. DILARANG MENGGUNAKAN CHEAT ATAU FILE ILLEGAL**\n"
    "⛔ MELANGGAR : BANNED PERMANEN\n\n"

    "**2. DILARANG MEMBAWA ORANG TUA, SUKU, AGAMA**\n"
    "⛔ MELANGGAR : BANNED PERMANEN / BLACKLIST\n\n"

    "**3. DILARANG TOXIC BERLEBIHAN**\n"
    "⛔ MELANGGAR : WARNING > KICK > BANNED 1-3 HARI\n\n"

    "**4. DILARANG MELAKUKAN RMT SESAMA PLAYER BANTAIZONE**\n"
    "⛔ MELANGGAR : BANNED PERMANEN ATAU HAPUS DATABASE\n\n"

    "**5. DILARANG MENYALAHGUNAKAN BUG**\n"
    "⛔ MELANGGAR : BAN 1-7 HARI (TERGANTUNG LEVEL PELANGGARAN)\n\n"

    "**6. RESPECT SESAMA PLAYER BANTAIZONE**\n"
    "⛔ MELANGGAR : TEGURAN ATAU KICK"
),

        color=discord.Color.gold()
    )

    embed.set_footer(
        text="JIKA MELANGGAR ATURAN DIATAS MAKA AKAN ADA KONSEKUENSI DARI SERVER",
        icon_url="https://cdn.discordapp.com/attachments/1387432917818540103/1387760824654888960/bzarena.png?ex=6891463b&is=688ff4bb&hm=b87317c7b0913b381f89edb0f1d4313d3e4a307b9199c71e81e5eedcb5ef0c10&"  # Ganti dengan URL logo kamu
    )

    embed.set_author(
        name="BANTAIZONE ARENA",
        icon_url="https://cdn.discordapp.com/attachments/1387432917818540103/1387760824654888960/bzarena.png?ex=6891463b&is=688ff4bb&hm=b87317c7b0913b381f89edb0f1d4313d3e4a307b9199c71e81e5eedcb5ef0c10&"  # Ganti juga ini kalau perlu
    )

    await ctx.send(embed=embed)


bot.run(TOKEN)
