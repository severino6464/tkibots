import telebot
import time
import datetime
import random
import threading
from telebot import types

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" #FOXBOT

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001949467505'

texto4 = """
🚨 Atenção! O Tigre vai falhar 
    🤑Prepare-se para lucrar em breve!!
    
    🐯💰🐯💰🐯💰🐯💰🐯💰🐯💰🐯
"""


texto5 = """""
✅✅✅VITÓRIA ✅✅✅

🐯🍀🐯🍀🐯🍀🐯🍀🐯🍀🐯🍀🐯

Você que fez GREEN envie um print em nosso suporte 👉👉 [FALE CONOSCO](https://l1nk.dev/vipgratis)

🎁 GANHE ATÉ R$5000,00 [AQUI](https://18kbet.online/player-from-agent/agent/167j6)


"""

mensagem = """
💰FALHA CONFIRMADA💰
    🍀Fortune Tiger🐯
    ⏱️Válido até:  {}

    👉{}x Normal 
    ⚡{}x Turbo
    🚥Intercalando 

🐯 Link do jogo: [Clique aqui](https://www.18kbet.online/casino/lobby/casino/category/MAIS%20JOGADOS%20CASSINO%20/game/14142?demo=false)
📲 Única plataforma que funciona o sinal: [Tiger Fortune](https://18kbet.online/player-from-agent/agent/167j6)

🚀 [jogue pelo app](https://xngbet.appnuts.cloud/ap/casa/)

"""


      
   
n_jogadas = random.randint(8, 20)
n_jogadas2 = random.randint(8, 20)
validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(hora_validade,n_jogadas, n_jogadas2)

bot.send_message(chat_id=group_id, text=texto4 ,parse_mode='Markdown')
print("BOT-TIGER-NATHAN")
time.sleep(120)
    
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
time.sleep(120)  # Espera 5 minutos (300 segundos)

         

time.sleep(360)

  




bot.polling()