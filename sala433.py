import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001958644577'  

possibilidades_minas = [
    "Apostar em números baixos [1-18]",
    "Apostar em números altos [19-36]",
    "Apostar na duzia 1 e 3",
    "Apostar na cor 🔴",
    "Apostar na cor ⚫"
]



texto4 = """
⚠️ <b>ATENÇÃO VAMOS INICIAR</b> ⚠️

<a href="https://affiliates.nuts.bet/visit/?bta=37384&brand=nutsbet"><b>🔗 Cadastre-se antes de Jogar!</b></a>

<a href="https://nuts.bet/live-casino/game/2177465"><b>🏦 Abra a roleta</b></a>
"""

texto5 = """
✅✅ <b>SESSÃO ENCERRADA!</b> ✅✅
"""


mensagem = """
💰 ANALISTA CONFIRMOU 💰
🎰 Roleta: Brasileira

{}

⚠️ Sempre cobrir o zero
🔁 Fazer até 2 proteções 

<a href="https://affiliates.nuts.bet/visit/?bta=37384&brand=nutsbet"><b>🔗 Cadastre-se antes de Jogar!</b></a>

<a href="https://nuts.bet/live-casino/game/2177465"><b>🏦Abra a roleta</b></a>
"""

def send_signal():

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 


    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)

    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)



def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = ["07:00", "12:00", "20:30","21:16"]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
