#!/usr/bin/python3
"""Defines a Node of a singly linked list"""


class Node:
    """A node in a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """Initialize a new Node with its data and next node.
        Args:
            data (int): Value of a Node object
            next_node: Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the Node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node of the List.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list.
    """
    def __init__(self):
        """Initialize a new SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """Prepare for the printing of a SinglyLinkedList.
        """
        values = []
        node = self.__head
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new.next_node = node.next_node
            node.next_node = new
