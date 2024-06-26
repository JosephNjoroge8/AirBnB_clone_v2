#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {
            obj_key: obj.to_dict() for obj_key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing)
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                classes = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
                }
                FileStorage.__objects = {
                    obj_key: classes[obj_value["__class__"]](**obj_value)
                    for obj_key, obj_value in obj_dict.items()
                }
        except FileNotFoundError:
            pass
