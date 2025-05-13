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
    bst = BST()
    bst.insert(10)
    assert bst.root is not None
    assert bst.root.data == 10


def test_insert_left_and_right_children():
    """
    Test insertion at left and right.
    """
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)

    assert bst.root.left.data == 5
    assert bst.root.right.data == 15


def test_recursive_insert_multiple_levels():
    """
    Test insertion at multiple levels.
    """
    bst = BST()
    values = [10, 5, 15, 2, 7, 12, 20]
    for val in values:
        bst.insert(val)

    assert bst.root.data == 10

    assert bst.root.left.data == 5
    assert bst.root.left.left.data == 2
    assert bst.root.left.right.data == 7

    assert bst.root.right.data == 15
    assert bst.root.right.right.data == 20
    assert bst.root.right.left.data == 12


# def test_no_duplicates_inserted():
#     bst = BST()
#     bst.insert(10)
#     bst.insert(5)
#     bst.insert(10)  # duplicate
#     assert bst.root.data == 10
#     assert bst.root.left.data == 5
#     assert bst.root.right is None
