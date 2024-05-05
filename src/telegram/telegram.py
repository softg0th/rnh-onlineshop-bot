from dataclasses import dataclass

import telebot
from telebot import types

from src.config import common_messages
from src.config import BOT_TOKEN
from src.utils.db_interactions import DbCrud

bot = telebot.TeleBot(BOT_TOKEN)


@dataclass
class UserLevel:
    level: int


user_level = UserLevel(-1)


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
    levels = {'Начинающий': "0",
              'Средний': "1",
              'Продвинутый': "2"}

    markup = create_menu(levels)
    bot.send_message(message.chat.id, 'Выберите уровень подготовки', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def send_menu_types(callback):
    if callback.message:
        if callback.data in ("lose", "gain", "flex") and user_level.level != -1:
            user_type_level = -1
            if callback.data == 'lose':
                user_type_level = 0
            elif callback.data == 'gain':
                user_type_level = 1
            elif callback.data == 'flex':
                user_type_level = 2

            category_id = db.grep_categories(user_level.level, user_type_level)
            try:
                items = db.grep_items(category_id)
                db.add_click(category_id)
                message_container = []
                for item in items:
                    formatted_item = (f'*{item['name']}.*\n'
                                      f'Описание: {item['description']}\n'
                                      f'[Заказать]({item['url']})\n'
                                      f'{item['photo']}\n')
                    message_container.append(formatted_item)
                message_container = ''.join(message_container)
                bot.edit_message_text(chat_id=callback.message.chat.id,
                                      message_id=callback.message.message_id,
                                      text=f"Товары: {message_container}",
                                      parse_mode='Markdown')
            except Exception as ex:
                print(ex)
                bot.edit_message_text(chat_id=callback.message.chat.id,
                                      message_id=callback.message.message_id,
                                      text=f"Внутренняя ошибка!")
            user_level.level = -1

        else:
            user_level.level = int(callback.data)
            goal = {
                'Похудение': "lose",
                'Набор массы': "gain",
                'Гибкость': "flex"
            }

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                  text="Выберите цель тренировки",
                                  reply_markup=create_menu(goal))


@bot.message_handler(content_types=['text'])
def reply_to_text(message):
    bot.reply_to(message, common_messages.get('error'))


db = DbCrud()
bot.infinity_polling()
