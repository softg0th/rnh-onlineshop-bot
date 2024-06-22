from pymongo import MongoClient

from src.config import DB_URL, DB_NAME


client = MongoClient(DB_URL)
database = client[DB_NAME]

items_collection = database['items']
categories_collection = database['categories']
users_collection = database['users']


