import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002012721862'

possibilidades_minas = [
"🔵",
"🔴"
     
 
]



texto4 = """
⚠️ Fique atento ao jogo ⚠️

🎲 BAC BO
🔎 identificando entrada

🖥 Link de cadastro:[Clique aqui](https://go.boasortebet.com/visit/?bta=35385&brand=boasortebet)
"""


texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""



mensagem = """
✅ Entrada Confirmada 

👉 Entrada:{}

⚠️ MÁXIMO 2 GALES 
🔔 Entrada Confirmada 🔔  
✅ Entrar Agora  

⏱️ Válido até: {}

📲: Plataforma correta: [Clique aqui](https://go.boasortebet.com/visit/?bta=35385&brand=boasortebet)
"""





print("=========")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
time.sleep(120) 



  
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(60)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
time.sleep(120) 
