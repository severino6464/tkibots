import requests
import time
import datetime
import random

possibilidades_minas = [
    "‼️ RETIRAR EM 1.50x",
    "‼️ RETIRAR EM 2.00x",
    "‼️ RETIRAR EM 2.00x",
    "‼️ RETIRAR EM 3.50x",
    "‼️ RETIRAR EM 1.04x",
    "‼️ RETIRAR EM 2.30x",
    "‼️ RETIRAR EM 5.00x"
]

texto4 = """
⚠️ Fique atento ao jogo ⚠️

✈️ Aviator 
🔎 identificando entrada

Cadastre-se aqui!
https://go.boasortebet.com/visit/?bta=35563&brand=boasortebet
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GREEN! ✅✅
"""

mensagem = """
✅ Entrada Confirmada 

{}

⚠️ MÁXIMO 2 GALES 
🔔 Entrada Confirmada 🔔  
✅ Entrar Agora  

⏱️ Válido até: {}

Cadastre-se aqui!
https://go.boasortebet.com/visit/?bta=35563&brand=boasortebet
"""

def enviar_mensagens():
    url = 'https://api.z-api.io/instances/3C6139F323A8F08189B42A5707B8D550/token/A705A869C06CC34BF55690C8/send-text'
    headers = {
        'Client-Token': 'F9dfef0feecb44fbe8ad1accdb380e4f7S',
        'Content-Type': 'application/json'
    }

    # Enviar a mensagem de texto4
    data = {
        "phone": "120363183582582799-group",  # Substitua com o número de telefone real
        "message": texto4
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 1 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 1. Código de status: {response.status_code}")

    time.sleep(120)  # Aguardar 2 minutos

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)

    data = {
        "phone": "120363183582582799-group",  # Substitua com o número de telefone real
        "message": mensagem_formatada
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 2 formatada enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 2 formatada. Código de status: {response.status_code}")

    time.sleep(60)  # Aguardar 1 minuto

    # Enviar a mensagem de texto5
    data = {
        "phone": "120363183582582799-group",  # Substitua com o número de telefone real
        "message": texto5
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 3 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 3. Código de status: {response.status_code}")

    time.sleep(120)  # Aguardar 2 minutos

enviar_mensagens()
print("Todas as mensagens foram enviadas. Reiniciando o ciclo.\n")
