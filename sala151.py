import telebot
import time
import threading
import datetime
import random
import sys
import os
from telebot import types

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" #token fox

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001951898336'

caminho_arquivo = "C:/Users/neto/Desktop/gp-mines01.py"

texto4 = """
🐯 Atenção! Tigre saindo da jaula…
🤑 Sinais em breve, se prepare!   

🐯💰🐯💰🐯💰🐯💰🐯💰🐯💰🐯
"""

mensagem2 = """

✅✅✅ VITÓRIA!!! ✅✅✅
🕑 Finalizado às: {}
🐯☘🐯☘🐯☘🐯☘🐯☘🐯☘🐯☘

   """



mensagem = """
🚨 𝗘𝗡𝗧𝗥𝗔𝗗𝗔 𝗖𝗢𝗡𝗙𝗜𝗥𝗠𝗔𝗗𝗔 🚨

🐯 [Fortune Tiger]()
⚠️ Sinal 𝗩𝗮́𝗹𝗶𝗱𝗼 até:{}
⭐️ 𝗠𝗮́𝘅𝗶𝗺𝗼 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: 20

💰 {}X normal 
🔃 Intercalando
⚡️ {}X Turbo


📲: Plataforma correta: [Clique aqui](https://iluck.bet/?c=rafael999)

"""


valores_botoes = {
    '1': 7,
    '2': 4,
    '3': 1,
    '4': 3
}




#------------------------------------------

def reiniciar_programa():
    python = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)
    time.sleep(10)  # Pausa de 10 segundos
    os.execl(python, *args)

#--------------------------------------------------




def criar_teclado():
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    row_buttons = []

    emoji_dict = {
        '1': '🔥',
        '2': '👏🏻',
        '3': '👍',
        '4': '❤️'
    }

    for button, valor in valores_botoes.items():
        emoji = emoji_dict.get(button, '')
        button_text = '{} {}'.format(emoji, valor)
        row_buttons.append(types.InlineKeyboardButton(text=button_text, callback_data=button))

    keyboard.add(*row_buttons)
    return keyboard



def enviar_mensagem():
    keyboard = criar_teclado()

    validade2 = datetime.datetime.now() + datetime.timedelta(minutes=0)
    hora_validade2 = validade2.strftime("%H:%M")
    mensagem_formatada2 = mensagem2.format(hora_validade2)
    bot.send_message(chat_id=group_id, text=mensagem_formatada2,reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    button = call.data
    if button in valores_botoes:
        time.sleep(10)
        valores_botoes[button] += 2
        

        if valores_botoes[button] >= 14:
            valores_botoes[button] = 6

        keyboard = criar_teclado()
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)

def enviar_periodicamente():
    while True:
        try:
            n_jogadas = random.randint(6, 13)
            n_jogadas2 = random.randint(4, 15)
            validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
            hora_validade = validade.strftime("%H:%M")
            mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

            bot.send_message(chat_id=group_id, text=texto4 ,parse_mode='Markdown')
            print("BOT-TIGER-henrique")
       
            time.sleep(60)  # Aguarda 1 minuto

        
            bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
       
            time.sleep(240)  # Espera 5 minutos (300 segundos)

            enviar_mensagem() 

            time.sleep(120)
        
        
        except Exception as e:
            print("Ocorreu um erro fatal:", e)
            print("REINICIANDO O PROGRAMA")
            reiniciar_programa()

# Inicia um thread separado para enviar a mensagem periodicamente
thread_envio = threading.Thread(target=enviar_periodicamente)
thread_envio.start()

bot.polling()
