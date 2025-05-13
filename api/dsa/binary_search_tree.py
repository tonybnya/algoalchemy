"""
Implementation of a Binary Search Tree.
"""


class Node:
    """
    Modelisation of a Node.
    """

    def __init__(self, data=None) -> None:
        """
        Initialisation.
        """
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    Modelisation of the wrapper as a Binary Search Tree.
    """

    def __init__(self) -> None:
        """
        Initialisation.
        """
        self.root = None

    def _insert_recursive(self, value, node):
        """
        Recursively check each node to insert the value in the right place.
        """
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)
        else:
            return

    def insert(self, value) -> None:
        """
        Insert a node with the value `value` in the BST.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            # _insert_recursive is a private method (starts with _)
            self._insert_recursive(value, self.root)
