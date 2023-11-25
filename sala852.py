import requests
import time
import datetime
import random

sticker_file_id = 'CAACAgIAAxkBAAMmZSb_ngXS-jrJPaIDkQxNkCtYOQQAAtgLAAJYD5hKNPj69b5xWK8wBA'

texto4 = """
🎲 Fique atento ao jogo 🎲

🐭 Fortune mouse
🔎 Estamos validando uma entrada

Cadastre-se aqui


"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GREEN! ✅✅
"""

mensagem = """
⚠️ ENTRADA CONFIRMADA ⚠️

🐭 Fortune mouse

🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
⏰ Sinal válido até: {}

🌪 Faça no máximo {} jogadas!

Cadastre-se aqui


"""

def enviar_mensagens():
    url = 'https://api.z-api.io/instances/SEU_ID_DA_INSTANCIA/token/SEU_TOKEN_DA_INSTANCIA/send-text'  # Substitua com suas informações reais
    headers = {
        'Client-Token': 'SEU_CLIENT_TOKEN',
        'Content-Type': 'application/json'
    }

    # Enviar a mensagem de texto4
    data = {
        "phone": "120363199384599443-group",  # Substitua com o número de telefone real
        "message": texto4
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 1 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 1. Código de status: {response.status_code}")

    time.sleep(60)  # Aguardar 1 minuto

    n_jogadas = random.randint(2, 15)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")

    # Enviar a mensagem formatada
    mensagem_formatada = mensagem.format(n_jogadas, hora_validade, n_jogadas)

    data = {
        "phone": "120363199384599443-group",  # Substitua com o número de telefone real
        "message": mensagem_formatada
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 2 formatada enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 2 formatada. Código de status: {response.status_code}")

    time.sleep(120)  # Espera 2 minutos (120 segundos)

    # Enviar a mensagem de texto5
    data = {
        "phone": "120363199384599443-group",  # Substitua com o número de telefone real
        "message": texto5
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 3 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 3. Código de status: {response.status_code}")

    time.sleep(120)  # Espera 2 minutos (120 segundos)
    # Enviar o sticker
    data = {
        "phone": "===",  # Substitua com o número de telefone real
        "message": f"[STICKER]{sticker_file_id}"
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Sticker enviado com sucesso!")
    else:
        print(f"Falha ao enviar o sticker. Código de status: {response.status_code}")

enviar_mensagens()
print("Todas as mensagens foram enviadas. Reiniciando o ciclo.\n")
