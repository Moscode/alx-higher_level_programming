#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if (type(data) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if (next_node is not None and type(next_node) != Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (type(value) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None and type(value) != Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        """
        sorting and inserting method
        """
    def sorted_insert(self, value):
        """Inserts a node to the singly linked list
        The node is inserted at an ordered position in the list
        Args:
            value (Node): The node to insert
        """

        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head

            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node

            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Defines the printing of a singly linked list"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node

        return '\n'.join(values)
