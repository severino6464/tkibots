import telebot

# Substitua 'YOUR_BOT_TOKEN' pelo token de autenticação do seu bot
bot = telebot.TeleBot('6698661685:AAG_PSElNamrv7IiruwnvRSf-Xpcvtpq2SY')

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker_file_id = message.sticker.file_id

    # Formate a mensagem como uma resposta à mensagem de sticker original
    response_message = f'O ID do sticker é: <a href="https://t.me/addstickers/{sticker_file_id}">{sticker_file_id}</a>'
    
    # Envie a mensagem formatada como resposta à mensagem de sticker
    bot.send_message(message.chat.id, response_message, parse_mode='HTML', reply_to_message_id=message.message_id)

# Inicie o bot
bot.polling()



