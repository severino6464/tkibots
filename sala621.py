import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002091709537'

sticker_file_id = 'CAACAgIAAxkBAAMmZSb_ngXS-jrJPaIDkQxNkCtYOQQAAtgLAAJYD5hKNPj69b5xWK8wBA'

texto4 = """
🎲 Fique atento ao jogo 🎲

🐭 Fortune mouse
🔎 Estamos validando uma entrada

<a href="https://affiliates.nuts.bet/visit/?bta=37766&brand=nutsbet">📱 Cadastre-se aqui</a>
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""


mensagem = """
⚠️ ENTRADA CONFIRMADA ⚠️

🐭 Fortune mouse

🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
⏰ Sinal válido até: {}

🌪 Faça no máximo {} jogadas!

<a href="https://affiliates.nuts.bet/visit/?bta=37766&brand=nutsbet">📱 Cadastre-se aqui</a>

<a href="https://affiliates.nuts.bet/visit/?bta=37766&brand=nutsbet">📱 Jogar Fortune mouse 🐭 </a>
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
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(120) 
