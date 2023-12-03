import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001916532826'

sticker_file_id = 'CAACAgEAAxkBAANSZWw5rb6ubRY9EjZXj1pAbRDYcBYAAskCAAK0WehF68sLQC3exTYzBA'

def gerar_possibilidades_minas():
    possibilidades_minas = []
    for _ in range(3):
        # Inicializa a matriz com "🧤" para representar células vazias
        matriz_mina = [["🧤"] * 3 for _ in range(2)]  # Changed to 2x3 matrix

        # Escolhe aleatoriamente uma linha e uma coluna para a bola (⚽️)
        linha = random.randint(0, 1)  # Adjusted to 0-1 for 2 rows
        coluna = random.randint(0, 2)  # Adjusted to 0-2 for 3 columns

        # Define a posição da bola na matriz
        matriz_mina[linha][coluna] = "⚽️"
        
        # Adiciona o emoji 🧍🏻 à segunda coluna da linha de baixo
        matriz_mina[(linha + 2) % 2][1] = "🧍🏻"

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

Você pode transformar R$10 em R$320 em poucos minutos!💰🚀

"""

texto6 = """
✅5 GREENS AO VIVO TODOS OS DIAS DE GRAÇA

Deposite 30 reais e clique no link abaixo para entrar nas lives e concorrer a prêmios 👇

<a href="https://t.me/+P4rH7M6Iz0QyOWIx"><b>CLIQUE AQUI</b></a>
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
mensagem_formatada = mensagem.format(selecao_aleatoria, mensagem_formatada, hora_validade)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(55)
bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(5)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(60)
bot.send_message(chat_id=group_id, text=texto6, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(360)
