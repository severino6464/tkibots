import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002060601382'

possibilidades_minas = [
"🔵",
"🔴"
     
 
]



texto4 = """
⚠️ Fique atento ao jogo ⚠️

🎲 Manccini Dados
🔎 identificando entrada


<a href="https://go.aff.bullsbetaffiliate.com/433v7x66">🔗 Clique aqui para jogar ✅</a>

"""


texto5 = """
✅GRENN DO MANCCINI 🙅🏽‍♂️
 
"""



mensagem = """
🔔Entrada Confirmada 🔔
👉 Entrada:{}
Cobrir Empate 🟤


⏱️ Válido até: {}

<a href="https://go.aff.bullsbetaffiliate.com/433v7x66">🔗 Clique aqui para jogar ✅</a>
"""





print("sala635")

bot.send_message(chat_id=group_id, text=texto4,parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120) 



  
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(60)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120) 