import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # Replace with your Telegram Bot API key

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001935348815'  

possibilidades_minas = [
    "Apostar em números baixos [1-18]",
    "Apostar em números altos [19-36]",
    "Apostar na duzia 1 e 3",
    "Apostar na cor 🔴",
    "Apostar na cor ⚫"
]

links = [
    "https://exemplo1.com",
]


texto4 = """
💎ENCONTRANDO FALHA NA MATRIX...💎
🐯POSSÍVEL ENTRADA EM 2 MINUTOS

[📱 CADASTRE-SE AQUI](http://bit.ly/cadastrofortuneassertivepkg)
"""

texto5 = """
✅🤑BATEUUUU🤑✅
CONSEGUIU PEGAR? Manda o print @suportevippkg
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

def send_signal():
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
 



    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 



    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
 



    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 



    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(600)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
 



    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 



    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(120)
    
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='Markdown')






def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "10:00", "14:00", "18:16", "23:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
    check_and_send_signal()
    # Wait for 1 minute before checking the time again
    datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
    print(f"Error occurred: {str(e)}")