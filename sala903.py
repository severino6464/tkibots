import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002089557138'

links = [
    "https://exemplo1.com",
]


possibilidades_minas = [
    "Apostar em números baixos [1-18]",
    "Apostar em números altos [19-36]",
    "Apostar na duzia 1 e 3",
    "Apostar na cor 🔴",
    "Apostar na cor ⚫"
]



texto4 = """
⚠️ <b>ATENÇÃO VAMOS INICIAR!</b> ⚠️
"""


mensagem = """
🔥 <b>ENTRADA CONFIRMADA!</b> 🔥
🎰 Roleta: Live

{}


👉 Cobrir o zero
🔁 Fazer até 3 gales

<a href="https://affiliates.nuts.bet/visit/?bta=38747&brand=nutsbet">🔗 Cadastre-se antes de Jogar!</a>

<a href="https://nuts.bet/live-casino/game/2186140">🖥 Jogue aqui!</a>

"""




print("======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60)
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120)

time.sleep(420)
