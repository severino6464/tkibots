import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001925862233'  

possibilidades_minas = [
"🔵",
"🔴"
     
 
]



texto4 = """
⚠️ Fique atento ao jogo ⚠️

🎲 BAC BOO
🔎 SESSÃO INICIADA!

🖥 Link de cadastro:[Clique aqui](https://affiliates.nuts.bet/visit/?bta=36841&brand=nutsbet)
"""

texto5 = """
SESSÃO ENCERRADA!
"""

texto6 = """
📔 RELATÓRIO DE OPERAÇÕES 

1º ENTRADA > WIN ✅
2º ENTRADA > WIN ✅
3º ENTRADA > WIN ✅
4º ENTRADA > WIN ✅
5º ENTRADA > WIN ✅
6º ENTRADA > WIN ✅

Placar: ✅ 6 x 0 ❌ (100.00%)
"""

texto7 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅!
"""

mensagem = """
✅ Entrada Confirmada 

👉 Entrada:{}

⚠️ MÁXIMO 2 GALES 
🔔 Entrada Confirmada 🔔  
✅ Entrar Agora  


📲: Plataforma correta: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=36841&brand=nutsbet)
"""

def send_signal():

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)
    bot.send_message(chat_id=channel_id, text=texto7, parse_mode='Markdown')
    time.sleep(180)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)
    bot.send_message(chat_id=channel_id, text=texto7, parse_mode='Markdown')
    time.sleep(180)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)
    bot.send_message(chat_id=channel_id, text=texto7, parse_mode='Markdown')
    time.sleep(180)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)
    bot.send_message(chat_id=channel_id, text=texto7, parse_mode='Markdown')
    time.sleep(180)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)
    bot.send_message(chat_id=channel_id, text=texto7, parse_mode='Markdown')
    time.sleep(180)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)
    bot.send_message(chat_id=channel_id, text=texto7, parse_mode='Markdown')
    time.sleep(180)

    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='Markdown')
    time.sleep(60)
    bot.send_message(chat_id=channel_id, text=texto6, parse_mode='Markdown')






def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "10:00", "15:00", "20:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
