from interfaces.db_interface import DbCRUDInterface
from db import items_collection, categories_collection


class DbCrud(DbCRUDInterface):
    def grep(self, category_id) -> list:
        category_object = categories_collection.find_one({"_id": category_id})
        items_data = []

        for item in category_object.get('items'):
            items_data.append({'name': item.get('name'),
                               'description': item.get('description'),
                               'url': item.get('url'),
                               'photo': item.get('photo')})
        return items_data

    def add_click(self, category_id) -> None:
        categories_collection.update_one({'_id': category_id},
                                         {"$inc": {"appeals": 1}})
        return
