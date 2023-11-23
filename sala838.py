import requests
import time
import datetime
import random

sticker_file_id = 'CAACAgIAAxkBAAMfZSb4VppXyng9TmBwSA12Ss3y2hkAAhoDAAKc1ucKpX8qfdF9KAIwBA'

texto4 = """
🎲 Fique atento ao jogo 🎲

🐂 Fortune OX
🔎 Estamos validando uma entrada

Cadastre-se aqui!
https://go.boasortebet.com/visit/?bta=35882brand=boasortebet

🚨O sinal do robô só funciona apenas na plataforma acima! Faça💰🤑
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GREEN! ✅✅
"""

mensagem = """
⚠️ ENTRADA CONFIRMADA ⚠️

🐂 Fortune OX

🔥 𝗡º 𝗱𝗲 𝗝𝗼𝗴𝗮𝗱𝗮𝘀: {}
🔹 {}X modo Normal
🔹 {}X modo Turbo
⏰ Sinal válido até: {}

🌪 Faça no máximo {} jogadas!

Cadastre-se aqui!
https://go.boasortebet.com/visit/?bta=35882brand=boasortebet

🚨O sinal do Robô só funciona apenas na plataforma acima! Faça💰🤑
"""

def enviar_mensagens():
    url = 'https://api.z-api.io/instances/3C6139F323A8F08189B42A5707B8D550/token/A705A869C06CC34BF55690C8/send-text'
    headers = {
        'Client-Token': 'F9dfef0feecb44fbe8ad1accdb380e4f7S',
        'Content-Type': 'application/json'
    }

    # Enviar a mensagem de texto4
    data = {
        "phone": "120363181576569838-group",  # Substitua com o número de telefone real
        "message": texto4
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 1 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 1. Código de status: {response.status_code}")

    time.sleep(60)  # Aguardar 1 minuto

    n_jogadas = random.randint(1, 12)
    n_jogadas2 = random.randint(1, 6)
    n_jogadas3 = random.randint(1, 6)
    n_jogadas4 = random.randint(1, 6)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")

    # Enviar a mensagem formatada
    mensagem_formatada = mensagem.format(n_jogadas, n_jogadas2, n_jogadas3, hora_validade, n_jogadas4)

    data = {
        "phone": "120363181576569838-group",  # Substitua com o número de telefone real
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
        "phone": "120363181576569838-group",  # Substitua com o número de telefone real
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
