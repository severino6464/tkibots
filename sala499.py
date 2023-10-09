import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001977642982'

texto4 = """
⚠️ <b>OPORTUNIDADE IDENTIFICADA!</b> ⚠️
"""

texto5 = """
🥷🏻🍩 <b>Entrada Finalizada</b> 🍩🥷🏻
     ✅✅ <b>LUCROOO!</b> ✅✅
"""

mensagem = """
🥷🏻 <b>Entrada Confirmada!</b> 🍩

🎯 <b>Estratégia</b>: Minutos Pagantes
🔥 <b>Número de cortes</b>: {}

🕑 <b>HORÁRIOS PAGANTES</b>:

🍩{} - 🔪 {} cortes
🍩{} - 🔪 {} cortes
🍩{} - 🔪 {} cortes

<a href="https://go.aff.bullsbetaffiliate.com/p79vpxd3">🎰 <b>CADASTRE-SE PARA JOGAR</b></a>

Quem lucrou acima de R$ 10 reage aqui embaixo 👇
"""

n_jogadas = random.randint(2, 6)

entrada1 = datetime.datetime.now() + datetime.timedelta(minutes=2)
hora_validade1 = entrada1.strftime("%H:%M")
entrada2 = datetime.datetime.now() + datetime.timedelta(minutes=4)
hora_validade2 = entrada2.strftime("%H:%M")
entrada3 = datetime.datetime.now() + datetime.timedelta(minutes=6)
hora_validade3 = entrada3.strftime("%H:%M")

n_jogadas2 = random.randint(2, 6)
n_jogadas3 = random.randint(2, 6)
n_jogadas4 = random.randint(2, 6)


mensagem_formatada = mensagem.format(n_jogadas, hora_validade1, n_jogadas2, hora_validade2, n_jogadas3, hora_validade3, n_jogadas4)

print("=======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(1080)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(600)
