import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001908449168'

sticker_file_id = 'CAACAgEAAxkBAAMCZSbmh4EopfmSJgx8Z8sDxkeWf1UAAvwAAzgOghFAju2fQymOBzAE'

mensagem = """
🚨 <b>ENTRADA CONFIRMADA</b> 🚨

⏰19:05 🕗 ✅ | 19:09 🕗 ✅
⏰19:13 🕗 ✅ | 19:21 🕗 ✅ 
⏰19:30 🕖 ✅ | 19:38 🕖 ✅
⏰19:40 🕖 ✅ | 19:47 🕖 ✅
⏰19:53 🕖 ✅ | 19:59 🕖 ✅

⏰20:04 🕗 ✅ | 20:18 🕗 ✅
⏰20:19 🕗 ✅ | 20:22 🕗 ✅
⏰20:28 🕗 ✅ | 20:35 🕗 ✅
⏰20:41 🕗 ✅ | 20:48 🕗 ✅
⏰20:53 🕗 ✅ | 20:59 🕗 ✅

⏰21:03 🕘 ✅ | 21:09 🕘 ✅
⏰21:15 🕘 ✅ | 21:20 🕘 ✅
⏰21:28 🕘 ✅ | 21:35 🕘 ✅
⏰21:41 🕘 ✅ | 21:47 🕘 ✅
⏰21:52 🕘 ✅ | 21:59 🕘 ✅

⏰22:02 🕙 ✅ | 22:07 🕙 ✅
⏰22:13 🕙 ✅ | 22:20 🕙 ✅
⏰22:26 🕙 ✅ | 22:32 🕙 ✅
⏰22:39 🕙 ✅ | 22:45 🕙 ✅
⏰22:52 🕙 ✅ | 22:59 🕙 ✅

⏰23:03 🕚 ✅ | 23:09 🕚 ✅
⏰23:15 🕚 ✅ | 23:20 🕚 ✅
⏰23:27 🕚 ✅ | 23:33 🕚 ✅
⏰23:40 🕚 ✅ | 23:46 🕚 ✅
⏰23:52 🕚 ✅ | 23:59 🕚 ✅

🐌 {}x Normal
🔃Intercalando 
⚡ {}x Turbo



<a href="https://bcraft.g2afse.com/click?pid=15&offer_id=36">🔗 Fazer CADASTRO ✅</a>
"""

print("========")

 
n_jogadas = random.randint(6, 20)
n_jogadas2 = random.randint(4, 20)
mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(120)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(480)