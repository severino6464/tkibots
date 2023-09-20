import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001951898336'




texto4 = """
🤑👾 ATENÇÃO! QUEBRANDO A PROTEÇÃO DA CASA! 
SINAIS ACERTIVOS EM 5 MINUTOS! 👾🤑
"""


texto5 = """
O Green veio!✅✅

"""


mensagem = """
🚨 𝗘𝗡𝗧𝗥𝗔𝗗𝗔 𝗖𝗢𝗡𝗙𝗜𝗥𝗠𝗔𝗗𝗔 🚨

🐯 [Fortune Tiger]()
⚠️ Sinal 𝗩𝗮́𝗹𝗶𝗱𝗼 até:{}
⭐️ 𝗠𝗮́𝘅𝗶𝗺𝗼 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: 20

💰 {}X normal 
🔃 Intercalando
⚡️ {}X Turbo


📲: Casa com a proteção quebrada: [Clique aqui](https://iluck.bet/?c=rafael999)
"""

def send_signal():

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(300) 


    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(600)



    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(600)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(600)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(600)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(600)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(600)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='Markdown')
   







def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "07:00","12:00","14:30","17:00","20:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
