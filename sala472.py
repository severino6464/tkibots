from distutils.cmd import Command
from doctest import testfile
import string
from turtle import st
import telebot
import time

from telebot import types
import threading

CHAVE_API = "6583137021:AAEOopzWOThN6VQ081Ir4CZD65NSdVXUoJo"

bot = telebot.TeleBot(CHAVE_API)

autorizar = 1
fluxo = {}

texto3 = """

Oii, tudo bem? 

Você está a um passo de começar a ganhar dinheiro comigo apenas jogando 🤭🤑

Para começar a faturar ainda HOJE clique no botão abaixo e compartilhe seu contato comigo 👇"""

texto4 = """
felipe luna aqui numero 1 do brasil neste mercado falando com voce para te ajudar a lucrar junto com nossa turma neste mercado mais antes da gente continuar clica no botao abaixo para fazer seu cadastro
"""

texto6 = """
Quando terminar o cadastro me avisa aqui"""

texto5 = """
Otimo! 🤩

Agora só falta mais um passo...

Clique no botão para entrar no grupo e começar a lucrar ainda hoje comigo
👇🤑
"""

texto7 = """
Clique no BOTÃO abaixo e faça o cadastro GRATUITAMENTE 👇"""

texto8 = """
Conseguiu realizar o cadastro?"""








def enviar_mensagem_fixada(chat_id):
    # Texto da mensagem fixada
    mensagem_fixada = "Para vincular sua conta do aplicativo na casa de apostas, clique em /start👇"

    # Enviar a mensagem fixada
    bot.send_message(chat_id, mensagem_fixada, disable_notification=True, pin=True)




def verificar(mensagem):
    global fluxo
    moment = mensagem.text
    idchat = mensagem.chat.id
    print(moment)
    print(idchat)

    if fluxo.get(idchat) is None:
        fluxo[idchat] = 1

    if fluxo[idchat] == 1:


        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button_contato = types.KeyboardButton("Enviar Contato", request_contact=True)
        markup.add(button_contato)
        bot.send_message(mensagem.chat.id, texto3, reply_markup=markup)

        time.sleep(20)

        bot.send_message(mensagem.chat.id, texto4)
        time.sleep(5)


        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("Cadastrar", url="https://onabet.cxclick.com/visit/?bta=36671&brand=onabet")
        markup.add(button)
        bot.send_message(mensagem.chat.id, texto7, reply_markup=markup)
        time.sleep(20)
       
        bot.send_message(mensagem.chat.id, texto6)
   
       
        fluxo[idchat] = 2

    elif fluxo[idchat] == 2:
        time.sleep(10)
        bot.send_message(mensagem.chat.id, texto8)

      



        fluxo[idchat] = 3

    elif fluxo[idchat] == 3:
        time.sleep(5)
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("ENTRAR NO GRUPO", url="https://t.me/playonabet")
        markup.add(button)
        bot.send_message(mensagem.chat.id, texto5, reply_markup=markup)




        fluxo[idchat] = 0
         # Enviar mensagem para o chat específico
        chat_id_especifico = 891227017
        mensagem_especifica = "Um usuário chegou ao final das mensagens."
        bot.send_message(chat_id_especifico, mensagem_especifica)

    return True

    


@bot.message_handler(func=verificar)
def responder(mensagem):
    return True


def handle_messages(messages):
    for message in messages:
        bot.process_new_messages([message])


def poll_updates():
    bot.polling(none_stop=True, interval=0, timeout=10)


if __name__ == "__main__":
    update_thread = threading.Thread(target=poll_updates)
    update_thread.start()