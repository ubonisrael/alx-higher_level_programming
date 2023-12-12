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
        Base.__nb_objects += 1
        return Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        from json import dumps

        if list_dictionaries is None:
            return "[]"

        """json_list = '['
        sorted_list = sorted(
            list_dictionaries, key=lambda x: x['id'], reverse=False)
        for i, x in enumerate(sorted_list):
            json_list += json.dumps(x) + (
                ", " if i+1 < len(sorted_list) else "")
        json_list += ']'"""
        return dumps(list_dictionaries)

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
                        raise TypeError(
                            'list_objs must be a list of instances')
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
        if cls.__name__ == 'Rectangle':
            a = cls(1, 1)
        else:
            a = cls(1)
        if a is not None:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV representation of list_objs to a file"""
        import csv

        list_dict = [x.to_dictionary() for x in list_objs]
        if cls.__name__ == 'Rectangle':
            keys = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            keys = ['id', 'size', 'x', 'y']
        with open("{}.csv".format(cls.__name__), "w", newline='') as csvf:
            dict_writer = csv.DictWriter(csvf, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """loads data from csv file"""
        import csv

        csv_list = []
        with open("{:s}.csv".format(cls.__name__), "r") as csvf:
            reader = csv.DictReader(csvf)
            for row in reader:
                for k, v in row.items():
                    row[k] = int(v)
                csv_list.append(cls.create(**row))
        return csv_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares using the turtle graphics module."""
        import turtle
        from random import randrange

        window = turtle.Screen()
        window.bgcolor("white")

        list_turtles = [turtle.Turtle() for x in list_rectangles]
        for i, y in enumerate(list_rectangles):
            tup = (randrange(0, 10) / 10,
                   randrange(0, 10) / 10,
                   randrange(0, 10) / 10)
            list_turtles[i].shape("circle")
            list_turtles[i].pensize(4)
            list_turtles[i].penup()
            list_turtles[i].goto(y.x, y.y)
            list_turtles[i].pendown()
            list_turtles[i].color("black", tup)
            list_turtles[i].begin_fill()
            for j in range(2):
                list_turtles[i].forward(y.width)
                list_turtles[i].right(90)
                list_turtles[i].forward(y.height)
                list_turtles[i].right(90)
            list_turtles[i].end_fill()
            list_turtles[i].hideturtle()

        list_turtles = [turtle.Turtle() for x in list_squares]
        for i, y in enumerate(list_squares):
            tup = (randrange(0, 10) / 10,
                   randrange(0, 10) / 10,
                   randrange(0, 10) / 10)
            list_turtles[i].shape("circle")
            list_turtles[i].pensize(4)
            list_turtles[i].penup()
            list_turtles[i].goto(y.x, y.y)
            list_turtles[i].pendown()
            list_turtles[i].color("black", tup)
            list_turtles[i].begin_fill()
            for j in range(4):
                list_turtles[i].forward(y.size)
                list_turtles[i].right(90)
            list_turtles[i].end_fill()
            list_turtles[i].hideturtle()
        
        window.exitonclick()
