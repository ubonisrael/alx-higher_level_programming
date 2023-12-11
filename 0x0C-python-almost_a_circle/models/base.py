#!/usr/bin/python3
""" Contains the Base class. """


class Base:
    """ The base model for all other models. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the base class with an id. """
        if id is None:
            self.id = self.increment_nb()
        else:
            self.id = id

    @classmethod
    def increment_nb(cls):
        """Inrements the number of objects and returns the current value. """
        cls.__nb_objects += 1
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        import json

        if list_dictionaries is None:
            return "[]"
        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        if len(list_dictionaries) == 0:
            return "[]"
        for x in list_dictionaries:
            if type(x) is not dict:
                raise TypeError(
                    "list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        import json

        new_list_objs = []
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string(new_list_objs))
            elif type(list_objs) is not list:
                raise TypeError('list_objs must be a list of instances')
            elif len(list_objs) == 0:
                f.write(cls.to_json_string(new_list_objs))
            else:
                for x in list_objs:
                    if not isinstance(x, Base):
                        raise TypeError('list_objs must be a list of instances')
                    new_list_objs.append(x.to_dictionary())
                f.write(cls.to_json_string(new_list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation of json_string"""
        import json

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        a = cls(1, 1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        instance_list = []
        try:
            with open("{:s}.json".format(cls.__name__), "r") as myFile:
                json_list = cls.from_json_string(myFile.read())
                for json_str in json_list:
                    instance_list.append(cls.create(**json_str))
            return instance_list
        except FileNotFoundError as e:
            return []
