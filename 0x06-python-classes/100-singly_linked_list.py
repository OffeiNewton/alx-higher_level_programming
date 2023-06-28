#!/usr/bin/python3

class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiates a Node object with data and next_node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the Node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the Node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node of the Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of the Node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Instantiates an empty SinglyLinkedList"""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list (increasing order)"""
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list"""
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
