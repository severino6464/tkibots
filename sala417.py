import telebot
import datetime
import random
import time

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001936374703'  

possibilidades_minas = [
    "Apostar em números baixos [1-18]",
    "Apostar em números altos [19-36]",
    "Apostar na duzia 1 e 3",
    "Apostar na cor 🔴",
    "Apostar na cor ⚫"
]

texto4 = """
⚠️ <b>ATENÇÃO VAMOS INICIAR</b> ⚠️

<a href="https://affiliates.nuts.bet/visit/?bta=37469&brand=nutsbet"><b>🔗 Cadastre-se antes de Jogar!</b></a>

<a href="https://affiliates.nuts.bet/visit/?bta=37469&nci=5359"><b>🏦 Abrir jogo</b></a>
"""

texto5 = """
✅✅ <b>SESSÃO ENCERRADA!</b> ✅✅
"""

mensagem = """
💰 SINAL CONFIRMOU 💰
🎰 Roleta: Brasileira

{}

⏱️ Válido até: {}
⚠️ Sempre cobrir o zero
🔁 Fazer até 2 proteções

<a href="https://affiliates.nuts.bet/visit/?bta=37469&brand=nutsbet"><b>🔗 Cadastre-se antes de Jogar!</b></a>

<a href="https://affiliates.nuts.bet/visit/?bta=37469&nci=5359"><b>🏦Abra a roleta</b></a>
"""

def send_signal():
    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(180)

    # Repita este bloco para cada sinal
    # ...

    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    horarios_sinal = ["09:30", "14:30", "20:30", "21:34"]
    
    horario_mais_proximo = min(horarios_sinal, key=lambda x: (datetime.datetime.strptime(x, "%H:%M") - datetime.datetime.strptime(current_time, "%H:%M")).total_seconds())
    
    if horario_mais_proximo == current_time:
        send_signal()

try:
    check_and_send_signal()
    # Aguarde 1 minuto antes de verificar o horário novamente
    time.sleep(60)
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
