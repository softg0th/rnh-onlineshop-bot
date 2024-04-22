from pydantic import Field, HttpUrl
from beanie import Document


class Item(Document):
    id: str = Field(alias="_id", default=None)
    name: str = Field(...)
    description: str = Field(...)
    url: HttpUrl = Field(...)
    photo: str = Field(default=None)
    category_name: str = Field(...)
    category_id: str = Field(...)
