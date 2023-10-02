import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001934170893'



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
ATENÇÃO VAMOS INICIAR !
"""


mensagem = """
🔥 ROBÔ CONFIRMOU 🔥
🎰 Roleta: Roulette Live

{}

👉 Cobrir o zero
🔁 Fazer até 3 gales
🔗 [Cadastre-se antes de Jogar!](https://affiliates.nuts.bet/visit/?bta=36804&brand=nutsbet)
🖥️[Jogue Aqui](https://affiliates.nuts.bet/visit/?bta=36804&brand=nutsbet)
⏱️ Válido até: {}
"""


print("BOT-aff80-nuts")
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
time.sleep(600)