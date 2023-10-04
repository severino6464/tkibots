import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001953285155'


texto4 = """
⚠️ ATENÇÃO VAMOS INICIAR ⚠️

🔎 Estamos validando uma entrada

[📱 Cadastre-se aqui](https://ninjacrash.net/sinais)

🚨O sinal só funciona apenas na plataforma acima!
"""


texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 Você que fez GREEN envie um print no @suportereidossinais1
"""



mensagem = """
🥷🏻  Entrada Confirmada! 🍩

🎯 Estratégia: Minutos Pagantes
🔥 Número de cortes: {}

🕑 HORÁRIOS PAGANTES:

🍩{}
🍩{}
🍩{}
🍩{}
🍩{}
🍩{}
🍩{}


<a href="https://bit.ly/REGISTRONINJA">🎰 CADASTRE-SE PARA JOGAR:</a>

<a href="https://bit.ly/APRENDAJOGAR">🎰 NÃO SABE JOGAR? APRENDA AGORA!</a>
"""



print("=======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
time.sleep(120) 

n_jogadas = random.randint(2, 6)

entrada1 = datetime.datetime.now() + datetime.timedelta(minutes=1)
hora_validade1 = entrada1.strftime("%H:%M")
entrada2 = datetime.datetime.now() + datetime.timedelta(minutes=3)
hora_validade2 = entrada2.strftime("%H:%M")
entrada3 = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade3 = entrada3.strftime("%H:%M")
entrada4 = datetime.datetime.now() + datetime.timedelta(minutes=8)
hora_validade4 = entrada4.strftime("%H:%M")
entrada5 = datetime.datetime.now() + datetime.timedelta(minutes=11)
hora_validade5 = entrada5.strftime("%H:%M")
entrada6 = datetime.datetime.now() + datetime.timedelta(minutes=14)
hora_validade6 = entrada6.strftime("%H:%M")
entrada7 = datetime.datetime.now() + datetime.timedelta(minutes=17)
hora_validade7 = entrada7.strftime("%H:%M")

mensagem_formatada = mensagem.format(n_jogadas, hora_validade1,hora_validade2,hora_validade3, hora_validade4, hora_validade5, hora_validade6, hora_validade7)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(1860)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')