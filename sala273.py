import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002133875158'

possibilidades_minas = [
"1.50x",
"2.50x",
"1.40x",
"2.10x",
"2.34x",
"1.70x",
"2.00x"
]



texto4 = """
⚠️ Fique atento ao jogo ⚠️

👨🏽‍🚀 Spaceman
🔎 identificando entrada

🖥 Link de cadastro:[Clique aqui](https://go.boasortebet.com/visit/?bta=35949&brand=boasortebet)
"""


texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""



mensagem = """
✅ Entrada Confirmada 

Entrar apos:

{}
{}
{}

✅ Sair em {}
⚠️ MÁXIMO 3 GALE 


📲: Plataforma correta: [Clique aqui](https://go.boasortebet.com/visit/?bta=35949&brand=boasortebet)
"""
print("=======")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
time.sleep(60) 



entrada1 = datetime.datetime.now() + datetime.timedelta(minutes=1)
hora_validade1 = entrada1.strftime("%H:%M")
entrada2 = datetime.datetime.now() + datetime.timedelta(minutes=3)
hora_validade2 = entrada2.strftime("%H:%M")
entrada3 = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade3 = entrada3.strftime("%H:%M")

validade = datetime.datetime.now() + datetime.timedelta(minutes=3)
hora_validade = validade.strftime("%H:%M")

possibilidade_mina_aleatoria = random.choice(possibilidades_minas)


mensagem_formatada = mensagem.format(hora_validade1,hora_validade2,hora_validade3,possibilidade_mina_aleatoria,)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(400)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
time.sleep(200) 
