import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002129062750'

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

🖥 Link de cadastro:[Clique aqui](https://affiliates.nuts.bet/visit/?bta=37072&nci=5344)
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

📲: Plataforma correta: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=37072&nci=5344))
"""

texto6 = """
🚨🚨 HORARIOS DE FUNCIONAMENTO MÉTODO AVIATOR🚨🚨


✅ Ai boca atenção que vai começar a sessão do método ✅
✅ sessão todos os dias ✅

⏰ 09:00 - 9:40 

⏰ 13:00 - 13:40

⏰ 19:00- 19:40

⏰ 22:00 - 22:40


MÉTODO AVIATOR:
https://t.me/+FfjehVUGzWY4NTdh

MÉTODO PENALTY: 
https://t.me/+vguYFi-7FFw0MDJh



📌 Vídeo ensinando como funciona fixado no topo do GRUPO✅
"""

def send_signal():

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) 
    bot.send_message(chat_id=group_id, text=texto6, parse_mode='Markdown')

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "09:00", "13:00", "19:00", "22:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")