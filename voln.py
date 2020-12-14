import telebot
from conf import t
bot = telebot.TeleBot(t)

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет, {message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')





@bot.message_handler(content_types=['text'])
def mess(message):
    final_mess = ""
    get_message_bot = message.text.strip()
    for i, s in enumerate(get_message_bot):
        if i % 2 == 0:           
            final_mess += s.upper() 
        else:
            final_mess += s

    bot.send_message(message.chat.id, final_mess, parse_mode='html')

bot.polling(none_stop=True)
