import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001810963252'  

possibilidades_minas = [
    "Apostar em números baixos [1-18]",
    "Apostar em números altos [19-36]",
    "Apostar na duzia 1 e 3",
    "Apostar na cor 🔴",
    "Apostar na cor ⚫"
]

links = [
    "https://example.com/link1",
    "https://example.com/link2",
    "https://example.com/link3"
]

texto4 = """
ATENÇÃO VAMOS INICIAR 

FAÇA SEU CADASTRO 👇
[Clique aqui](https://affiliates.nuts.bet/visit/?bta=36463&brand=nutsbet)

ENTRE NO JOGO👇🏻
[Clique aqui](https://affiliates.nuts.bet/visit/?bta=36463&brand=nutsbet)
"""


mensagem = """
💰 ENTRADA CONFIRMADA 💰
🎰 Roleta: Brasileira
Link: [Clique aqui](https://affiliates.nuts.bet/visit/?bta=36463&brand=nutsbet)

{}

👉 Cobrir o zero
🔁 Fazer até 3 gales
🔗 [Cadastre-se antes de Jogar!](https://affiliates.nuts.bet/visit/?bta=36463&brand=nutsbet)
⏱️ Válido até: {}
"""

print("======")
bot.send_message(chat_id=channel_id, text=texto4, parse_mode='markdown')
time.sleep(60)
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='markdown')
time.sleep(240)