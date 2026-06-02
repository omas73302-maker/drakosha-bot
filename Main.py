import telebot TOKEN = "8957128191:AAFwQhIkR8gMzl5U1S_7mbCV30xwGwaCqCw"
bot = telebot.TeleBot(TOKEN) @bot.message_handler(commands=['start'])
def start(message): bot.reply_to(message, "Привет! Я Дракоша.ТВ 🦎") bot.polling(none_stop=True)
