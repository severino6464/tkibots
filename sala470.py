import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001960486501'


def gerar_tres_opcoes_aleatorias(possibilidades):
    tres_opcoes = random.sample(possibilidades, 3)
    return ", ".join(tres_opcoes)

links = [
    "https://exemplo1.com",
]


possibilidades_minas = [
"CACHORRO 🐕", "JACARÉ 🐊", "PAVÃO 🦚",
"COELHO 🐇", "VACA 🐄", "PERU 🦃",
"CERVO 🦌", "GATO 🐈", "COBRA 🐍",
"BORBOLETA 🦋", "BOI 🐂", "CAMELO 🐪",
"GALO 🐓", "PORCO 🐷", "URSO 🧸",
"TIGRE 🐅", "GORILA 🦍", "ELEFANTE 🐘",
"OVELHA 🐑", "ÁGUIA 🦅", "BUFFALO 🐃",
"LEÃO 🦁", "CAVALO 🐎", "BODE 🐏",
"AVESTRUZ 🦤", "CACHORRO 🐕", "COELHO 🐇",
"JACARÉ 🐊", "PAVÃO 🦚", "VACA 🐄",
"PERU 🦃", "CERVO 🦌", "GATO 🐈",
"COBRA 🐍", "BORBOLETA 🦋", "BOI 🐂",
"CAMELO 🐪", "GALO 🐓", "PORCO 🐷",
"URSO 🧸", "TIGRE 🐅", "GORILA 🦍",
"ELEFANTE 🐘", "OVELHA 🐑", "ÁGUIA 🦅",
"BUFFALO 🐃", "LEÃO 🦁", "CAVALO 🐎",
"BODE 🐏", "AVESTRUZ 🦤", "CACHORRO 🐕",
"COELHO 🐇", "JACARÉ 🐊", "PAVÃO 🦚",
"VACA 🐄", "PERU 🦃", "CERVO 🦌",
"GATO 🐈", "COBRA 🐍", "BORBOLETA 🦋",
"BOI 🐂", "CAMELO 🐪", "GALO 🐓",
"PORCO 🐷", "URSO 🧸", "TIGRE 🐅",
"GORILA 🦍", "ELEFANTE 🐘", "OVELHA 🐑",
"ÁGUIA 🦅", "BUFFALO 🐃", "LEÃO 🦁",
"CAVALO 🐎", "BODE 🐏", "AVESTRUZ 🦤"
]



texto4 = """
🐝 Fique atento ao jogo 🦋

🐞 Jogo do Bicho
🔎 Estamos validando uma entrada

[📱 Cadastre-se aqui](https://18kbet.online/player-from-agent/agent/167j6)

🚨O sinal só funciona apenas na plataforma acima!
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 Você que fez GREEN envie um print no @suportereidossinais1
"""

mensagem = """
🔥 SINAL CONFIRMADO 🔥
🎯 Jogar: TRINCA

{}

🔁 Fazer até 2 gales
🔗 [Cadastre-se antes de Jogar!](https://18kbet.online/player-from-agent/agent/167j6)
🖥️[Jogue Aqui](https://www.18kbet.online/casino/lobby/casino/category/JOGO%20DO%20BICHO/game/1278?demo=false)
⏱️ Válido até: {}
"""




print("======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='Markdown')
time.sleep(120)
possibilidade_mina_aleatoria = gerar_tres_opcoes_aleatorias(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
time.sleep(300)
bot.send_message(chat_id=group_id, text=texto5, parse_mode='Markdown')
time.sleep(180)