import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001987054108'

possibilidades_minas = [
"❌❌❌\n❌🙎🏻‍♂️⚽️",
"❌⚽️❌\n❌🙎🏻‍♂️❌",
"❌❌❌\n⚽️🙎🏻‍♂️❌",
"❌❌⚽️\n❌🙎🏻‍♂️❌",
"❌⚽️❌\n❌🙎🏻‍♂️❌",
"⚽️❌❌\n❌🙎🏻‍♂️❌"
     
 
]



texto4 = """
⚠️ Fique atento ao jogo ⚠️

⚽️ Penalty shoot out 
🔎 identificando entrada

🖥 Link de cadastro:[Clique aqui](https://affiliates.nuts.bet/visit/?bta=37072&brand=nutsbet)
"""


texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""



mensagem = """
🎲 Entrada confirmada 🎲

🥇: Entrada 

{}
  
🎮: Tentativas: 3
⏱️ Válido até: {}

📲: Plataforma correta: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=37072&brand=nutsbet)
"""




print("=======")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
time.sleep(120) 



  
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(60)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
time.sleep(120) 