import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002090621432'

sticker_file_id = 'CAACAgIAAxkBAAMmZSb_ngXS-jrJPaIDkQxNkCtYOQQAAtgLAAJYD5hKNPj69b5xWK8wBA'

possibilidades_minas = [
    "⭐️💣💣💣💣\n💣💣💣⭐️💣\n💣💣⭐️💣💣\n⭐️💣💣💣💣\n💣💣💣💣💣",
    "⭐️💣💣💣💣\n💣💣💣⭐️💣\n💣💣⭐️💣💣\n⭐️💣💣💣💣\n💣💣💣💣💣",
    "⭐️💣💣💣💣\n💣💣💣⭐️💣\n💣💣⭐️💣💣\n⭐️💣💣💣💣\n💣💣💣💣💣",
]

links = [
    "https://exemplo1.com",
]

mensagem = """
✅ <b>NUTSBET CONFIRMA</b> ✅
🔁 Tentativas: 3
🕐 Válido até: {}

{}

⚠️ Aposte com: 3 💣
SITE ➡️ <a href="https://affiliates.nuts.bet/visit/?bta=38017&brand=nutsbet"><b>Plataforma bugada</b></a>
"""

text2 = """
O último padrão mines passou da validade. 
Aguarde o próximo padrão!
  """

print("=====")

possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=3)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade , possibilidade_mina_aleatoria)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(120)
bot.send_message(chat_id=group_id, text=text2, parse_mode='HTML', disable_web_page_preview=True)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(480)
