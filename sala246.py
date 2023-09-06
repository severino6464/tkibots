import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001932950543'



links = [
    "https://exemplo1.com",
]

mensagem = """
Lembrando galera, tô aqui para te ajudar…

Se depois de ter assistindo o tutorial completo que está fixado e ainda tiver alguma dúvida ou deu algum problema, me chama no privado pra eu te ajudar! 
👇🏼👇🏼👇🏼

CONVERSAR NO PRIVADO (https://t.me/Willfortuna_bot)
"""




print("BOT-aff245-nuts")
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
time.sleep(7200)
