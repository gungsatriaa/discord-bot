import discord
from discord.ext import commands

# Ganti dengan token bot kamu jika file ini dijalankan terpisah
TOKEN = 'MTM4Nzc1NTgwNzQ4Mjg0MzE1OA.GQyt2z.LcXKijvdCjYrrvp2oV00zOnIRU-FwjAqaKmEtg'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def rulesdonasi(ctx):
    embed = discord.Embed(
        title="📝 **RULES DONASI BANTAIZONE** 📝",
        color=discord.Color.green()
    )

    embed.add_field(
        name="**1. DONASI BERSIFAT SUKARELA DAN TANPA PAKSAAN**",
        value=(
            "- Donasi ke BANTAIZONE ARENA dianggap sebagai bentuk dukungan sukarela untuk pengembangan server, bukan pembelian item yang dijamin. Donasi tidak bisa ditarik kembali sepenuhnya. Jika refund disetujui, akan dikenakan potongan 15% sebagai biaya administrasi. Dengan berdonasi, Anda menyetujui kebijakan ini tanpa hak untuk protes atau tuntutan atas perubahan dalam game maupun benefit.\n"
        ),
        inline=False
    )

    embed.add_field(
        name="**2. JIKA ADA KESALAHAN DARI PIHAK PLAYER MAKA REFUND TIDAK 100%**",
        value=(
            "- Jika donasi dilakukan sebelum memastikan ketersediaan paket dan ternyata tidak tersedia, proses pengembalian dana (refund) akan diproses dalam waktu 1–2 hari kerja. Harap diperhatikan bahwa pengembalian dana akan dikenakan potongan sebesar 15% dari total nominal donasi sebagai biaya administrasi.\n"
        ),
        inline=False
    )

    embed.add_field(
        name="**3. PEMBAYARAN HANYA MENGGUNAKAN BAGIBAGI.COM**",
        value=(
            "- Seluruh proses donasi di BANTAIZONE ARENA hanya dilakukan melalui platform resmi Bagibagi.com. Kami tidak bertanggung jawab atas transaksi yang dilakukan di luar metode yang telah ditentukan. Pastikan Anda melakukan pembayaran hanya melalui link dan akun resmi yang diberikan oleh pihak admin.\n"
        ),
        inline=False
    )

    embed.set_footer(
        text="Ayo bantulah untuk mengembangkan server ini.",
        icon_url="https://cdn.discordapp.com/attachments/1387432917818540103/1387760824654888960/bzarena.png?ex=6891463b&is=688ff4bb&hm=b87317c7b0913b381f89edb0f1d4313d3e4a307b9199c71e81e5eedcb5ef0c10&"
    )

    embed.set_author(
        name="BANTAIZONE ARENA",
        icon_url="https://cdn.discordapp.com/attachments/1387432917818540103/1387760824654888960/bzarena.png?ex=6891463b&is=688ff4bb&hm=b87317c7b0913b381f89edb0f1d4313d3e4a307b9199c71e81e5eedcb5ef0c10&"
    )

    await ctx.send(embed=embed)

bot.run(TOKEN)
