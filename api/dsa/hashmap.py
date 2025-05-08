"""
Implementation of a HashMap.
"""


class Node:
    """
    Modelisation of a Node.
    """

    def __init__(self, data: "Data" = None, next=None) -> None:
        """
        Initialization.
        Runtime: O(1)
        """
        self.data = data
        self.next = next


class Data:
    """
    Modelisation of a Data.
    """

    def __init__(self, key: str, value) -> None:
        """
        Initialization.
        Runtime: O(1)
        """
        self.key = key
        self.value = value


class HashMap:
    """
    Modelisation of a HashMap.
    """

    def __init__(self, size: int) -> None:
        """
        Initialization.
        Runtime: O(size)
        """
        self.size = size
        # self.hash_table = [None] * size
        self.hash_table = [None for i in range(size)]

    def hash_key(self, key: str) -> int:
        """
        Convert the string key into a int hash_value so that,
        0 <= hash_value < len(hash_table)
        Runtime: O(n)  # n is the length of the string key
        """
        s: int = sum(ord(c) for c in key)

        return s % len(self.hash_table)

    def add_key_value(self, key: str, value) -> None:
        """
        Add a key value pair to the hash_table.
        Runtime: O(1), when no collision (desired behavior)

        Visual representation of a hash_table of size 4:

            [
        [0]     [ 'hello', 'world' ] -> None  # hashing key `hello` result to 0
        [1]     [ 'hi', 'there' ] -> [ 'ih', 'aya' ] -> None  # collision because hashing `hi` and `ih` keys result to the same result 1 with size 4
        [2]     None,
        [3]     None,
            ]
        """
        hashed_key: int = self.hash_key(key)
        if self.hash_table[hashed_key] is None:
            node = Node(Data(key, value), None)
            self.hash_table[hashed_key] = node
        else:
            # collision here
            temp = self.hash_table[hashed_key]  # temp is the head
            while temp.next:
                temp = temp.next

            # at this stage, next node is None
            # so, temp is at the tail node
            # create the new node pointing to None
            node = Node(Data(key, value), None)
            temp.next = node

    def get_value(self, key: str):
        """
        Get a value by its key.
        Runtime: O(1), when no collision (desired behavior)
        """
        hashed_key: int = self.hash_key(key)
        if self.hash_table[hashed_key] is not None:
            temp: Node = self.hash_table[hashed_key]
            # if no collision
            if temp.next is None:
                return temp.data.value
            # if collision
            while temp.next:
                if key == temp.data.key:
                    return temp.data.value
                temp = temp.next

            if key == temp.data.key:
                return temp.data.value

        return None

    def print_hash_table(self):
        """
        Print a string representation of the hash_table.
        """
        print("[")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                ll_str = ""
                temp = val
                if temp.next:
                    while temp.next:
                        ll_str += f"[ {temp.data.key} : {temp.data.value} ] -> "
                        temp = temp.next
                    ll_str += f"[ {temp.data.key} : {temp.data.value} ] -> None"
                    print(f"  [{i}] {ll_str}")
                else:
                    print(f"  [{i}] [ {val.data.key} : {val.data.value} ] -> None")
            else:
                print(f"  [{i}] {val}")
        print("]")
