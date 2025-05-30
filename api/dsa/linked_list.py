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
        Runtime: O(1)
        """
        self.head = None
        self.tail = None

    def print_ll(self) -> None:
        """
        Printer of the Linked List.
        Runtime: O(n)
        """
        ll_str: str = ""

        temp = self.head
        if self.head is None:
            print(None)
            return

        while temp:
            ll_str += f"[ {str(temp.data)} ] -> "
            temp = temp.next

        ll_str += "None"
        print(ll_str)

    def add_to_head(self, data) -> None:
        """
        Add a node containing 'data' at the beginning of the list.
        Runtime: O(1)
        """
        # keep track of both head and tail
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = self.head
            return

        node = Node(data, self.head)
        self.head = node

    def add_to_tail(self, data) -> None:
        """
        Add a node containing 'data' at the end of the list.
        Runtime: O(1)
        """
        if self.head is None:
            self.add_to_head(data)
            return

        # as we also keep track of the tail
        # insert to tail is just in O(1) runtime
        node = Node(data)
        self.tail.next = node
        self.tail = node

    def ll_to_list(self) -> list:
        """
        Convert a Linked List into a regular list.
        Runtime: O(n)
        Extra memory space: O(n)
        """
        lst: list = []
        if self.head is None:
            return lst

        temp = self.head
        while temp:
            lst.append(temp.data)
            temp = temp.next
        return lst

    def get_user_by_id(self, user_id):
        """
        Get the node containing the id `user_id`.
        Runtime: O(n)
        """
        temp = self.head
        while temp:
            if temp.data["id"] is int(user_id):
                return temp.data
            temp = temp.next

        return None
