import telebot
import time
import threading
import datetime
import random
import sys
import os
from telebot import types

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX
bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001943077650'



texto4 = """
🧙‍♂️ Fique atento o Mago Achou uma entrada 🧙‍♂️
💣 Mines 
🔎 Estamos validando
🖥 Link de cadastro:<a href="https://affiliates.nuts.bet/visit/?bta=36156&brand=nutsbet">🔗 Fazer CADASTRO ✅</a>
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 """

possibilidades_minas = [
    "💣💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",

    "💣💣⭐️⭐️⭐️\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣",

    "⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",

    "💣💣💣⭐️⭐️\n💣💣💣⭐️💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",

    "⭐️💣⭐️💣⭐️\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣⭐️💣💣💣\n💣💣⭐️💣💣",

    "⭐️💣⭐️💣⭐️\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "💣⭐️💣💣💣\n⭐️⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣",
    "💣⭐️💣💣⭐️\n⭐️💣⭐️💣💣\n💣💣💣⭐️💣\n💣💣💣💣💣\n💣💣⭐️💣💣",
    "⭐️💣⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "💣💣💣💣💣\n💣⭐️💣💣⭐️\n⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣",
    "⭐️⭐️💣💣💣\n💣⭐️💣💣💣\n💣💣⭐️⭐️💣\n💣💣💣💣💣\n💣💣💣💣💣",
    "⭐️⭐️💣⭐️💣\n💣💣💣💣💣\n⭐️💣💣⭐️💣\n💣💣💣💣💣\n💣⭐️💣💣💣",
    "⭐️💣⭐️⭐️💣\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣⭐️💣💣💣\n💣⭐️💣💣💣",
    "⭐️💣💣⭐️💣\n⭐️💣💣💣💣\n💣⭐️💣⭐️💣\n💣⭐️💣💣💣\n💣💣💣⭐️💣",
    "💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣⭐️⭐️\n💣⭐️💣⭐️💣\n💣💣💣⭐️💣",
    "⭐️💣⭐️⭐️💣\n⭐️💣💣⭐️💣\n💣⭐️💣⭐️⭐️\n💣💣💣💣💣\n⭐️💣⭐️💣⭐️",
    "⭐️💣💣💣⭐️\n💣💣💣💣💣\n⭐️💣💣⭐️💣\n💣💣💣⭐️⭐️\n💣💣💣⭐️💣",
    "💣💣💣💣💣\n💣💣💣⭐️⭐️\n⭐️💣💣⭐️⭐️\n⭐️💣⭐️⭐️💣\n⭐️💣💣⭐️💣",
    "⭐️💣⭐️⭐️💣\n💣⭐️💣💣⭐️\n⭐️💣💣💣⭐️\n💣💣💣⭐️💣\n💣💣💣⭐️💣"
 
]




mensagem = """
🧙‍♂️ Entrada confirmada 🧙‍ 
🥇: Entrada 

{}
  
🎮: Tentativas: 2
Jogar com 2 a 3 minas
📲: Plataforma correta: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=36156&brand=nutsbet)
👉🏻: Link do jogo: [Mines](https://nuts.bet/casino/game/2172765?provider=Spribe)
⏱️ Válido até: {}
"""
links = [
    "https://exemplo1.com",
   
]


valores_botoes = {
    '1': 7,
    '2': 4,
    '3': 1,
    '4': 3
}






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

    bot.send_message(chat_id=group_id, text=texto5, reply_markup=keyboard)


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

    try:
        possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
        link_aleatorio = random.choice(links)
        validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
        hora_validade = validade.strftime("%H:%M")
        mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
        mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
        mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

        bot.send_message(chat_id=group_id, text=texto4 ,parse_mode='HTML', disable_web_page_preview=True)
        print("Omagodomines")
       
        time.sleep(120)  

        
        bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
       
        time.sleep(120) 

        enviar_mensagem() 

        time.sleep(300)
        
        
    except Exception as e:
       
        print("Erro")
       

# Inicia um thread separado para enviar a mensagem periodicamente
thread_envio = threading.Thread(target=enviar_periodicamente)
thread_envio.start()

bot.polling()