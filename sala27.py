import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # Replace with your Telegram Bot API key

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001870896395'  # Replace with your channel ID

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

mensagem = """
💰 ENTRADA CONFIRMADA 💰
🎲 Estratégia: Repetição de Coluna 1
🎰 Roleta: 
✅ Entrada mínima: 0.5

{}

👉 Cobrir o zero
🔁 Fazer até 3 gales
🔗 [Cadastre-se antes de Jogar!](https://affiliates.nuts.bet/visit/?bta=35677&brand=nutsbet)
⏱️ Válido até: {}
"""

def send_signal():
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    link_aleatorio = random.choice(links)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
    mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='Markdown')
    time.sleep(60)

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "10:00", "10:10", "10:20", "10:30",
        "15:00", "15:15", "15:30", "15:45",
        "16:00", "20:00", "20:15", "20:30", "20:45", "21:00"
    ]

    if current_time in signal_times:
        send_signal()

try:
    check_and_send_signal()
    # Wait for 1 minute before checking the time again
    datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
    print(f"Error occurred: {str(e)}")
