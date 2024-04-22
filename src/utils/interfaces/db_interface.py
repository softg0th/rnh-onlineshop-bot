from abc import ABC, abstractmethod


class DbCRUDInterface(ABC):
    def grep(self, category_id) -> list:
        pass

    def add_click(self, category_id) -> None:
        pass
