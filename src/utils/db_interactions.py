from src.utils.interfaces.db_interface import DbCRUDInterface
from src.utils.db import items_collection, categories_collection, users_collection


class DbCrud(DbCRUDInterface):

    def grep_categories(self, level, type_cat):
        category_query = {"$and": [{"level": level}, {"type": type_cat}]}
        category = categories_collection.find_one(category_query)
        return category['_id']

    def grep_items(self, category_id) -> list:
        category_object = items_collection.find({"category_id": category_id})
        items_data = []

        for item in category_object:
            items_data.append({'name': item.get('name'),
                               'description': item.get('description'),
                               'url': item.get('url'),
                               'photo': item.get('photo')})
        return items_data

    def insert_user(self, user_object) -> bool:
        try:
            users_collection.insert_one(user_object)
            return True

        except Exception:
            return False

    def drop_user(self, chat_id):
        users_collection.delete_one({'chat_id': chat_id})

    def update_user_cats(self, chat_id, category_id):
        users_collection.update_one({'chat_id': chat_id}, {'$push': {'categories': category_id}})

    def add_click(self, category_id) -> None:
        categories_collection.update_one({'_id': category_id},
                                         {"$inc": {"appeals": 1}})
        return
