import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001900457280'


text2 = """""
🤑 SINAL FINALIZADO 🤑

🍀 identificando novos padrões… 🕰

"""


mensagem = """
🚨SINAL APENAS PARA A NUTS BET 🚨

✅ENTRADA CONFIRMADA✅

🐯 Fortune Tiger 
⏰ Estratégia: Horários Pagantes
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

[🔗 Fazer CADASTRO ✅](https://affiliates.nuts.bet/visit/?bta=36079&brand=nutsbet)

"""



 


n_jogadas = random.randint(3, 10)
n_jogadas2 = random.randint(3, 10)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
time.sleep(345)  # Espera 10 minutos (600 segundos)

bot.send_message(chat_id=group_id, text=text2, parse_mode='Markdown')
    
time.sleep(120)

