# Saya-Userbot
from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            f"🌖"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern='^.helikopter(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("▬▬▬.◙.▬▬▬ \n"
                     "═▂▄▄▓▄▄▂ \n"
                     "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                     "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                     "◥█████◤ \n"
                     "══╩══╩══ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ Hallo Semuanya :) \n"
                     "╬═╬☻/ \n"
                     "╬═╬/▌ \n"
                     "╬═╬/ \\ \n")


@register(outgoing=True, pattern='^.tembak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**Mau Jadi Pacarku Gak?!**")


@register(outgoing=True, pattern='^.bundir(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Dadah Semuanya...`          \n　　　　　|"
                     "\n　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　／￣￣＼| \n"
                     "＜ ´･ 　　 |＼ \n"
                     "　|　３　 | 丶＼ \n"
                     "＜ 、･　　|　　＼ \n"
                     "　＼＿＿／∪ _ ∪) \n"
                     "　　　　　 Ｕ Ｕ\n")


@register(outgoing=True, pattern='^.aowkwk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("────██──────▀▀▀██\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`")


@register(outgoing=True, pattern='^.ular(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n")

@register(outgoing=True, pattern='^.lv(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("              ｡ﾟﾟ･｡･ﾟﾟ｡\n"
                     "               。   ｡ﾟ\n"
                     "                ﾟ･｡･ﾟ\n"
                     "           ︵          ︵\n"
                     "         (    ╲     /     / \n"
                     "          ╲       ╲/    / \n"
                     "            ╲       ╲  / \n"
                     "          ╭ ͡ ╲        ╲\n"
                     "      ╭ ͡ ╲     ╲        ﾉ\n"
                     "   ╭ ͡ ╲    ╲          ╱\n"
                     "   ╲    ╲           ╱\n"
                     "     ╲            ╱\n"
                     "             ︶\n")



                       


@register(outgoing=True, pattern='^.supreme(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
                     "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")


@register(outgoing=True, pattern='^.tank(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                     "▂▄▅█████████▅▄▃▂…\n"
                     "[███████████████████]\n"
                     "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")


@register(outgoing=True, pattern='^.babi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")


@register(outgoing=True, pattern='^.ajg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")


@register(outgoing=True, pattern='^.bernyanyi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ganteng Doang Gak Bernyanyi (ง˙o˙)ว**")
    sleep(2)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")


@register(outgoing=True, pattern='^.foff(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(".                       /¯ )")
    await typew.edit(".                       /¯ )\n                      /¯  /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")

CMD_HELP.update({
    "panimasi2":
    "`.bulan` ; `.hati` ; `.bernyanyi`\
    \n🗿CMD🗿: liat aja.\
    \n\n`.helikopter` ; `.tank` ; `.tembak`\n`.bundir`\
    \n🗿CMD🗿: liat sendiri\
    \n\n`.y`\
    \n🗿CMD🗿: jempol\
    \n\n`.supreme`\
    \n🗿CMD🗿: Liat Sendiri Ajalah Tod\
    \n\n`.aowkwk`\
    \n🗿CMD: 🗿ketawa lari.\
    \n\n`.ular` ; `.babi` ; `.foff` ; `.foto` ; `.ajg`\
    \n🗿CMD🗿:liat sendiri."
})
