import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001916532826'

sticker_file_id = 'CAACAgEAAxkBAANSZWw5rb6ubRY9EjZXj1pAbRDYcBYAAskCAAK0WehF68sLQC3exTYzBA'

def gerar_possibilidades_minas(opcoes_anteriores):
    possibilidades_minas = []
    for _ in range(3):
        # Inicializa a matriz com "🧤" para representar células vazias
        matriz_mina = [["🧤"] * 3 for _ in range(2)]  # Changed to 2x3 matrix

        # Cria uma lista com as posições disponíveis para a bola (⚽️)
        posicoes_disponiveis = [(i, j) for i in range(2) for j in range(3) if (i, j) not in opcoes_anteriores]

        # Escolhe aleatoriamente uma posição para a bola
        posicao_bola = random.choice(posicoes_disponiveis)
        linha_bola, coluna_bola = posicao_bola

        # Adiciona a posição atual à lista de opções anteriores
        opcoes_anteriores.append((linha_bola, coluna_bola))

        # Define a posição da bola na matriz
        matriz_mina[linha_bola][coluna_bola] = "⚽️"
        
        # Define a posição do goleiro (🧍🏻) na linha de baixo
        linha_goleiro = 1
        coluna_goleiro = 1  # Fixo no meio

        # Define a posição do goleiro na matriz
        matriz_mina[linha_goleiro][coluna_goleiro] = "🧍🏻"

        # Formata a matriz como texto
        possibilidade_mina = "\n".join("".join(linha) for linha in matriz_mina)
        possibilidades_minas.append(possibilidade_mina)

    return possibilidades_minas

selecoes = [
    "🇦🇷 Argentina", "🇦🇹 Áustria", "🇧🇪 Bélgica", "🇧🇷 Brasil",
    "🇭🇷 Croácia", "Tcheco", "🇩🇰 Dinamarca", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra",
    "🇫🇮 Finlândia", "🇫🇷 França", "🇩🇪 Alemanha", "🇮🇪 Irlanda",
    "🇮🇹 Itália", "🇳🇱 Holanda", "🇵🇱 Polônia", "🇵🇹 Portugal",
    "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escócia", "🇷🇸 Sérvia", "🇪🇸 Espanha", "🇸🇪 Suécia",
    "🇨🇭 Suíça", "🇦🇹🇷 Turquia", "🇺🇦 Ucrânia", "🇺🇾 Uruguai"
]

texto4 = """
⚠️ <b>Fique atento ao jogo</b> ⚠️

⚽️ Penalty Shoot-Out 
🔎 identificando entrada

<a href="https://go.aff.br4-partners.com/bwo8x4n1?utm_source=P">📲 <b>Link de cadastro</b></a>
"""

mensagem = """
✅💰<b>Estratégia Exclusiva - 12x a 32x</b>💰✅
🔗 Link de acesso: <a href="https://go.aff.br4-partners.com/bwo8x4n1?utm_source=P"><b>Penalty Shoot-Out-Street</b></a>
🏁 Seleção: {}
👇🏻 <b>Chute o mais próximo do ângulo/trave possível!</b> 👇🏻

{}

🎉 Para 20x = Repita o 1º chute

🤩 Para 32x = Repita o 1º e 2º chute

⏰ Válido até: {} ⏳

Quem lucrou acima de R$ 30 reage aqui embaixo👇
"""

texto5 = """
✅✅✅ GREEN!!! ✅✅✅

Não perca a próxima entrada 12x a 32x do nosso robô!🤖✅

Clique na mensagem fixada logo abaixo do nome do nosso grupo ou aqui embaixo e crie sua conta no cassino seguindo os passos que indicamos!👇

<a href="https://go.aff.br4-partners.com/bwo8x4n1?utm_source=P"><b>CLIQUE AQUI E COMECE LUCRAR AGORA MESMO🤑</b></a>

Você pode transformar R$30 em R$320 em poucos minutos!💰🚀

"""

print("=======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120)

opcoes_anteriores = []  # Lista para armazenar as posições já utilizadas
possibilidades_minas = gerar_possibilidades_minas(opcoes_anteriores)
mensagem_formatada = "\n\n".join(possibilidades_minas)

n_jogadas = random.randint(1, 3)
validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
hora_validade = validade.strftime("%H:%M")
selecao_aleatoria = random.choice(selecoes)
mensagem_formatada = mensagem.format(selecao_aleatoria, mensagem_formatada, hora_validade)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(55)
bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(5)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(420)
