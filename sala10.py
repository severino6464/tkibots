<p>import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOXx

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001811028389'


texto4 = """.
๐ฒ Fique atento ao jogo ๐ฒ

๐ฏ Fortune Tiger - Entrada em 2 minutos
๐ Estamos validando uma entrada

[๐ฑ Cadastre-se aqui](https://affiliates.nuts.bet/visit/?bta=35071&amp;brand=nutsbet)
"""

texto5 = """
๐ท๐น Entrada Finalizada ๐น๐ท
     โโ GRENN! โโ
 
"""


mensagem = """
โ&nbsp;๏ธ ENTRADA CONFIRMADA โ&nbsp;๏ธ

๐ฏ ๐๐ผ๐ฟ๐๐๐ป๐ฒ ๐ง๐ถ๐ด๐ฒ๐ฟ โ
๐ฏ Estratรฉgia: ๐๐ผ๐ฟ๐ฎฬ๐ฟ๐ถ๐ผ๐ ๐ฃ๐ฎ๐ด๐ฎ๐ป๐๐ฒ๐
๐ฅ ๐กยบ ๐ฑ๐ฒ ๐๐ผ๐ด๐ฎ๐ฑ๐ฎ๐: {}
โฐ Sinal vรกlido atรฉ: {}

๐ช Faรงa no mรกximo {} jogadas!

[๐ฑ Cadastre-se aqui](https://affiliates.nuts.bet/visit/?bta=35071&amp;brand=nutsbet)

[๐ฑ Jogar Fortune Tiger๐ฏโ](https://affiliates.nuts.bet/visit/?bta=35071&amp;brand=nutsbet)
"""



while True:

    print("BOT-aff11-nuts")

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
    time.sleep(120) 



    n_jogadas = random.randint(2, 10)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas)

    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')

    time.sleep(60)  # Espera 5 minutos (300 segundos)

    bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
    time.sleep(120) </p>