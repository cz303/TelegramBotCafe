import telebot

bot = telebot.TeleBot("951388162:AAEtCaLOXZMXrepJ4S0r09bKHNzdZQNxyuE")

@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Выбрать кофе', 'Помощь')
    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Выбрать кофе":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Латте', 'Капучино', 'Американо')
        bot.send_message(message.from_user.id, 'Выберите кофе', reply_markup=user_markup)
    elif message.text == "Латте" or message.text == "Капучино" or message.text == "Американо":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('0,2', '0,3', '0,5')
        bot.send_message(message.from_user.id, 'Выберите объем', reply_markup=user_markup)
    elif message.text == "0,2" or message.text == "0,3" or message.text == "0,5":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Да, оплатить заказ', 'Нет, хочу поменять заказ')
        bot.send_message(message.from_user.id, 'Все правильно?', reply_markup=user_markup)
    elif message.text == "Да, оплатить заказ":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Оплата','Нет, хочу поменять заказ')
        bot.send_message(message.from_user.id, 'Okey', reply_markup=user_markup)
    elif message.text == "Нет, хочу поменять заказ":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Выбрать кофе')
        bot.send_message(message.from_user.id, 'Выберите объем', reply_markup=user_markup)
    elif message.text == "Оплата":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Отправить деньги','Нет, хочу поменять заказ')
        bot.send_message(message.from_user.id, 'Отправьте деньги на этот etherium-кошелек:'+'0x7861D09Eb3A1bBBd9Ff493dcF8d2ded089144c39', reply_markup=user_markup)
    else:
        print("Ваш запрос не распознан")


bot.polling(none_stop=True, interval=0)
