import telebot
from telebot import types

from src.config import common_messages
from src.config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


def create_menu(btn_list: dict) -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    for element in btn_list.items():
        btn = types.InlineKeyboardButton(text=element[0], callback_data=element[1])
        markup.add(btn)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, common_messages.get('hello'))


@bot.message_handler(commands=['choice'])
def make_choice(message):
    levels = {'Начинающий': 'low',
              'Средний': 'medium',
              'Продвинутый': 'advanced'}

    markup = create_menu(levels)
    bot.send_message(message.chat.id, 'Выберите уровень подготовки', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def send_menu_types(callback):
    if callback.message:
        if callback.data == 'gain':
            bot.edit_message_text(chat_id=callback.message.chat.id,
                                  message_id=callback.message.message_id,
                                  text="Просто жри")
        elif callback.data == 'drop':
            bot.edit_message_text(chat_id=callback.message.chat.id,
                                  message_id=callback.message.message_id,
                                  text="Просто не ешь")
        elif callback.data == 'flex':
            bot.edit_message_text(chat_id=callback.message.chat.id,
                                  message_id=callback.message.message_id,
                                  text="Просто качай жопу")
        else:
            goal = {
                'Набор массы': 'gain',
                'Похудение': 'drop',
                'Гибкость': 'flex'
            }

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                  text="Выберите цель тренировки",
                                  reply_markup=create_menu(goal))


@bot.message_handler(content_types=['text'])
def reply_to_text(message):
    bot.reply_to(message, common_messages.get('error'))


bot.infinity_polling()
