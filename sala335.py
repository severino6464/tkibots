import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001925684200'





mensagem = """
🚨 ENTRADA CONFIRMADA 🚨

🐯 Fortune Tiger 
⏰ Estratégia: Horários Pagantes
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

[🔗 Fazer CADASTRO ✅](https://affiliates.nuts.bet/visit/?bta=35945&brand=nutsbet)
[🔗 Abrir FORTUNE TIGER](https://affiliates.nuts.bet/visit/?bta=35945&brand=nutsbet)

Aposte agora e aumente suas chances de vitória! 💰
"""





print("aff335")

 


n_jogadas = random.randint(1, 10)
n_jogadas2 = random.randint(1, 10)
validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(600)  # Espera 10 minutos (600 segundos)

