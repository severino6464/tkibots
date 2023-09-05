import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001935348815'


texto4 = """
💎ENCONTRANDO FALHA NA MATRIX...💎
🐯POSSÍVEL ENTRADA EM 2 MINUTOS

[📱 CADASTRE-SE AQUI](http://bit.ly/cadastrofortuneassertivepkg)
"""

texto5 = """
🔮 DINHEIRO NO BOLSO 🔮
        ✅✅ GRENN! ✅✅
"""


mensagem = """
🔮 MATRIX QUEBRADA🔮

🐯 FORTUNE TIGER ☘️
🎯 Estratégia: Multiplicador de 100x
🔥 Jogadas: {}
⏰ Válido até: {}

🌪 Faça no máximo {} jogadas!

[📱 CADASTRE-SE AQUI](http://bit.ly/cadastrofortuneassertivepkg)

[ 📱 ABRIR FORTUNE TIGER🐯☘️](http://bit.ly/cadastrofortuneassertivepkg)
"""
print("BOT-aff229-nuts")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
time.sleep(120) 



n_jogadas = random.randint(2, 10)
validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(60)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
time.sleep(120) 
