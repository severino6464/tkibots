import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001541256350'  

possibilidades_minas = [
    "💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",
    "💣💣⭐️💣⭐️\n💣⭐️⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",
    "💣💣💣⭐️⭐️\n💣💣💣⭐️💣\n💣⭐️⭐️⭐️💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣💣💣⭐️\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣⭐️⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣💣💣⭐️\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "💣⭐️💣💣💣\n⭐️💣⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣",
    "💣⭐️💣⭐️💣\n💣💣💣⭐️💣\n💣💣⭐️⭐️💣\n💣💣⭐️⭐️💣\n💣💣⭐️💣💣",
    "⭐️⭐️⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "💣💣💣💣💣\n💣💣💣💣⭐️\n⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️⭐️💣💣💣\n💣⭐️💣💣💣\n💣⭐️⭐️⭐️💣\n💣💣💣💣💣\n💣💣💣💣💣",
    "⭐️⭐️💣⭐️💣\n💣💣💣⭐️⭐️\n💣💣💣💣💣\n💣💣💣💣💣\n💣⭐️⭐️⭐️💣",
    "💣💣💣💣⭐️\n⭐️💣💣⭐️💣\n⭐️⭐️⭐️💣💣\n💣⭐️💣💣💣\n💣⭐️💣💣💣",
    "⭐️💣💣⭐️💣\n💣💣💣💣💣\n💣⭐️💣⭐️💣\n💣⭐️💣💣💣\n💣⭐️💣⭐️💣",
    "⭐️⭐️⭐️💣💣\n⭐️💣⭐️💣💣\n💣💣💣💣💣\n💣💣💣💣💣\n💣💣💣⭐️💣",
    "⭐️💣💣💣💣\n⭐️💣💣⭐️💣\n💣💣💣💣💣\n💣💣⭐️⭐️💣\n💣💣⭐️⭐️⭐️",
    "💣💣💣💣⭐️\n⭐️💣💣⭐️💣\n⭐️💣⭐️⭐️💣\n💣💣💣💣💣\n💣💣⭐️⭐️💣",
    "💣💣💣⭐️💣\n⭐️💣💣⭐️⭐️\n⭐️💣💣💣💣\n💣💣💣💣💣\n💣💣💣⭐️💣",
    "⭐️💣💣💣💣\n💣💣💣💣💣\n⭐️💣💣💣💣\n💣⭐️💣⭐️💣\n💣⭐️💣⭐️💣"
]


texto4 = """
ATENÇÃO VAMOS INICIAR 

FAÇA SEU CADASTRO 👇
[Clique aqui](https://affiliates.nuts.bet/visit/?bta=36355&brand=nutsbet&utm_campaign=mines)

"""

texto5 = """
SESSÃO ENCERRADA!
"""


mensagem = """
🎲 Entrada confirmada 🎲
🥇: Entrada 

{}

🎮: Tentativas: 2
Jogar com 2 a 3 minas

📲: Plataforma correta: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=36355&brand=nutsbet&utm_campaign=mines)
👉🏻: Link do jogo: [Mines](https://affiliates.nuts.bet/visit/?bta=36355&brand=nutsbet&utm_campaign=mines)
⏱️ Válido até: {}
"""

def send_signal():
    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='Markdown')


def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "10:00", "15:30", "20:30"
    ]

    if current_time in signal_times:
        send_signal()


try:
    check_and_send_signal()
    # Wait for 1 minute before checking the time again
    datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
    print(f"Error occurred: {str(e)}")
