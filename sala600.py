import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001987054108'

sticker_file_id = 'CAACAgIAAxkBAAMsZTC6XdKmOE1SHeCfUBcpU4Y79f0AAloHAAJjK-IJRP8CDh-ifn8wBA'

def gerar_possibilidades_minas():
    possibilidades_minas = []
    for _ in range(3):
        # Inicializa a matriz com "🟢" para representar células vazias
        matriz_mina = [["🟢"] * 5 for _ in range(3)]
        
        # Escolhe aleatoriamente uma linha e uma coluna para a bola (⚽️)
        linha = random.randint(0, 2)
        coluna = random.randint(0, 4)
        
        # Define a posição da bola na matriz
        matriz_mina[linha][coluna] = "⚽️"
        
        # Formata a matriz como texto
        possibilidade_mina = "\n".join("".join(linha) for linha in matriz_mina)
        possibilidades_minas.append(possibilidade_mina)

    return possibilidades_minas

texto4 = """
⚠️ <b>Fique atento ao jogo</b> ⚠️

⚽️ Penalty Shoot-Out-Street 
🔎 identificando entrada

<a href="https://affiliates.nuts.bet/visit/?bta=37072&brand=nutsbet">📲 <b>Link de cadastro</b></a>
"""

texto5 = """
🔷🔹 <b>Entrada Finalizada</b> 🔹🔷
     ✅✅ <b>GRENN!</b> ✅✅
"""

mensagem = """
⚽️💰 <b>Entrada confirmada</b> ⚽️💰
🏁 Seleção: {}
⏰ Válido até: {}
🔁 N° de tentativas: {}

🔗 Link de acesso: <a href="https://affiliates.nuts.bet/visit/?bta=37072&brand=nutsbet"><b>Penalty Shoot-Out-Street</b></a>
  
🔗 Link de acesso ao jogo: <a href="https://affiliates.nuts.bet/visit/?bta=37072&nci=5386"><b>Penalty Shoot-Out-Street</b></a>
  
👇🏻 <b>Provável sequência</b> 👇🏻

{}
  
"""

texto6= """
🚨🚨 HORARIOS DE FUNCIONAMENTO MÉTODO PENALTY🚨🚨


✅ Ai boca atenção que vai começar a sessão do método ✅
✅ sessão todos os dias ✅

⏰ 09:00 - 9:40 

⏰ 13:00 - 13:40

⏰ 19:00- 19:40

⏰ 22:00 - 22:40


MÉTODO AVIATOR:
https://t.me/+FfjehVUGzWY4NTdh

MÉTODO PENALTY: 
https://t.me/+vguYFi-7FFw0MDJh



📌 Vídeo ensinando como funciona fixado no topo do GRUPO✅
"""

selecoes = [
    "Argentina", "Áustria", "Bélgica", "Brasil", "Croácia", "Tcheco", "Dinamarca",
    "Inglaterra", "Finlândia", "França", "Alemanha", "Irlanda", "Itália",
    "Holanda", "Polônia", "Portugal", "Escócia", "Sérvia", "Espanha",
    "Suécia", "Suíça", "Turquia", "Ucrânia", "Uruguai"
]

def send_signal():

    print("=======")
    bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    possibilidades_minas = gerar_possibilidades_minas()
    mensagem_formatada = "\n\n".join(possibilidades_minas)
    selecao_aleatoria = random.choice(selecoes)
    n_jogadas = random.randint(1, 3)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(10)
    bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
    time.sleep(50)

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    possibilidades_minas = gerar_possibilidades_minas()
    mensagem_formatada = "\n\n".join(possibilidades_minas)
    selecao_aleatoria = random.choice(selecoes)
    n_jogadas = random.randint(1, 3)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(10)
    bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
    time.sleep(50)

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    possibilidades_minas = gerar_possibilidades_minas()
    mensagem_formatada = "\n\n".join(possibilidades_minas)
    selecao_aleatoria = random.choice(selecoes)
    n_jogadas = random.randint(1, 3)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(10)
    bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
    time.sleep(50)

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    possibilidades_minas = gerar_possibilidades_minas()
    mensagem_formatada = "\n\n".join(possibilidades_minas)
    selecao_aleatoria = random.choice(selecoes)
    n_jogadas = random.randint(1, 3)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(10)
    bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
    time.sleep(50)

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    possibilidades_minas = gerar_possibilidades_minas()
    mensagem_formatada = "\n\n".join(possibilidades_minas)
    selecao_aleatoria = random.choice(selecoes)
    n_jogadas = random.randint(1, 3)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(10)
    bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
    time.sleep(50)

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    possibilidades_minas = gerar_possibilidades_minas()
    mensagem_formatada = "\n\n".join(possibilidades_minas)
    selecao_aleatoria = random.choice(selecoes)
    n_jogadas = random.randint(1, 3)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(10)
    bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
    time.sleep(50)

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    possibilidades_minas = gerar_possibilidades_minas()
    mensagem_formatada = "\n\n".join(possibilidades_minas)
    selecao_aleatoria = random.choice(selecoes)
    n_jogadas = random.randint(1, 3)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(10)
    bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
    time.sleep(50)

    bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)
    possibilidades_minas = gerar_possibilidades_minas()
    mensagem_formatada = "\n\n".join(possibilidades_minas)
    selecao_aleatoria = random.choice(selecoes)
    n_jogadas = random.randint(1, 3)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120)  # Espera 5 minutos (300 segundos)
    bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(10)
    bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
    time.sleep(50)

    bot.send_message(chat_id=group_id, text=texto6, parse_mode='HTML', disable_web_page_preview=True)


def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "09:00", "13:00", "19:00", "22:00"
    ]

    if current_time in signal_times:
        send_signal()


try:
        check_and_send_signal()
        # Wait for 1 minute before checking the time again
        datetime.datetime.now() + datetime.timedelta(minutes=0)
except Exception as e:
        print(f"Error occurred: {str(e)}")
