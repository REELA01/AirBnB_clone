#!/usr/bin/python3
"""define the basemodel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Baesmodel class represnation"""

    def __init__(self, *args, **kwargs):
        """initializetion of BaseModel

           Args:
            *args (any): avoided
            **kwargs (dict): Key/value pairs of attr
        """
        iformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for ke, val in kwargs.items():
                if ke == "created_at" or ke == "updated_at":
                    self.__dict__[ke] = datetime.strptime(val, iformat)
                else:
                    self.__dict__[ke] = val
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """return basemodel dict"""
        dic_c = self.__dict__.copy()
        dic_c["created_at"] = self.created_at.isoformat()
        dic_c["updated_at"] = self.updated_at.isoformat()
        dic_c["__class__"] = self.__class__.__name__
        return dic_c

    def __str__(self):
        """return str represntation of the inctance"""
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
