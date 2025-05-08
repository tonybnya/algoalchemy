"""
Implementation of a Linked List.
"""


class Node:
    """
    Modelisation of a Node.
    """

    def __init__(self, data=None, next=None) -> None:
        """
        Initialization.
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Modelisation of a Linked List.
    """

    def __init__(self) -> None:
        """
        Initialization.
        """
        self.head = None
        self.tail = None

    # def print_ll(self) -> None:
    #     """
    #     Printer of the Linked List.
    #     """
    #     ll_str: str = ""
    #
    #     temp = self.head
    #     if self.head is None:
    #         print(None)
    #         return
    #
    #     while temp:
    #         ll_str += f"[ {str(temp.data)} ] -> "
    #         temp = temp.next
    #
    #     ll_str += "None"
    #     print(ll_str)

    # def insert_at_beginning(self, data) -> None:
    #     """
    #     Insert a node with 'data' at the beginning of the Linked List.
    #     """
    #     node = Node(data, self.head)
    #     self.head = node
