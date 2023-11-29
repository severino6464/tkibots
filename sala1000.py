import telebot
import time
import datetime
import random

CHAVE_API = "5939971508:AAE_Al4i1Hf7CnHSMU_VaGG-jTr_FRdd9eQ" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001943077650'





mensagem = """
🚨 ENTRADA CONFIRMADA 🚨

🐯 Fortune Tiger 
⏰ Estratégia: Horários Pagantes
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

[🔗 Fazer CADASTRO ✅](=========)
[🔗 Abrir FORTUNE TIGER](https://nuts.bet/casino/game/2180615)

"""





print("========")

 


n_jogadas = random.randint(6, 20)
n_jogadas2 = random.randint(4, 20)
validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(6)  # Espera 10 minutos (600 segundos)
