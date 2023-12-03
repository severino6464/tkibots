import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001622316632'

possibilidades_minas = [
    "Apostar em números baixos [1-18]",
    "Apostar em números altos [19-36]",
    "Apostar na duzia 1 e 3",
    "Apostar na cor 🔴",
    "Apostar na cor ⚫"
]


texto4 = """
⚠️ <b>OPORTUNIDADES IDENTIFICADAS!</b> ⚠️
"""

texto5 = """
     <b>Entradas Finalizadas!!!!</b>
✅✅ <b>LUCROOO!</b> ✅✅
"""

# Estrutura de dados para os animais
animais = [
    {
        'nome': 'Roleta Brasileira',
        'mensagem': """
🔥 <b>ROBÔ CONFIRMOU</b> 🔥
🎰 Roleta: Brasileira

{}

⏱️ Válido até: {}

👉 Cobrir o zero
🔁 Fazer até 3 gales

<a href="https://affiliates.nuts.bet/visit/?bta=38796&brand=nutsbet">🔗 Cadastre-se antes de Jogar!</a>

<a href="https://nuts.bet/live-casino/game/2177465">🖥 Jogue aqui!</a>
"""
    },
    {
        'nome': 'American Roulette',
        'mensagem': """
🔥 <b>ROBÔ CONFIRMOU</b> 🔥
🎰 Roleta: American Roulette

{}

⏱️ Válido até: {}

👉 Cobrir o zero
🔁 Fazer até 3 gales

<a href="https://affiliates.nuts.bet/visit/?bta=38796&brand=nutsbet">🔗 Cadastre-se antes de Jogar!</a>

<a href="https://nuts.bet/live-casino/game/2177465">🖥 Jogue aqui!</a>
"""
    },
    {
        'nome': 'Mega Fire Blaze Roullete Live',
        'mensagem': """
🔥 <b>ROBÔ CONFIRMOU</b> 🔥
🎰 Roleta: Mega Fire Blaze Roullete Live

{}

⏱️ Válido até: {}

👉 Cobrir o zero
🔁 Fazer até 3 gales

<a href="https://affiliates.nuts.bet/visit/?bta=38796&brand=nutsbet">🔗 Cadastre-se antes de Jogar!</a>

<a href="https://nuts.bet/live-casino/game/2177465">🖥 Jogue aqui!</a>
"""
    }
]

print("=======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60)

# Itera sobre os animais e envia as mensagens
for animal in animais:
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")

    mensagem_formatada = animal['mensagem'].format(
        possibilidade_mina_aleatoria, hora_validade)

    bot.send_message(chat_id=group_id, text=mensagem_formatada,
                     parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(480)
