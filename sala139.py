import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001962047779'





mensagem = """
🚨 ENTRADA CONFIRMADA 🚨

🐯 Fortune Tiger 
⏰ Estratégia: Horários Pagantes
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

[🔗 Fazer CADASTRO ✅](https://affiliates.nuts.bet/visit/?bta=36012&brand=nutsbet)
[🔗 Abrir FORTUNE TIGER](https://nuts.bet/casino/game/2180615)

"""



while True:

    print("139")

 


    n_jogadas = random.randint(6, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas)

    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(600)  # Espera 10 minutos (600 segundos)

