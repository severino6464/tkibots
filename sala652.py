import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001968919254'

sticker_file_id = 'CAACAgIAAxkBAAMfZSb4VppXyng9TmBwSA12Ss3y2hkAAhoDAAKc1ucKpX8qfdF9KAIwBA'

texto4 = """
🎲 Fique atento ao jogo 🎲

🐂 Fortune OX
🔎 Estamos validando uma entrada

<a href="https://affiliates.nuts.bet/visit/?bta=37951&brand=nutsbet">📱 Cadastre-se aqui</a>

🚨O sinal do robô só funciona apenas na plataforma acima! Faça💰🤑


"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""


mensagem = """
⚠️ ENTRADA CONFIRMADA ⚠️

🐂 Fortune OX

🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
🔹 {}X modo Normal
🔹 {}X modo Turbo
⏰ Sinal válido até: {}


🌪 Faça no máximo {} jogadas!

<a href="https://affiliates.nuts.bet/visit/?bta=37951&brand=nutsbet">📱 Cadastre-se aqui</a>

<a href="https://affiliates.nuts.bet/visit/?bta=37951&brand=nutsbet">📱 Jogar Fortune ox</a>

🚨O sinal do Robô só funciona apenas na plataforma acima! Faça💰🤑
"""

print("======")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60) 



   
n_jogadas = random.randint(1, 12)
n_jogadas2 = random.randint(1, 6)
n_jogadas3 = random.randint(1, 6)
n_jogadas4 = random.randint(1, 6)
validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(n_jogadas,n_jogadas2,n_jogadas3,hora_validade, n_jogadas4)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(120) 

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(120) 