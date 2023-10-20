import telebot
import datetime
import random
import time
import requests

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # Substitua pelo seu token de bot
bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001953877651'  # Substitua pelo ID do seu canal

possibilidades_minas = [
    "Apostar na 1° e 2° coluna",
    "Apostar na 1° e 3° coluna",
    "Apostar na 2° e 3° coluna",
]

url = "https://casino.betfair.com/api/tables-details"
headers = {"cookie": "vid=8ab7daa7-57f7-4196-8285-943390594163"}

def puxar_dados():
    resposta = requests.get(url, headers=headers)
    dic_resposta = resposta.json()
    dados = dic_resposta['gameTables']
    for i in dados:
        roletas = i['gameTableId']
        if '103910' in roletas:
            chaves = i.keys()
            if 'lastNumbers' in chaves:
                ultimos_resultados = i['lastNumbers']
                return ultimos_resultados

texto4 = """
⚠️ <b>ATENÇÃO VAMOS INICIAR</b> ⚠️

<a href="https://affiliates.nuts.bet/visit/?bta=35722&brand=nutsbet"><b>💸 Clique aqui para abrir a corretora!</b></a>
"""

mensagem = """
🎯 <b>Entrada Confirmada</b> 🎯

🖥️ Roleta: ROLETA BRASILEIRA 🇧🇷
🔁 Até duas proteções - Cobrir o zero!

🔥 Entrar: {}

🧨 Último número: {}
⏱️ Válido até: {}

<a href="https://affiliates.nuts.bet/visit/?bta=35722&brand=nutsbet"><b>💸 Clique aqui para abrir a corretora!</b></a>
"""

# Lista para armazenar os sinais enviados
sinais_enviados = []

def enviar_sinal(resultado, contagem_verde, contagem_vermelho):
    ultimos_resultados = puxar_dados()
    if ultimos_resultados:
        ultimo_numero = ultimos_resultados[0]
        possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
        mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, ultimo_numero, resultado['hora'])
        bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
        sinais_enviados.append(resultado)
        if resultado['resultado'] == 'GREEN ✅':
            contagem_verde += 1
        elif resultado['resultado'] == 'RED ❌':
            contagem_vermelho += 1
        return contagem_verde, contagem_vermelho

def gerar_relatorio(contagem_verde, contagem_vermelho):
    data_atual = datetime.datetime now().strftime("%d/%m/%Y")
    relatorio = f"📔 RELATÓRIO DE OPERAÇÕES ({data_atual})\n\n"

    for resultado in sinais_enviados:
        relatorio += f"{resultado['hora']} - {resultado['resultado']}\n"

    placar = f"\nPlacar: ✅ {contagem_verde} x ❌ {contagem_vermelho}\n"
    relatorio += placar

    return relatorio

def enviar_relatorio(contagem_verde, contagem_vermelho):
    relatorio = gerar_relatorio(contagem_verde, contagem_vermelho)
    bot.send_message(chat_id=channel_id, text=relatorio, parse_mode='HTML', disable_web_page_preview=True)

def enviar_sinais_e_relatorio():
    contagem_verde = 0
    contagem_vermelho = 0

    # Enviar o texto4 antes dos sinais
    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)

    # Aguardar 5 minutos antes de iniciar os sinais
    time.sleep(5 * 60)

    for _ in range(6):
        resultado = {'hora': datetime.datetime.now().strftime("%H:%M"), 'resultado': 'GREEN ✅' if contagem_verde < 5 else 'RED ❌'}
        
        contagem_verde, contagem_vermelho = enviar_sinal(resultado, contagem_verde, contagem_vermelho)
        
        time.sleep(10 * 60)

    enviar_relatorio(contagem_verde, contagem_vermelho)

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = ["09:00", "14:00", "16:22"]

    if current_time in signal_times:
        enviar_sinais_e_relatorio()

while True:
    try:
        check_and_send_signal()
        time.sleep(60)
    except Exception as e:
        print(f"Erro ocorreu: {str(e)}")
