import telebot
from telebot import types

BOT_TOKEN = ''

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать в группу ваш ювелир!\nЗдесь вы можете заказать изготовление изделий любой сложности,лазерную гравировку,лазерную пайку и ремонт любой сложности")

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Заказать изделие", url='https://t.me/Jeweler_lg')
    item2 = types.InlineKeyboardButton("Услуги ремонта", callback_data='button2')
    item3 = types.InlineKeyboardButton("Задать вопрос", url='https://t.me/Jeweler_lg')
    item4 = types.InlineKeyboardButton("Донат на развитие",url='https://yoomoney.ru/')
    item5 = types.InlineKeyboardButton("Связаться с ювелиром", url='https://t.me/Jeweler_lg')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Выберите услугу:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == 'button1':
        bot.answer_callback_query(call.id, "Вы нажали кнопку заказать изделие!")
        bot.send_message(call.message.chat.id, "")

    elif call.data == 'button2':
        bot.answer_callback_query(call.id, "Вы нажали кнопку услуги ремонта!")
        bot.send_message(call.message.chat.id, "Ваши любимые украшения нуждаются в заботе?\nЯ предлагаю профессиональный ремонт ювелирных изделий любой сложности\nВерну вашим украшениям первозданный вид! ")

    elif call.data == 'button3':
        bot.answer_callback_query(call.id, "Вы нажали кнопку задать вопрос!")
        bot.send_message(call.message.chat.id, "")
    elif call.data == 'button4':
        bot.answer_callback_query(call.id, "Вы нажали кнопку донат на развитие!")
        bot.send_message(call.message.chat.id, "")

    elif call.data == 'button5':
        bot.answer_callback_query(call.id, "Вы нажали кнопку связаться с ювелиром!")
        bot.send_message(call.message.chat.id, "")

    else:
        bot.answer_callback_query(call.id, "Что-то пошло не так...")

print('bot start')
bot.infinity_polling()