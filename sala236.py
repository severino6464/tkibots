import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001825767051'  

possibilidades_minas = [
    "Apostar na duzia 1 e 3",
    "Apostar na 1º e 3º coluna",
    "Apostar na 2º e 3º coluna",
    "Apostar na 1º e 2º coluna"
]



texto4 = """
ATENÇÃO VAMOS INICIAR 

FAÇA SEU CADASTRO 👇
[Clique aqui](https://affiliates.nuts.bet/visit/?bta=36463&brand=nutsbet)

ENTRE NO JOGO👇🏻
[Clique aqui](https://affiliates.nuts.bet/visit/?bta=36463&brand=nutsbet)
"""

texto5 = """
SESSÃO ENCERRADA!
"""


mensagem = """
💰 ENTRADA CONFIRMADA 💰
🎰 Roleta: Brasileira
Link: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=36463&brand=nutsbet)

{}

👉 Cobrir o zero
🔁 Fazer até 3 gales
🔗 [Cadastre-se antes de Jogar!](https://affiliates.nuts.bet/visit/?bta=36463&brand=nutsbet)
⏱️ Válido até: {}
"""

def send_signal():
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
 



    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 



    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)


    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)


    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)


    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)


    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)


    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='Markdown')






def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "10:00", "15:00", "21:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
    check_and_send_signal()
    # Wait for 1 minute before checking the time again
    datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
    print(f"Error occurred: {str(e)}")
