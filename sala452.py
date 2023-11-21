import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001869121732'  

texto4 = """
🐯💎<b>ATENÇÃO SESSÃO DO TIGER VAI INICIAR EM 5 MINUTOS</b>💎🐯

<a href="https://go.aff.br4-partners.com/w1pjlefq?campaign_id=1834">📱 CADASTRE-SE AQUI</a>
"""

texto5 = """
<b>✅🤑BATEUUUU🤑✅</b>
"""

texto6= """
🐯 <b>SESSÃO DO FORTUNE TIGER ENCERRADA!</b> 🐯
"""

mensagem = """
🔮Entrada Confirmada🔮

🐯 FORTUNE TIGER ☘️
🔥 Jogadas: {}
⏰ Válido até: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

🌪 Faça no máximo {} jogadas!

<a href="https://go.aff.br4-partners.com/w1pjlefq?campaign_id=1834">📱 CADASTRE-SE AQUI</a>

<a href="https://go.aff.br4-partners.com/w1pjlefq?campaign_id=1834">📱 ABRIR FORTUNE TIGER🐯☘️</a>
"""

def send_signal():

    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300) 
    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 15)
    n_jogadas3 = random.randint(4, 20)
    n_jogadas4 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas3, n_jogadas4, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(480)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(420)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 15)
    n_jogadas3 = random.randint(4, 20)
    n_jogadas4 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas3, n_jogadas4, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(480)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(420)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 15)
    n_jogadas3 = random.randint(4, 20)
    n_jogadas4 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas3, n_jogadas4, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(480)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(30)

    bot.send_message(chat_id=channel_id, text=texto6, parse_mode='HTML', disable_web_page_preview=True)



def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00" 
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
