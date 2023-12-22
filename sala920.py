import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1002144551821'

possibilidades_minas = [
    "Apostar em números baixos [1-18]",
    "Apostar em números altos [19-36]",
    "Apostar na duzia 1 e 3",
    "Apostar na cor 🔴",
    "Apostar na cor ⚫"
]



sticker_file_id = 'CAACAgIAAxkBAAMmZSb_ngXS-jrJPaIDkQxNkCtYOQQAAtgLAAJYD5hKNPj69b5xWK8wBA'

texto4 = """
⚠️ <b>ATENÇÃO VAMOS INICIAR</b> ⚠️

<a href="https://affiliates.nuts.bet/visit/?bta=38914&brand=nutsbet"><b>🔗 Cadastre-se antes de Jogar!</b></a>

<a href="https://nuts.bet/live-casino/game/2183643"><b>🏦 Abra a roleta</b></a>
"""

texto5 = """
✅✅ <b>ENTRADA ENCERRADA!</b> ✅✅
"""


mensagem = """
💰 ANALISTA CONFIRMOU 💰
🎰 Roleta: American

{}

⏱️ Válido até: {}
⚠️ Sempre cobrir o zero
🔁 Fazer até 2 proteções


<a href="https://affiliates.nuts.bet/visit/?bta=38914&brand=nutsbet"><b>🔗 Cadastre-se antes de Jogar!</b></a>

<a href="https://nuts.bet/live-casino/game/2183643"><b>🏦Abra a roleta</b></a>
"""



print("======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60)
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120)
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(20)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(400)
