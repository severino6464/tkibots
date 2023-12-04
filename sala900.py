import requests
import time
import random
import datetime

mensagem_1 = """
💎ENCONTRANDO FALHA NA MATRIX...💎
🐯POSSÍVEL ENTRADA EM 2 MINUTOS

📱 CADASTRE-SE AQUI
https://affiliates.nuts.bet/visit/?bta=38654&brand=nutsbet
"""

mensagem_2 = """
🚨 ENTRADA CONFIRMADA 🚨

🐯 Fortune Tiger 
⏰ Estratégia: Horários Pagantes
⚠️ Válido ate: {}

💰 {}x Normal
💰 {}x Turbo

⚡ Intercalando

📱 CADASTRE-SE AQUI
https://affiliates.nuts.bet/visit/?bta=38654&brand=nutsbet
"""

links = [
    "https://affiliates.nuts.bet/visit/?bta=38654&brand=nutsbet",
    
]


text2 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
  """



  
def enviar_mensagens():
    url = 'https://api.z-api.io/instances/3C6139F323A8F08189B42A5707B8D550/token/A705A869C06CC34BF55690C8/send-text'
    headers = {
        'Client-Token': 'F9dfef0feecb44fbe8ad1accdb380e4f7S',
        'Content-Type': 'application/json'
    }

    # Enviar a mensagem_1
    data = {
        "phone": "120363183209544577-group",
        "message": mensagem_1
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 1 enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 1. Código de status: {response.status_code}")

    time.sleep(120)  # Aguardar 2 minutos

    n_jogadas = random.randint(6, 20)
    n_jogadas2 = random.randint(4, 20)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem_2.format(hora_validade,n_jogadas, n_jogadas2)

    data = {
        "phone": "120363183209544577-group",
        "message": mensagem_formatada
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem 2 formatada enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem 2 formatada. Código de status: {response.status_code}")

    time.sleep(600)  # Aguardar 40 segundos após o envio da mensagem formatada


enviar_mensagens()
print("Todas as mensagens foram enviadas. Reiniciando o ciclo.\n")
    
    
