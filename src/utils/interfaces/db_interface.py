from abc import ABC, abstractmethod


class DbCRUDInterface(ABC):
    @abstractmethod
    def grep_categories(self, level, type_cat):
        pass

    @abstractmethod
    def grep_items(self, category_id) -> list:
        pass

    @abstractmethod
    def insert_user(self, user_object) -> bool:
        pass

    @abstractmethod
    def drop_user(self, chat_id) -> bool:
        pass

    @abstractmethod
    def update_user_cats(self, chat_id, category_id):
        pass

    @abstractmethod
    def add_click(self, category_id) -> None:
        pass
