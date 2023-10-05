import telebot
import time
from telebot import types




# Substitua 'SEU_TOKEN' pelo token do seu bot do Telegram
bot = telebot.TeleBot('6583137021:AAEOopzWOThN6VQ081Ir4CZD65NSdVXUoJo')

# Variável de estado para controlar o fluxo da conversa
state = {}



texto1 = """

Oii, tudo bem? 

Você está a um passo de começar a ganhar dinheiro comigo apenas jogando 🤭🤑

Para começar a faturar ainda HOJE clique no botão abaixo e compartilhe seu contato comigo 👇"""

texto2 = """
felipe luna aqui numero 1 do brasil neste mercado falando com voce para te ajudar a lucrar junto com nossa turma neste mercado mais antes da gente continuar clica no botao abaixo para fazer seu cadastro
"""

texto3 = """
Otimo! 🤩

Agora só falta mais um passo...

Clique no botão para entrar no grupo e começar a lucrar ainda hoje comigo
👇🤑
"""

# Comando /start para iniciar o fluxo
@bot.message_handler(commands=['start'])
def start(message):

    state[message.chat.id] = 1  

   
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_contato = types.KeyboardButton("Enviar Contato", request_contact=True)
    markup.add(button_contato)
    bot.send_message(message.chat.id, texto1, reply_markup=markup)
   

@bot.message_handler(func=lambda message: state.get(message.chat.id) == 1)
def handle_message1(message):
    state[message.chat.id] = 2  # Avança para o próximo estado
   
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Cadastrar", url="https://onabet.cxclick.com/visit/?bta=36671&brand=onabet")
    markup.add(button)
    bot.send_message(message.chat.id,texto2,reply_markup=markup)
    time.sleep(20)

@bot.message_handler(func=lambda message: state.get(message.chat.id) == 2)
def handle_message2(message):
    state[message.chat.id] = 3
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("ENTRAR NO GRUPO", url="https://t.me/playonabet")
    markup.add(button)
    bot.send_message(message.chat.id, texto3,reply_markup=markup)


    chat_id_especifico = 891227017
    mensagem_especifica = "Um usuário chegou ao final das mensagens."
    bot.send_message(chat_id_especifico, mensagem_especifica)
    state[message.chat.id] = 0  # Reinicia o estado
   


# Iniciar o bot
bot.polling()
