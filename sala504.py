import telebot
import time
from telebot import types




# Substitua 'SEU_TOKEN' pelo token do seu bot do Telegram
bot = telebot.TeleBot('6583137021:AAEOopzWOThN6VQ081Ir4CZD65NSdVXUoJo')

# Variável de estado para controlar o fluxo da conversa
state = {}


texto0 = """
.
"""
texto1 = """
Faaaala comigo, Felipe Luna aquii!

Antes de tudo você precisa se cadastrar nesse link grátis, porque nossa inteligência artificial está ligada nesse site… FAZ SEU CADASTRO E ME CHAMA AQUI👇"""


texto2 = """
Showw!! 🤩

Agora só falta mais um passo...
Clique no botão abaixo e entre no grupo gratuito para começar a ganhar dinheiro ainda hoje comigo!! 🤑

"""

texto3 = """
Para você poder pegar os meus sinais de forma GRATUITA e lucrar comigo, você precisa fazer o seu cadastro...
Clica no botão abaixo e realize o seu cadastro de forma gratuita. 👇
"""

texto4 = """
CADASTRE AGORA E GANHE 🎁 

"""

texto5 = """
Perfeito!! Então bora ganhar dinheiro agora!! 🤑

Tô te mandando meu curso para você aprender a pegar os meus sinais dentro do grupo.

Assista com atenção e após você finalizar estará pronto pra lucrar comigo. 🤩🤑

Toque no botão abaixo para você ser direcionado para o curso gratuito. 👇

"""

texto6 = """"
Para ganhar dinheiro comigo ainda hoje você precisa estar dentro do grupo do Telegram.

"""

texto9 = """"
teste okk"""

# Comando /start para iniciar o fluxo
@bot.message_handler(commands=['start'])
def start(message):

    state[message.chat.id] = 1  

   
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Cadastrar", url="https://onabet.cxclick.com/visit/?bta=36671&brand=onabet")
    markup.add(button)
    bot.send_message(message.chat.id,texto1,reply_markup=markup)
    time.sleep(10)

   

    markup = types.InlineKeyboardMarkup()
    sim_button = types.InlineKeyboardButton("Sim, ja FIZ 👍", callback_data='sim')
    nao_button = types.InlineKeyboardButton("Ainda NÃ0 fiz", callback_data='nao')
    markup.row(sim_button, nao_button)
    bot.send_message(message.chat.id, "Eai, já se cadastrou??", reply_markup=markup)





@bot.callback_query_handler(func=lambda call: state.get(call.message.chat.id) == 1)
def handle_callback_query(call):
    if call.data == 'sim':

        
        
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("ACESSAR GRUPO AGORA ", url="https://t.me/playonabet")
        markup.add(button)
        bot.send_message(call.message.chat.id,texto2,reply_markup=markup)

        time.sleep(10)

        markup = types.InlineKeyboardMarkup()
        sim1_button = types.InlineKeyboardButton("Já estou no Grupo 🤑", callback_data='sim')
        nao1_button = types.InlineKeyboardButton("Ainda não Entrei 😞", callback_data='nao')
        markup.row(sim1_button, nao1_button)
        bot.send_message(call.message.chat.id, "Eai já ta no grupo??", reply_markup=markup)





        state[call.message.chat.id] = 2  

    elif call.data == 'nao':
       
        
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(texto4, url="https://onabet.cxclick.com/visit/?bta=36671&brand=onabet")
        markup.add(button)
        bot.send_message(call.message.chat.id,texto3,reply_markup=markup)

        state[call.message.chat.id] = 2  # Reinicie o estado


        time.sleep(10)

        markup = types.InlineKeyboardMarkup()
        sim1_button = types.InlineKeyboardButton("Já estou no Grupo 🤑", callback_data='sim')
        nao1_button = types.InlineKeyboardButton("Ainda não Entrei 😞", callback_data='nao')
        markup.row(sim1_button, nao1_button)
        bot.send_message(call.message.chat.id, "Eai já ta no grupo??", reply_markup=markup)










@bot.callback_query_handler(func=lambda call: state.get(call.message.chat.id) == 2)
def handle_callback_query(call):
    if call.data == 'sim':

     
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("ACESSAR  ", url="https://t.me/playonabet")
        markup.add(button)
        bot.send_message(call.message.chat.id,texto5,reply_markup=markup)



        state[call.message.chat.id] = 0  

    elif call.data == 'nao':

      
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("Clica no botão abaixo e acesse o grupo enquanto ainda está gratuito. 👇 ", url="https://t.me/playonabet")
        markup.add(button)
        bot.send_message(call.message.chat.id,texto6,reply_markup=markup)
       
       

        state[call.message.chat.id] = 0  # Reinicie o estado









# Iniciar o bot
bot.polling()
