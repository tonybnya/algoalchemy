"""
Implementation of a Binary Search Tree.
"""

from app.models.blogpost import BlogPost


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
    Modelisation of the wrapper class for the Binary Search Tree.
    """

    def __init__(self) -> None:
        """
        Initialisation.
        """
        self.root = None

    def _get_value(self, data):
        """
        Helper method to extract the comparison value from data.
        If data is a dictionary with an 'id' key, use that value.
        Otherwise, use the data value directly.
        """
        if isinstance(data, dict) and "id" in data:
            return data["id"]
        return data

    def _insert_recursive(self, data, node):
        """
        Private method used only by the insert() method.
        Recursively check each node to insert the value in the right place.
        """
        data_value = self._get_value(data)
        node_value = self._get_value(node.data)

        if data_value < node_value:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data_value > node_value:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            # a BST should not contain duplicates
            # this stage means the BST already contains the given data
            return

    def insert(self, data) -> None:
        """
        Insert a node with the data `data` in the BST.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            # _insert_recursive is a private method (starts with _)
            self._insert_recursive(data, self.root)

    def _search_recursive(self, blogpost_id, node):
        """
        Private method used only by the search() method.
        Recursively check each node to find a specific blogpost_id.
        """
        # if node.left is None and node.right is None:
        #     return False

        node_value = self._get_value(node.data)

        if blogpost_id == node_value:
            return node.data

        if blogpost_id < node_value and node.left is not None:
            left_value = self._get_value(node.left.data)
            if blogpost_id == left_value:
                return node.left.data
            return self._search_recursive(blogpost_id, node.left)

        if blogpost_id > node_value and node.right is not None:
            right_value = self._get_value(node.right.data)
            if blogpost_id == right_value:
                return node.right.data
            return self._search_recursive(blogpost_id, node.right)

        return False

    def search(self, blogpost_id: str) -> BlogPost | bool:
        """
        Search for blogpost by its ID.
        """
        # the blogpost_id from the URL is a string
        blogpost_id = int(blogpost_id)

        if self.root is None:
            return False

        # _search_recursive is a private method (starts with _)
        return self._search_recursive(blogpost_id, self.root)
