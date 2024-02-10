#!/usr/bin/python3
"""define user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User calss represnation"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
