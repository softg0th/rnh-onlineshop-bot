from abc import ABC, abstractmethod


class DbCRUDInterface(ABC):
    @abstractmethod
    def grep_categories(self, level, type_cat):
        pass

    @abstractmethod
    def grep_items(self, category_id) -> list:
        pass

    @abstractmethod
    def add_click(self, category_id) -> None:
        pass
