import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001635658555'

possibilidades_minas = [
    "Apostar na 1° e 2° coluna",
    "Apostar na 1° e 3° coluna",
    "Apostar na 2° e 3° coluna",
    "Apostar na 1° e 2° dúzia",
    "Apostar na 1° e 3° dúzia",
    "Apostar na 2° e 3° dúzia"
]



texto4 = """
⚠️ <b>ATENÇÃO VAMOS INICIAR</b> ⚠️

<a href="https://affiliates.nuts.bet/visit/?bta=37630&brand=nutsbet"><b>🔗 Cadastre-se antes de Jogar!</b></a>

<a href="https://nuts.bet/live-casino/game/2177465"><b>🏦 Abra a roleta</b></a>
"""

texto5 = """
✅✅ <b>SESSÃO ENCERRADA!</b> ✅✅
"""


mensagem = """
🚨 <b>ENTRADA CONFIRMADA</b> 🚨
🎮 Roleta: Roleta Brasileira


{}

⏱️ Válido até: {}
⭕ Ate duas proteções - Cobrir o zero.

<a href="https://affiliates.nuts.bet/visit/?bta=37630&brand=nutsbet"><b>🔗 Cadastre-se antes de Jogar!</b></a>

<a href="https://nuts.bet/live-casino/game/2177465"><b>🏦Abra a roleta</b></a>
"""

def send_signal():

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 


    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(180)


    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)



def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "10:20", "14:30", "19:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
