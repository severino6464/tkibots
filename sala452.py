import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001944503081'





mensagem = """
🚨 ENTRADA CONFIRMADA 🚨

🍀 Lucky Neko
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

[🔗 Fazer CADASTRO ✅](https://bit.ly/3LDnAAn)
[🔗 Abrir FORTUNE TIGER](https://bit.ly/3LDnAAn)

"""





print("========")

 


n_jogadas = random.randint(6, 20)
n_jogadas2 = random.randint(4, 20)
validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(600)  # Espera 10 minutos (600 segundos)

