"""
Implementation of a Queue.
Insertion and Deletion follows FIFO (First In First Out) principle.
"""


class Node:
    def __init__(self, data, next) -> None:
        """
        Modelisation of a Node.
        """
        self.data = data
        self.next = next


class Queue:
    """
    Modelisation of a Queue.
    """

    def __init__(self) -> None:
        """
        Initialization.
        """
        self.head = None
        self.tail = None

    def enqueue(self, data) -> None:
        """
        Add a new node to the end of the Queue.
        """
        node = Node(data, None)
        if self.head is None and self.tail is None:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node
        return

    def dequeue(self) -> None:
        """
        Remove the node to the head of the Queue.
        """
        if self.head is None:
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_node
