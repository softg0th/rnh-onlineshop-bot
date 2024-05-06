import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

DB_HOST = os.getenv('MONGO_HOST')
DB_PORT = os.getenv('MONGO_PORT')
DB_USER = os.getenv('MONGO_USER')
DB_PASSWORD = os.getenv('MONGO_PASSWORD')
DB_URL = os.getenv('MONGO_URL')
DB_NAME = os.getenv('DB_NAME')


common_messages = {
    'error': 'Пожалуйста, взаимодействуйте с ботом посредством команд или меню!',
    'hello': 'Здравствуйте! Вас привестсвует помощник по подбору спортивных товаров FitTorg! Если Вам не понятно, как использовать'
             'меня, нажмите /help. Для выбора товаров нажмите /choice.',
    'help': '...',
}
