import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002041984604'


texto4 = """
🎲 Fique atento ao jogo 🎲

🐰 Fortune Rabbit
🔎 Estamos validando uma entrada

<a href="https://go.boasortebet.com/visit/?bta=35563&brand=boasortebet">📱 Cadastre-se aqui</a>
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""


mensagem = """
⚠️ ENTRADA CONFIRMADA ⚠️

🐰 Fortune Rabbit 🐰

🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
⏰ Sinal válido até: {}

🌪 Faça no máximo {} jogadas!

<a href="https://go.boasortebet.com/visit/?bta=35563&brand=boasortebet">📱 Cadastre-se aqui</a>
"""




print("===========")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60) 



n_jogadas = random.randint(2, 15)
validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(120)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120) 
