import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001987578081'

possibilidades_minas = [
    "💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",
    "💣💣⭐️💣⭐️\n💣⭐️⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",
    "💣💣💣⭐️⭐️\n💣💣💣⭐️💣\n💣⭐️⭐️⭐️💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣💣💣⭐️\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣⭐️⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣💣💣⭐️\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "💣⭐️💣💣💣\n⭐️💣⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣",
    "💣⭐️💣⭐️💣\n💣💣💣⭐️💣\n💣💣⭐️⭐️💣\n💣💣⭐️⭐️💣\n💣💣⭐️💣💣",
    "⭐️⭐️⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "💣💣💣💣💣\n💣💣💣💣⭐️\n⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️⭐️💣💣💣\n💣⭐️💣💣💣\n💣⭐️⭐️⭐️💣\n💣💣💣💣💣\n💣💣💣💣💣",
    "⭐️⭐️💣⭐️💣\n💣💣💣⭐️⭐️\n💣💣💣💣💣\n💣💣💣💣💣\n💣⭐️⭐️⭐️💣",
    "💣💣💣💣⭐️\n⭐️💣💣⭐️💣\n⭐️⭐️⭐️💣💣\n💣⭐️💣💣💣\n💣⭐️💣💣💣",
    "⭐️💣💣⭐️💣\n💣💣💣💣💣\n💣⭐️💣⭐️💣\n💣⭐️💣💣💣\n💣⭐️💣⭐️💣",
    "⭐️⭐️⭐️💣💣\n⭐️💣⭐️💣💣\n💣💣💣💣💣\n💣💣💣💣💣\n💣💣💣⭐️💣",
    "⭐️💣💣💣💣\n⭐️💣💣⭐️💣\n💣💣💣💣💣\n💣💣⭐️⭐️💣\n💣💣⭐️⭐️⭐️",
    "💣💣💣💣⭐️\n⭐️💣💣⭐️💣\n⭐️💣⭐️⭐️💣\n💣💣💣💣💣\n💣💣⭐️⭐️💣",
    "💣💣💣⭐️💣\n⭐️💣💣⭐️⭐️\n⭐️💣💣💣💣\n💣💣💣💣💣\n💣💣💣⭐️💣",
    "⭐️💣💣💣💣\n💣💣💣💣💣\n⭐️💣💣💣💣\n💣⭐️💣⭐️💣\n💣⭐️💣⭐️💣"
]

links = [
    "https://exemplo1.com",
   
]


text1 = """
Faça seu cadastro [Clicando aqui](https://affiliates.nuts.bet/visit/?bta=36261&brand=nutsbet) 
✍🏻 Os sinais só funcionam na nuts bet
  """

mensagem = """
🎲 Entrada confirmada 🎲
🥇: Entrada 

{}
🎮: Tentativas: 2
Jogar com 2 a 3 minas

📲: Plataforma correta: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=36261&brand=nutsbet)
👉🏻: Link do jogo: [Mines](https://affiliates.nuts.bet/visit/?bta=36261&brand=nutsbet)
⏱️ Válido até: {}

"""


text2 = """
🔷🔹 Entrada Finalizada 🔹🔷 

✅✅✅ GRENN! ✅✅✅

💰 Lucrou? Mande print para um dos admins 
 
🔥 Só quem joga na NUTS BET deu green

💰⭐💰⭐💰⭐💰⭐💰⭐💰⭐
  """

print("aff208")

possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

time.sleep(5)

bot.send_message(chat_id=group_id, text=text1 ,parse_mode='Markdown')
    
time.sleep(120)
bot.send_message(chat_id=group_id, text=text2 ,parse_mode='Markdown')

