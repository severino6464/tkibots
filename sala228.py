import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = ' -1001563762046'


texto4 = """
🎲 Fique atento ao jogo 🎲

🐯 Fortune Tiger - Entrada em 2 minutos
🔎 Estamos validando uma entrada

[📱 Cadastre-se aqui](https://affiliates.nuts.bet/visit/?bta=35979&brand=nutsbet)
"""

texto5 = """
🔷🔹 Entrada finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""


mensagem = """
⚠️ ENTRADA CONFIRMADA ⚠️

🐯 𝗙𝗼𝗿𝘁𝘂𝗻𝗲 𝗧𝗶𝗴𝗲𝗿 ☘
🎯 Estratégia: 𝗛𝗼𝗿𝗮́𝗿𝗶𝗼𝘀 𝗣𝗮𝗴𝗮𝗻𝘁𝗲𝘀
🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
⏰ Sinal válido até: {}

🌪 Faça no máximo {} jogadas!

[📱 Cadastre-se aqui](https://affiliates.nuts.bet/visit/?bta=35979&brand=nutsbet)

[📱 Jogar Fortune Tiger🐯☘](https://affiliates.nuts.bet/visit/?bta=35979&brand=nutsbet)
"""



while True:

    print("BOT-aff224-nuts")

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 



    n_jogadas = random.randint(2, 10)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas)

    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(60)  # Espera 5 minutos (300 segundos)

    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 
