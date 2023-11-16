import random
import requests
import telebot
import datetime
import time

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # Substitua pelo seu token de bot
bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1002052729835'  # Substitua pelo ID do seu canal

possibilidades_minas = [
    "Apostar na 1° e 2° dúzia",
    "Apostar na 1° e 3° dúzia",
    "Apostar na 2° e 3° dúzia"
]

url = "https://casino.betfair.com/api/tables-details"
headers = {"cookie": "vid=YOUR_COOKIE"}

def puxar_ultimo_numero():
    resposta = requests.get(url, headers=headers)
    dic_resposta = resposta.json()
    dados = dic_resposta['gameTables']
    for i in dados:
        roletas = i['gameTableId']
        if '103910' in roletas:
            chaves = i.keys()
            if 'lastNumbers' in chaves:
                ultimos_resultados = i['lastNumbers']
                if ultimos_resultados:
                    return ultimos_resultados[0]
    return None

texto4 = """
⚠️ <b>ATENÇÃO VAMOS INICIAR</b> ⚠️

<a href="https://affiliates.nuts.bet/visit/?bta=38535&brand=nutsbet"><b>💸 Clique aqui para abrir a corretora!</b></a>
"""

mensagem = """
🎯 <b>Entrada Confirmada</b> 🎯

🖥️ Roleta: ROLETA BRASILEIRA 🇧🇷
🔁 Até duas proteções - Cobrir o zero!

🔥 Entrar: {}

🧨 Último número: {}

<a href="https://affiliates.nuts.bet/visit/?bta=38535&brand=nutsbet"><b>💸 Clique aqui para abrir a corretora!</b></a>
"""

# Lista para armazenar os sinais enviados
sinais_enviados = []

def enviar_sinal():
    ultimos_resultados = puxar_ultimo_numero()
    if ultimos_resultados:
        ultimo_numero = ultimos_resultados
        possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
        hora = datetime.datetime.now().strftime("%H:%M")
        resultado = 'GREEN ✅' if random.random() < 0.8 else 'RED ❌'  # Exemplo aleatório

        # Esperar 5 segundos antes de enviar a mensagem
        time.sleep(5)

        mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, ultimo_numero, hora)
        bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
        sinais_enviados.append({'hora': hora, 'resultado': resultado})

def gerar_relatorio():
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
    relatorio = f"📔 RELATÓRIO DE OPERAÇÕES ({data_atual})\n\n"

    contagem_verde = 0
    contagem_vermelho = 0

    for resultado in sinais_enviados:
        relatorio += f"{resultado['hora']} - {resultado['resultado']}\n"

        if resultado['resultado'] == 'GREEN ✅':
            contagem_verde += 1
        elif resultado['resultado'] == 'RED ❌':
            contagem_vermelho += 1

    placar = f"\nPlacar: ✅ {contagem_verde} x ❌ {contagem_vermelho}\n"
    relatorio += placar

    return relatorio


def enviar_relatorio():
    relatorio = gerar_relatorio()
    bot.send_message(chat_id=channel_id, text=relatorio, parse_mode='HTML', disable_web_page_preview=True)

def enviar_sinais_e_relatorio():
    # Enviar o texto4 antes dos sinais
    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)

    # Aguardar 5 minutos antes de iniciar os sinais
    time.sleep(5 * 60)

    for _ in range(5):
        enviar_sinal()
        time.sleep(10 * 60)

    enviar_relatorio()

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = ["09:00", "14:00", "18:00"]

    if current_time in signal_times:
        enviar_sinais_e_relatorio()

# Chame a função check_and_send_signal a partir do seu código principal sempre que necessário
check_and_send_signal()
