import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002113060115'

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

selecoes = [
    "Argentina", "Áustria", "Bélgica", "Brasil",
    "Croácia", "Tcheco", "Dinamarca", "Inglaterra",
    "Finlândia", "França", "Alemanha", "Irlanda",
    "Itália", "Holanda", "Polônia", "Portugal",
    "Escócia", "Sérvia", "Espanha", "Suécia",
    "Suíça", "Turquia", "Ucrânia", "Uruguai"
]

texto4 = """
⚠️ <b>Fique atento ao jogo</b> ⚠️

⚽️ Penalty Shoot-Out 
🔎 identificando entrada

<a href="http://bit.ly/CLIQUE_AQUI_PARA_FORAR">📲 <b>Link de cadastro</b></a>
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
🔗 Link de acesso: <a href="http://bit.ly/CLIQUE_AQUI_PARA_FORAR"><b>Penalty Shoot-Out-Street</b></a>
👇🏻 <b>Provável sequência</b> 👇🏻

{}
  
"""

print("=======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120)

possibilidades_minas = gerar_possibilidades_minas()
mensagem_formatada = "\n\n".join(possibilidades_minas)

n_jogadas = random.randint(1, 3)
validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
hora_validade = validade.strftime("%H:%M")
selecao_aleatoria = random.choice(selecoes)
mensagem_formatada = mensagem.format(selecao_aleatoria, hora_validade, n_jogadas, mensagem_formatada)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(10)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(50)
