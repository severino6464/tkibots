import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002084504086'

sticker_file_id = 'CAACAgEAAxkBAAMCZSbmh4EopfmSJgx8Z8sDxkeWf1UAAvwAAzgOghFAju2fQymOBzAE'

texto1 = """

⚠ <b>NOVA FALHA ENCONTRADA</b> ⚠

🎰 <b>Slots</b>: Tigre,Rato,Touro e Coelho

✅<b>98,89%</b> DE ACERTIVIDADE

🔎 Identificando a falha
"""
mensagem = """
⚠ FALHA ENCONTRADA ⚠

⏰ Estratégia: Horários Pagantes
🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
♻️ Intercale entre Turbo e Normal
🔄 Valor da Rodada Variado


⚠️ Válido ate: {}


<a href="https://affiliates.nuts.bet/visit/?bta=38230&brand=nutsbet">📱 Cadastre-se aqui</a>(SO FUNCIONA NA NUTSBET)

🚨 Faça um depósito Recomendado de R$40,00 ou +, para a falha funcionar!
"""

texto2 = """
✅ <b>OPORTUNIDADE FINALIZADA</b> ✅


⏰ Aguarde a próxima falha... ⏰
"""

print("========")

bot.send_message(chat_id=group_id, text=texto1, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120)
n_jogadas = random.randint(6, 20)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(n_jogadas, hora_validade)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(300)
bot.send_message(chat_id=group_id, text=texto2, parse_mode='HTML', disable_web_page_preview=True)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(180)
