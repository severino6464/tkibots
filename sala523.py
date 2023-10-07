import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001633098503'  

texto4 = """
⚠️ <b>A SESSÃO VAI SER INICIADA</b> ⚠️

🎲 Fique atento ao jogo 🎲

🐭 Fortune mouse

<a href="https://affiliates.nuts.bet/visit/?bta=37480&brand=nutsbet">📱 Cadastre-se aqui</a>
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""

texto6= """
🐭 <b>SESSÃO DO FORTUNE RABBIT ENCERRADA!</b> 🐭
"""

mensagem = """
⚠️ <b>ENTRADA CONFIRMADA</b> ⚠️

🐭 Fortune mouse 🐭

🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
⏰ Sinal válido até: {}

🌪 Faça no máximo {} jogadas!

<a href="https://affiliates.nuts.bet/visit/?bta=37480&brand=nutsbet">📱 Cadastre-se aqui</a>

<a href="https://affiliates.nuts.bet/visit/?bta=37480&brand=nutsbet">📱 Jogar Fortune mouse 🐭 </a>
"""

def send_signal():

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300) 
    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=4)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(240)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

    bot.send_message(chat_id=channel_id, text=texto6, parse_mode='HTML', disable_web_page_preview=True)



def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
    "16:30"
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
