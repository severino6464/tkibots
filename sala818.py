import requests
import time
import random
import datetime

texto4 = """
⚠️ *ATENÇÃO VAMOS INICIAR!* ⚠️
"""

mensagem = """
🔥 *ROBÔ CONFIRMOU* 🔥
🎰 Roleta: Brasileira

{}

⏱️ Válido até: {}

👉 Cobrir o zero
🔁 Fazer até 3 gales

🔗 Cadastre-se antes de Jogar!
https://go.boasortebet.com/visit/?bta=35352&brand=boasortebet
"""

links = [
    "https://exemplo1.com",
]

possibilidades_minas = [
    "Apostar em números baixos [1-18]",
    "Apostar em números altos [19-36]",
    "Apostar na duzia 1 e 3",
    "Apostar na cor 🔴",
    "Apostar na cor ⚫"
]

def enviar_mensagens():
     url = 'https://api.z-api.io/instances/3C6139F323A8F08189B42A5707B8D550/token/A705A869C06CC34BF55690C8/send-text'
    headers = {
        'Client-Token': 'F9dfef0feecb44fbe8ad1accdb380e4f7S',
        'Content-Type': 'application/json'
    }

    # Enviar a mensagem de texto4
    data = {
        "phone": "120363197773071755-group",  # Substitua com o número de telefone real
        "message": texto4
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 1 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 1. Código de status: {response.status_code}")

    time.sleep(60)  # Aguardar 1 minuto

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    link_aleatorio = random.choice(links)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
    mensagem_formatada = mensagem_formatada.replace("========", link_aleatorio)

    data = {
        "phone": "120363197773071755-group",  # Substitua com o número de telefone real
        "message": mensagem_formatada
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 2 formatada enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 2 formatada. Código de status: {response.status_code}")

    time.sleep(120)  # Aguardar 2 minutos

    # Envie um sticker (se você tiver um método para enviar adesivos)
    # Substitua "SEU_STICKER_ID" pelo ID do seu adesivo no WhatsApp
    data = {
        "phone": "120363197773071755-group",  # Substitua com o número de telefone real
        "message": "CAACAgIAAxkBAAMmZSb_ngXS-jrJPaIDkQxNkCtYOQQAAtgLAAJYD5hKNPj69b5xWK8wBA"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Sticker enviado com sucesso!")
    else:
        print(f"Falha ao enviar o adesivo. Código de status: {response.status_code}")

    time.sleep(420)  # Aguardar 7 minutos


enviar_mensagens()
print("Todas as mensagens foram enviadas. Reiniciando o ciclo.\n")
