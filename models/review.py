#!/usr/bin/python3
"""define Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class repersntation"""

    place_id = ""
    user_id = ""
    text = ""
