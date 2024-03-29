#!/usr/bin/python3
"""define filestorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FIileSorage calss represnation

     Attributes:
        __file_path (str): file name to save
        __objects (dict): instance dirctory
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __object"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with its key"""
        obnam = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obnam, obj.id)] = obj

    def save(self):
        """"do serilazation prosses"""
        object_1 = {}
        for ke in self.__objects:
            object_1[ke] = self.__objects[ke].to_dict()
        with open(self.__file_path, 'w') as file_1:
            json.dump(object_1, file_1)

    def reload(self):
        """do serilization prosses if json file exist"""
        try:
            with open(FileStorage.__file_path) as file_2:
                dict_1 = json.load(file_2)
                for ob in dict_1.values():
                    class_n = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_n)(**ob))
        except FileNotFoundError:
            return
