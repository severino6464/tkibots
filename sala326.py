import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001924828186'

possibilidades_minas = [
"‼️ RETIRO EN 1.50x",
"‼️ RETIRO EN 2.00x",
"‼️ RETIRO EN 2.00x",
"‼️ RETIRO EN 3.50x",
"‼️ RETIRO EN 1.04x",
"‼️ RETIRO EN 2.30x",
"‼️ RETIRO EN 5.00x"
     
 
]



texto4 = """

⚠️ Estén atentos al juego ⚠️

✈️ aviador
🔎 identificación de entrada

🖥 Enlace de registro: [Haga clic aquí](https://sshortly1.com/YaRn0A)
"""


texto5 = """
🔷🔹 Entrada Terminada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""



mensagem = """
✅ Entrada Confirmada 

{}

⚠️ MÁXIMO 2 GALES
🔔 Entrada Confirmada 🔔
✅ Iniciar sesión ahora

⏱️ Válido hasta: {}

📲: Plataforma correcta: [Haga clic aquí](https://sshortly1.com/YaRn0A
"""





print("BOT-02-gustavo")

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