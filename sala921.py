import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002076063423'

possibilidades_minas = [
"‼️ RETIRAR EM 1.50x"
     
 
]



texto4 = """
⚠️ Fique atento ao jogo ⚠️

✈️ Aviator 
🔎 identificando entrada

<a href="https://affiliates.nuts.bet/visit/?bta=38752&brand=nutsbet"><b>🖥 Link de cadastro</b></a>
"""




mensagem = """
✅ Entrada Confirmada 

{}

⚠️ MÁXIMO 2 GALES 
🔔 Entrada Confirmada 🔔  
✅ Entrar Agora  

⏱️ Válido até: {}

<a href="https://affiliates.nuts.bet/visit/?bta=38752&brand=nutsbet"><b>🖥 Link de cadastro</b></a>
"""





print("=======")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120) 



  
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(60)  # Espera 5 minutos (300 segundos)
time.sleep(120) 
