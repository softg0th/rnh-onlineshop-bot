import telebot

from src.config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)
bot.infinity_polling()
