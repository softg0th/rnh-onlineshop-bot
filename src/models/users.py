from typing import List

from beanie import Document
from pydantic import Field, HttpUrl


class User(Document):
    id: str = Field(alias="_id", default=None)
    chat_id: int = Field(...)
    age: int = Field(...)
    sex: str = Field(...)
    categories: List = Field(...)
