import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002028262476'


texto4 = """
⚠️ <b>OPORTUNIDADE IDENTIFICADA!</b> ⚠️
"""



mensagem = """
🔔 <b>ENTRADA QUEENFIRMADA!</b> 🔔
🖥 Mesa: <a href="#"><b>Football Studio</b></a>

🕑 <b>HORÁRIOS PAGANTES</b>:

{}
{}
{}
{}
{}
{}
{}

💰 Apostar apenas em empates

🚨 Cobrir o empate com 10% da aposta

<a href="https://affiliates.nuts.bet/visit/?bta=39016&brand=nutsbet">🎰 <b>CLIQUE E CADASTRE-SE NA PLATAFORMA</b></a>
"""



print("=======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120) 

entrada1 = datetime.datetime.now() + datetime.timedelta(minutes=1)
hora_validade1 = entrada1.strftime("%H:%M")
entrada2 = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade2 = entrada2.strftime("%H:%M")
entrada3 = datetime.datetime.now() + datetime.timedelta(minutes=8)
hora_validade3 = entrada3.strftime("%H:%M")
entrada4 = datetime.datetime.now() + datetime.timedelta(minutes=11)
hora_validade4 = entrada4.strftime("%H:%M")
entrada5 = datetime.datetime.now() + datetime.timedelta(minutes=14)
hora_validade5 = entrada5.strftime("%H:%M")
entrada6 = datetime.datetime.now() + datetime.timedelta(minutes=17)
hora_validade6 = entrada6.strftime("%H:%M")
entrada7 = datetime.datetime.now() + datetime.timedelta(minutes=21)
hora_validade7 = entrada7.strftime("%H:%M")

mensagem_formatada = mensagem.format(hora_validade1,hora_validade2,hora_validade3, hora_validade4, hora_validade5, hora_validade6, hora_validade7)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(1200)
time.sleep(600)
