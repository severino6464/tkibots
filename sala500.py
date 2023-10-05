import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001977464309'  

texto4 = """
🚨🍀 ATENÇÃO VAMOS INICIAR OS SINAIS DO LUCKY NEKO 🍀🚨

FAÇA SEU CADASTRO 👇
<a href="https://go.aff.br4-partners.com/w1pjlefq">🔗 Fazer CADASTRO </a>

"""

mensagem = """
🚨 ENTRADA CONFIRMADA 🚨

🍀 Lucky Neko
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

<a href="https://go.aff.br4-partners.com/w1pjlefq">🔗 Fazer CADASTRO ✅</a>
<a href="https://go.aff.br4-partners.com/w1pjlefq">🔗 Abrir FORTUNE TIGER</a>

"""

texto5 = """
🍀🍀 <b>Entradas Finalizadas</b> 🍀🍀
     ✅✅ <b>SÓÓÓ LUCROOO!</b> ✅✅

"""

texto6 = """
🍀 <b>SESSÃO DO LUCKY NEKO ENCERRADA!</b> 🍀

"""

def send_signal():
    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300) 

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade, n_jogadas, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, pparse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(780)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade, n_jogadas, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, pparse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(780)

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade, n_jogadas, n_jogadas2)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, pparse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(30)
    bot.send_message(chat_id=channel_id, text=texto6, parse_mode='HTML', disable_web_page_preview=True)


def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "02:00", "05:00", "08:00", "11:00", "14:00", "17:00", "20:00", "23:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
    check_and_send_signal()
    # Wait for 1 minute before checking the time again
    datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
    print(f"Error occurred: {str(e)}")
