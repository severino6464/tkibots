import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001807547435'  




texto4 = """
💎ENCONTRANDO FALHA...💎
🐯POSSÍVEL ENTRADA EM 2 MINUTOS

[📱 CADASTRE-SE AQUI](https://affiliates.nuts.bet/visit/?bta=36824&brand=nutsbet)
"""


texto5 = """
✅🤑BATEUUUU🤑✅
"""


mensagem = """
🔮Entrda Confirmada🔮

🐯 FORTUNE TIGER ☘️
🎯 Estratégia: Multiplicador de 100x
🔥 Jogadas: {}
⏰ Válido até: {}

🌪 Faça no máximo {} jogadas!

[📱 CADASTRE-SE AQUI](https://affiliates.nuts.bet/visit/?bta=36824&brand=nutsbet)

[ 📱 ABRIR FORTUNE TIGER🐯☘️](https://affiliates.nuts.bet/visit/?bta=36824&brand=nutsbet)
"""

def send_signal():

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(1798)

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(1798)

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(1798)

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(120)    

    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='Markdown')



def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "09:00", "14:00", "19:00" 
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
