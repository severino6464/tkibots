<p>import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOXx

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001811028389'


texto4 = """
ðŸŽ² Fique atento ao jogo ðŸŽ²

ðŸ¯ Fortune Tiger - Entrada em 2 minutos
ðŸ”Ž Estamos validando uma entrada

[ðŸ“± Cadastre-se aqui](https://affiliates.nuts.bet/visit/?bta=35071&amp;brand=nutsbet)
"""

texto5 = """
ðŸ”·ðŸ”¹ Entrada Finalizada ðŸ”¹ðŸ”·
     âœ…âœ… GRENN! âœ…âœ…
 
"""


mensagem = """
âš&nbsp;ï¸ ENTRADA CONFIRMADA âš&nbsp;ï¸

ðŸ¯ ð—™ð—¼ð—¿ð˜ð˜‚ð—»ð—² ð—§ð—¶ð—´ð—²ð—¿ â˜˜
ðŸŽ¯ EstratÃ©gia: ð—›ð—¼ð—¿ð—®Ìð—¿ð—¶ð—¼ð˜€ ð—£ð—®ð—´ð—®ð—»ð˜ð—²ð˜€
ðŸ”¥ ð—¡Âº ð—±ð—² ð—ð—¼ð—´ð—®ð—±ð—®ð˜€: {}
â° Sinal vÃ¡lido atÃ©: {}

ðŸŒª FaÃ§a no mÃ¡ximo {} jogadas!

[ðŸ“± Cadastre-se aqui](https://affiliates.nuts.bet/visit/?bta=35071&amp;brand=nutsbet)

[ðŸ“± Jogar Fortune TigerðŸ¯â˜˜](https://affiliates.nuts.bet/visit/?bta=35071&amp;brand=nutsbet)
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