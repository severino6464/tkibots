import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001937083111'  




texto4 = """
⚠️ Fique atento ao jogo ⚠️

🐂 Fortune OX
🔎 identificando entrada

<a href="https://affiliates.nuts.bet/visit/?bta=37296&brand=nutsbet">📱 Cadastre-se aqui</a>
"""


texto5 = """
✅🤑BATEUUUU🤑✅
"""


mensagem = """
⚠️ <b>ENTRADA CONFIRMADA</b> ⚠️
🧭 <b>Comece a girar agora</b>

🐂 Fortune OX

🔥 𝗡º 𝗱𝗲 rodadas automáticas: {}
🔹 {}X modo Normal
🔹 {}X modo Turbo
⏰ Sinal válido até: {}


🌪 Faça no máximo {} jogadas!

<a href="https://affiliates.nuts.bet/visit/?bta=37296&brand=nutsbet">📱 Cadastre-se aqui</a>

<a href="https://affiliates.nuts.bet/visit/?bta=37296&brand=nutsbet">📱 Jogar Fortune Ox</a>

🚨O sinal do robô só funciona apenas na plataforma acima! Faça💰🤑
"""

def send_signal():
    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 
    n_jogadas = 10
    n_jogadas2 = 15
    n_jogadas3 = 15
    n_jogadas4 = 10
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas,n_jogadas2,n_jogadas3,hora_validade, n_jogadas4)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 
    n_jogadas = 10
    n_jogadas2 = 15
    n_jogadas3 = 15
    n_jogadas4 = 10
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas,n_jogadas2,n_jogadas3,hora_validade, n_jogadas4)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 
    n_jogadas = 10
    n_jogadas2 = 15
    n_jogadas3 = 15
    n_jogadas4 = 10
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas,n_jogadas2,n_jogadas3,hora_validade, n_jogadas4)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 
    n_jogadas = 10
    n_jogadas2 = 15
    n_jogadas3 = 15
    n_jogadas4 = 10
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas,n_jogadas2,n_jogadas3,hora_validade, n_jogadas4)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 
    n_jogadas = 10
    n_jogadas2 = 15
    n_jogadas3 = 15
    n_jogadas4 = 10
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas,n_jogadas2,n_jogadas3,hora_validade, n_jogadas4)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)
    

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "09:00", "15:00", "20:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
