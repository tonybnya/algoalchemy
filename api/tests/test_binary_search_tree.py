"""
Test file.
"""

import os
import sys

# Add the parent directory of dsa to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now we can import directly from the dsa directory
from dsa.binary_search_tree import BST, Node


def test_insert_root():
    """
    Test insertion at the root.
    """
    tree = BST()
    tree.insert(10)
    assert tree.root is not None
    assert tree.root.data == 10


# def test_insert_left_and_right_children():
#     tree = BST()
#     tree.insert(10)
#     tree.insert(5)
#     tree.insert(15)
#
#     assert tree.root.left.data == 5
#     assert tree.root.right.data == 15
#
#
# def test_recursive_insert_multiple_levels():
#     tree = BST()
#     values = [10, 5, 15, 2, 7, 12, 20]
#     for val in values:
#         tree.insert(val)
#
#     assert tree.root.left.left.data == 2
#     assert tree.root.left.right.data == 7
#     assert tree.root.right.left.data == 12
#     assert tree.root.right.right.data == 20
#
#
# def test_no_duplicates_inserted():
#     tree = BST()
#     tree.insert(10)
#     tree.insert(5)
#     tree.insert(10)  # duplicate
#     assert tree.root.data == 10
#     assert tree.root.left.data == 5
#     assert tree.root.right is None
