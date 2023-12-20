import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002083489243'

links = [
    "https://exemplo1.com",
]


possibilidades_minas = [
    '💰 After the 5️⃣ bet 1️⃣ e 2️⃣',
    '💰 After the 1️⃣ bet 1️⃣ e 2️⃣',
    '💰 After the 2️⃣ bet 1️⃣ e 2️⃣'
]



texto4 = """
🚨 <b>ALERT, POSSIBLE ENTRY!</b>
🎰 Roulette: <a href="https://1woqny.top/#fsxk">Crazy Time Bet7k</a>
⏳ Wait to confirm
"""
texto3 = """
✅✅ GREEN!!! ✅✅
"""

mensagem = """
🔔 Confirmed Entry 🔔 
🎰 Roulette: <a href="https://1woqny.top/#fsxk">Crazy Time Bet7k</a>

{}

🔁 Make up to 2 gales
"""




print("======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60)
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60)
bot.send_message(chat_id=group_id, text=texto3, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(180)
