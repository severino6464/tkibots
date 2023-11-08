import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001973318281'  

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
[Clique aqui](=======)

"""

texto5 = """
SESSÃO ENCERRADA!

SÓ GREEN!!! 🤑🤑🤑
"""


mensagem = """
🎲 Entrada confirmada 🎲
🥇: Entrada 

{}

🎮: Tentativas: 2
Jogar com 2 a 3 minas

📲: Plataforma correta: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=36075&amp;brand=nutsbet)
👉🏻: Link do jogo: [Mines](https://affiliates.nuts.bet/visit/?bta=36075&amp;brand=nutsbet)
⏱️ Válido até: {}
"""

def send_signal():
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
 



    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 



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




#cada sessao com 20 sinais de 10 minutos de intervalo cada

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "09:00", "14:00", "20:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
    check_and_send_signal()
    # Wait for 1 minute before checking the time again
    datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
    print(f"Error occurred: {str(e)}")
</p>
