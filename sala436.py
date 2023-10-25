import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001970951473'



links = [
    "https://exemplo1.com",
]


possibilidades_minas = [
    "1° e 2° dúzia",
    "1° e 3° dúzia",
    "2° e 3° dúzia"

]



texto4 = """
ATENÇÃO VAMOS INICIAR !
"""


mensagem = """
🔥 <b>Entrada: {}</b>
🛡 Ate duas proteções - Cobrir o zero!
🔗<a href="https://affiliates.nuts.bet/visit/?bta=36979&brand=nutsbet"> Cadastre-se antes de Jogar!</a>
🎯 Entrada confirmada 🎯 
 Roleta: ROLETA BRASILEIRA 🎰
"""

print("======")
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(600)