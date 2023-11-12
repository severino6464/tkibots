import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002023633024'

sticker_file_id = 'CAACAgEAAxkBAAMCZSbmh4EopfmSJgx8Z8sDxkeWf1UAAvwAAzgOghFAju2fQymOBzAE'



texto1 = """
ATENÇÃO!

"""

texto2 = """
ENTRADA CONFIRMADA!
Validade: 3 minutos
"""

texto3 = """
ENTRADA ENCERRADA
"""


bot.send_message(chat_id=group_id, text=texto1, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(10)
bot.send_message(chat_id=group_id, text=texto2, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(180)
bot.send_message(chat_id=group_id, text=texto3, parse_mode='HTML', disable_web_page_preview=True)
