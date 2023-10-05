import telebot

# Substitua 'SEU_TOKEN' pelo token do seu bot do Telegram
bot = telebot.TeleBot('6583137021:AAEOopzWOThN6VQ081Ir4CZD65NSdVXUoJo')

# Variável de estado para controlar o fluxo da conversa
state = {}

# Comando /start para iniciar o fluxo
@bot.message_handler(commands=['start'])
def start(message):
    state[message.chat.id] = 1  # Inicia no primeiro estado
    bot.send_message(message.chat.id, "Olá! Este é um bot de exemplo. Digite qualquer mensagem para continuar.")

# Função para lidar com mensagens de texto
@bot.message_handler(func=lambda message: state.get(message.chat.id) == 1)
def handle_message1(message):
    state[message.chat.id] = 2  # Avança para o próximo estado
    bot.send_message(message.chat.id, f"Você disse: {message.text}. Digite a próxima mensagem.")

@bot.message_handler(func=lambda message: state.get(message.chat.id) == 2)
def handle_message2(message):
    state[message.chat.id] = 3
    bot.send_message(message.chat.id, f"Você disse: {message.text}. Digite a próxima mensagem.")

@bot.message_handler(func=lambda message: state.get(message.chat.id) == 3)
def handle_message3(message):
    state[message.chat.id] = 4
    bot.send_message(message.chat.id, f"Você disse: {message.text}. Digite a próxima mensagem.")

@bot.message_handler(func=lambda message: state.get(message.chat.id) == 4)
def handle_message4(message):
    state[message.chat.id] = 5
    bot.send_message(message.chat.id, f"Você disse: {message.text}. Digite a próxima mensagem.")

@bot.message_handler(func=lambda message: state.get(message.chat.id) == 5)
def handle_message5(message):
    state[message.chat.id] = 6
    bot.send_message(message.chat.id, f"Você disse: {message.text}. Digite a última mensagem.")

@bot.message_handler(func=lambda message: state.get(message.chat.id) == 6)
def handle_message6(message):
    state[message.chat.id] = 0  # Reinicia o estado
    bot.send_message(message.chat.id, "Você completou o fluxo de 6 mensagens. Digite /start para recomeçar.")

# Iniciar o bot
bot.polling()
