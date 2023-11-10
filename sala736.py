import telebot
import time
import threading
import datetime
import random
import sys
import os
from telebot import types

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 
bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002108709967'


possibilidades_minas = [
    "‼️ RETIRAR EM 1.50x",
    "‼️ RETIRAR EM 2.00x",
    "‼️ RETIRAR EM 2.00x",
    "‼️ RETIRAR EM 3.50x",
    "‼️ RETIRAR EM 1.04x",
    "‼️ RETIRAR EM 2.30x",
    "‼️ RETIRAR EM 5.00x"
]

texto4 = """
⚠️ Fique atento ao jogo ⚠️

✈️ Aviator 
🔎 identificando entrada

<a href="https://bit.ly/PlataformaSecreta_vip"><b>🖥 Link de cadastro</b></a>
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
"""

mensagem = """
✅ Entrada Confirmada 

{}

⚠️ MÁXIMO 2 GALES 
🔔 Entrada Confirmada 🔔  
✅ Entrar Agora  

⏱️ Válido até: {}

<a href="https://bit.ly/PlataformaSecreta_vip"><b>🖥 Link de cadastro</b></a>
"""

links = [
    "https://exemplo1.com",
   
]

def reiniciar_programa():
    python = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)
    time.sleep(10)  # Pausa de 10 segundos
    os.execl(python, *args)

def enviar_mensagem():
    keyboard = types.InlineKeyboardMarkup()
    instagram_button = types.InlineKeyboardButton(text="Instagram", url="https://instagram.com/melobetz?igshid=YzAwZjE1ZTI0Zg%3D%3D&utm_source=qr")
    keyboard.add(instagram_button)

    bot.send_message(chat_id=group_id, text=texto5, reply_markup=keyboard)

def enviar_periodicamente():
    while True:
        try:
            possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
            link_aleatorio = random.choice(links)
            validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
            hora_validade = validade.strftime("%H:%M")
            mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
            mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
            mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

            bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML')
            time.sleep(120)

            bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML')
            time.sleep(120)

            enviar_mensagem()
            time.sleep(200)

        except Exception as e:
            print("Ocorreu um erro fatal:", e)
            print("REINICIANDO O PROGRAMA")
            reiniciar_programa()

# Inicia um thread separado para enviar a mensagem periodicamente
thread_envio = threading.Thread(target=enviar_periodicamente)
thread_envio.start()

bot.polling()
