import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001848899968'  




texto4 = """
🚨 Analisando 🚨
🎰 Fortune Tiger 🐯
🏠 Nuts Bet

💰 4 ou 8 reais POR JOGADA

💰 Cria a sua conta com bônus aqui!  👇

🔗 [LINK](https://affiliates.nuts.bet/visit/?bta=36355&brand=nutsbet&utm_campaign=tiger)
"""

mensagem = """
🔔 ENTRADA CONFIRMADA 🔔
🎰 Fortune Tiger 🐯
🏠 Nuts Bet

🚥 Normal: {}x 

⚡ Turbo: {}x

⏰ Válido até: {}

💰 4 ou 8 reais POR JOGADA

💰 Cria a sua conta com bônus aqui!  👇

🔗 [LINK](https://affiliates.nuts.bet/visit/?bta=36355&brand=nutsbet&utm_campaign=tiger)
"""

def send_signal():

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 

    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)


    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    n_jogadas = random.randint(3, 12)
    n_jogadas2 = random.randint(3, 12)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

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