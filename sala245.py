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
Se você é novo ou nova aqui e já quer começar a ganhar dinheiro comigo, clica aqui 👇🏼 e faça seu cadastro gratuito! 👇🏼

➡️ [CLIQUE AQUI E CADASTRE-SE](https://affiliates.nuts.bet/visit/?bta=36034&brand=nutsbet)  ⬅️

Após realizar seu cadastro assista esse vídeo passo a passo que preparei pra você, eu te ensino tudo que precisa saber 👇🏼

📱[CLIQUE AQUI PRA ASSISTIR O MINICURSO GRATUITO](https://t.me/c/1932950543/52)

Depois de seguir todos esses passos, faz o seu depósito, prepara sua banca e vem por dinheiro no bolso comigo! 🤑
"""




print("BOT-aff245-nuts")
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
time.sleep(3600)
