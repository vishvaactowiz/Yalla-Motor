from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional
import re
from pydantic import field_validator


class Store(BaseModel):
    id: str = Field(pattern=r"^[A-Z]{2}\d{3}$")  # AP301, AN401 etc.
    store_name: str = Field(min_length=2)
    url: Optional[HttpUrl] = None
    full_address: str = Field(min_length=5)
    phone1: Optional[str] = None
    dealer_type: Optional[str] = None

    @field_validator("phone1")
    def clean_phone(cls, v):
        if v:
            return re.sub(r"\D", "", v)
        return v


class City(BaseModel):
    city_name: str
    city_code: str
    stores: List[Store]


class State(BaseModel):
    state_name: str
    state_code: str
    cities: List[City]