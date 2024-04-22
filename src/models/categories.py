from typing import List

from pydantic import Field
from beanie import Document


class Category(Document):
    id: str = Field(alias="_id", default=None)
    name: str = Field(...)
    description: str = Field(...)
    appeals: int = Field(default=0)
    items: List = Field(...)
