import telebot
import time
import threading
import datetime
import random
import sys
import os
from telebot import types

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" #token fox

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001688759094'


texto4 = """
🐯 Atenção! Tigre saindo da jaula…
🤑 Sinais em breve, se prepare!   

🐯💰🐯💰🐯💰🐯💰🐯💰🐯💰🐯
"""

texto5 = """

✅✅✅ VITÓRIA!!! ✅✅✅
🕑 Finalizado
🐯☘🐯☘🐯☘🐯☘🐯☘🐯☘🐯☘

Você que fez GREEN envie um print em nosso suporte: @suportedoscampeoes
   """



mensagem = """
🚨 𝗘𝗡𝗧𝗥𝗔𝗗𝗔 𝗖𝗢𝗡𝗙𝗜𝗥𝗠𝗔𝗗𝗔 🚨

🐯 [Fortune Tiger](https://viralizouu.com/tigerfree-)
⚠️ Sinal 𝗩𝗮́𝗹𝗶𝗱𝗼 até:{}
⭐️ 𝗠𝗮́𝘅𝗶𝗺𝗼 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: 20

💰 {}X normal 
🔃 Intercalando
⚡️ {}X Turbo


📲: Plataforma correta: [Clique aqui](https://viralizouu.com/tigerfree-)

"""








n_jogadas = random.randint(6, 13)
n_jogadas2 = random.randint(4, 15)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

bot.send_message(chat_id=group_id, text=texto4 ,parse_mode='Markdown')
print("BOT-TIGER-WALACE")
       
time.sleep(60)  # Aguarda 1 minuto

        
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
       
time.sleep(240)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5 ,parse_mode='Markdown')

time.sleep(120)
        
        
