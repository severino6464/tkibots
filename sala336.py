import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001932819990'


texto4 = """
🎲 Fique atento ao jogo 🎲

🐂 Fortune OX
🔎 Estamos validando uma entrada

[📱 Cadastre-se aqui](https://affiliates.nuts.bet/visit/?bta=35945&brand=nutsbet)
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""


mensagem = """
⚠️ ENTRADA CONFIRMADA ⚠️

🐂 Fortune OX

🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
⏰ Sinal válido até: {}

🌪 Faça no máximo {} jogadas!

[📱 Cadastre-se aqui](https://affiliates.nuts.bet/visit/?bta=35945&brand=nutsbet)

[📱 Jogar Fortune ox](https://affiliates.nuts.bet/visit/?bta=35945&brand=nutsbet)
"""





print("aff336")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
time.sleep(60) 



n_jogadas = random.randint(2, 15)
validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(120)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
time.sleep(120) 