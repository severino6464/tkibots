import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001969564248'





mensagem = """
🚨 ENTRADA CONFIRMADA 🚨

🐯 Fortune Tiger 
⏰ Estratégia: Horários Pagantes
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

[🔗 Fazer CADASTRO ✅](https://bcraft.g2afse.com/click?pid=370&offer_id=39)
[🔗 Abrir FORTUNE TIGER](https://bcraft.g2afse.com/click?pid=370&offer_id=39)

"""





print("aff242")

 


n_jogadas = random.randint(6, 20)
n_jogadas2 = random.randint(4, 20)
validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(600)  # Espera 10 minutos (600 segundos)
