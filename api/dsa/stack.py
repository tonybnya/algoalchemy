"""
Implementation of a Stack.
Insertion and Deletion follows LIFO (Last In First Out) principle.
"""


class Node:
    def __init__(self, data, next) -> None:
        """
        Modelisation of a Node.
        """
        self.data = data
        self.next = next


class Stack:
    """
    Modelisation of a Stack.
    """

    def __init__(self) -> None:
        """
        Initialization.
        """
        self.top = None

    def peek(self) -> Node:
        """
        Check the item at the top and return it.
        """
        return self.top

    def push(self, data) -> None:
        """
        Add a new node to the top of the Stack.
        """
        next_node = self.top
        new_node = Node(data, next_node)
        self.top = new_node

    def pop(self) -> Node:
        """
        Remove and return the top node of the Stack.
        """
        if self.top is None:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node
