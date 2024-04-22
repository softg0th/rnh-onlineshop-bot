import telebot
from telebot import types

from src.config import common_messages
from src.main import bot


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, common_messages.get('hello'))


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, common_messages.get('help'))


@bot.message_handler(content_types=['text'])
def reply_to_text(message):
    bot.reply_to(message, common_messages.get('error'))
