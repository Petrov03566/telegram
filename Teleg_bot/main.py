import telebot

bot =telebot.TeleBot('6745962861:AAF0KOA65a0Lv8Q6i6H7rTTL-NfAVzcculs')

@bot.message_handler(commands=['start'])
def start(message):
    mes =f'Привет,<b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mes, parse_mode='html')

@bot.message_handler()
def get_user(message):
    if message.text =="Hello":  
        bot.send_message(message.chat.id,"И тебе привет", parse_mode='html' )
    elif message.text =="id":
        bot.send_message(message.chat.id,f"Твой ID: {message.from_user.id}",parse_mode='html' )
    else:
        bot.send_message(message.chat.id,"Я тебя понять не могу",parse_mode='html')

bot.polling(none_stop=True)