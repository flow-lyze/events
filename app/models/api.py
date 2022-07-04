from pydantic import BaseModel
from typing import Optional


class Response(BaseModel):
    status_code: int
    message: Optional[str] = None
    error: Optional[str] = None


class Event(BaseModel):
    """
        Model, represents hackathon event object

        Fields:
            name (str): a string name of event.
            date (str): a str, represents date, when event will happen.
            price (optional|int): an optional field, represents price to join an event.
            prize (str): a string, represents winner's prize of event.
    """
    id: Optional[str] = None
    name: str
    date: str
    price: Optional[int] = None
    prize: str
