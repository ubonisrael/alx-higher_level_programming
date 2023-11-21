#!/usr/bin/python3
""" Defines a singly linked list with its node. """


class Node:
    """ Defines the node of a singly linked list. """

    def __init__(self, data, next_node=None):
        """ Initializes the node class. """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves the data of the node. """
        return self.__data

    @property
    def next_node(self):
        """ Retrieves the next pointer of the node. """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ Sets the data of the node to a new value. """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @next_node.setter
    def next_node(self, value):
        """ Sets the next node of a linked list. """
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """ Defines a singly linked list. """
    def __init__(self):
        """ Initializes the singly linked list. """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new node into the list. """
        new_node = Node(value, None)
        current_node = self.__head
        prev_node = None
        if self.__head is None:
            self.__head = new_node
            return
        while current_node != None:
            if current_node.data > new_node.data:
                break
            prev_node = current_node
            current_node = current_node.next_node
        if prev_node is None:
            new_node.next_node = current_node
            self.__head = new_node
        elif current_node is None:
            prev_node.next_node = new_node
            new_node.next_node = None
        else:
            prev_node.next_node = new_node
            new_node.next_node = current_node

    def __str__(self):
        """ Prints the linked list. """
        print_str = ""
        if self.__head is None:
            return print_str
        current_node = self.__head
        while current_node != None:
            print_str += "{:d}".format(current_node.data)
            if current_node.next_node is not None:
                print_str += "\n"
            current_node = current_node.next_node
        return print_str
