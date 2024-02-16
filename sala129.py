import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001868804456'  
texto4 = """

⚠️⚠️⚠️ ATENÇÃO PLATAFORMA EM LANÇAMENTO E TÃO DOBRANDO OS DEPÓSITOS ⚠️⚠️⚠️


[📱 Cadastre-se aqui](https://vexbet.tech/)
[LINK DA PLATAFORMA](https://vexbet.tech/)


"""

bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
time.sleep(12000) 
