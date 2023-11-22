import requests
import time
import datetime
import random

possibilidades_minas = [
    "1.50x",
    "2.50x",
    "1.40x",
    "2.10x",
    "2.34x",
    "1.70x",
    "2.00x"
]

texto4 = """
⚠️ Fique atento ao jogo ⚠️

👨🏽‍🚀 Spaceman
🔎 identificando entrada

📲 Link de cadastro: https://go.boasortebet.com/visit/?bta=35563&brand=boasortebet
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GREEN! ✅✅
"""

mensagem = """
✅ Entrada Confirmada 

Entrar apos:

- {}
- {}
- {}

✅ Sair em {}
⚠️ MÁXIMO 3 GALE 

📲 Link de cadastro: https://go.boasortebet.com/visit/?bta=35563&brand=boasortebet
"""

def enviar_mensagens():
    url = 'https://api.z-api.io/instances/3C6139F323A8F08189B42A5707B8D550/token/A705A869C06CC34BF55690C8/send-text'
    headers = {
        'Client-Token': 'F9dfef0feecb44fbe8ad1accdb380e4f7S',
        'Content-Type': 'application/json'
    }

    # Enviar a mensagem de texto4
    data = {
        "phone": "120363201527701660-group",  # Substitua com o número de telefone real
        "message": texto4
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 1 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 1. Código de status: {response.status_code}")

    time.sleep(60)  # Aguardar 1 minuto

    entrada1 = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade1 = entrada1.strftime("%H:%M")
    entrada2 = datetime.datetime.now() + datetime.timedelta(minutes=3)
    hora_validade2 = entrada2.strftime("%H:%M")
    entrada3 = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade3 = entrada3.strftime("%H:%M")

    validade = datetime.datetime.now() + datetime.timedelta(minutes=3)
    hora_validade = validade.strftime("%H:%M")

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)

    # Enviar a mensagem formatada
    mensagem_formatada = mensagem.format(hora_validade1, hora_validade2, hora_validade3, possibilidade_mina_aleatoria)

    data = {
        "phone": "120363201527701660-group",  # Substitua com o número de telefone real
        "message": mensagem_formatada
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 2 formatada enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 2 formatada. Código de status: {response.status_code}")

    time.sleep(400)  # Espera 6 minutos (360 segundos)

    # Enviar a mensagem de texto5
    data = {
        "phone": "120363201527701660-group",  # Substitua com o número de telefone real
        "message": texto5
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 3 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 3. Código de status: {response.status_code}")

    time.sleep(200)  # Espera 3 minutos (180 segundos)

enviar_mensagens()
print("Todas as mensagens foram enviadas. Reiniciando o ciclo.\n")
