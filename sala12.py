import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001952647599'

possibilidades_minas = [
"5.50x",
"4.70x",
"7.40x",
"3.10x",
"6.34x",
"4.50x",
"5.00x"
]



texto4 = """
⚠️ Fique atento ao jogo ⚠️

👨🏽‍🚀 Spaceman
🔎 identificando entrada

🖥 Link de cadastro:[Clique aqui](https://18kbet.online/player-from-agent/agent/167j6)
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


📲: Plataforma correta: [Clique aqui](https://18kbet.online/player-from-agent/agent/167j6)
"""

print("BOT-aff13-nuts")

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