from datetime import date
from typing import Literal
from pydantic import BaseModel


class Product(BaseMode):
    id: int
    name: str
    compartment: Literal['Fridge','Freezer']
    shop: str
    qty: float
    unit: str
    expiration_date: date

