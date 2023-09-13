import telebot
import datetime
import random
import time


CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

channel_id = '-1001932869361'  


texto3 = """
✅✅✅ MAIS UM GRANDE GANHO PRA CONTA!!! 
Confia na call hahaha, Me manda um depoimento aqui!
👉 [Clique aqui](https://abrir.link/PD90e)
"""

texto4 = """
✅✅✅ MAIS UM GRANDE GANHO PRA CONTA!!! 
Confia na call hahaha, Me manda um depoimento aqui!
👉 [Clique aqui](https://abrir.link/PD90e)
"""

texto5 = """
❌❌❌ Red, Faz parte, bora para próxima
Não conseguiu subir sua banca ainda? Me chama aqui! 
👉 [Clique aqui](https://abrir.link/ujDxN)
"""

def send_signal():
    # Escolher aleatoriamente entre texto4 e texto5
    random_text = random.choice([texto3, texto4, texto5])
    # Enviar a mensagem para o canal especificado
    bot.send_message(chat_id=channel_id, text=random_text, parse_mode='Markdown')

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "09:35", "10:50", "11:35", "13:05", "15:35", "17:35", "18:50", "20:35", "21:20"
    ]

    if current_time in signal_times:
        send_signal()

try:
    # Executar a verificação e envio de sinal
    check_and_send_signal()
    # Esperar por 1 minuto antes de verificar novamente
    time.sleep(60)
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")