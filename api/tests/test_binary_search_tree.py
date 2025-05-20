# """
# Test file.
# """
#
# import os
# import sys
#
# # Add the parent directory of dsa to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#
# # Now we can import directly from the dsa directory
# from dsa.binary_search_tree import BST, Node
#
#
# def test_insert_root():
#     """
#     Test insertion at the root.
#     """
#     bst = BST()
#     bst.insert(10)
#     assert bst.root is not None
#     assert bst.root.data == 10
#
#
# def test_insert_left_and_right_children():
#     """
#     Test insertion at left and right.
#     """
#     bst = BST()
#     bst.insert(10)
#     bst.insert(5)
#     bst.insert(15)
#
#     assert bst.root.left.data == 5
#     assert bst.root.right.data == 15
#
#
# def test_recursive_insert_multiple_levels():
#     """
#     Test insertion at multiple levels.
#     """
#     bst = BST()
#     values = [10, 5, 15, 2, 7, 12, 20]
#     for val in values:
#         bst.insert(val)
#
#     assert bst.root.data == 10
#
#     assert bst.root.left.data == 5
#     assert bst.root.left.left.data == 2
#     assert bst.root.left.right.data == 7
#
#     assert bst.root.right.data == 15
#     assert bst.root.right.right.data == 20
#     assert bst.root.right.left.data == 12
#
#
# def test_no_duplicates_inserted():
#     """
#     Test insert a duplicate.
#     """
#     bst = BST()
#     bst.insert(10)
#     bst.insert(5)
#     bst.insert(10)
#     assert bst.root.data == 10
#     assert bst.root.left.data == 5
#     assert bst.root.right is None

import os
import sys

# Add the parent directory of dsa to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dsa.binary_search_tree import BST, Node


def test_insert_root():
    bst = BST()
    bst.insert(10)
    assert bst.root is not None
    assert bst.root.data == 10


def test_insert_left_and_right_children():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)

    assert bst.root.left.data == 5
    assert bst.root.right.data == 15


def test_recursive_insert_multiple_levels():
    bst = BST()
    values = [10, 5, 15, 2, 7, 12, 20]
    for val in values:
        bst.insert(val)

    assert bst.root.data == 10

    assert bst.root.left.data == 5
    assert bst.root.left.left.data == 2
    assert bst.root.left.right.data == 7

    assert bst.root.right.data == 15
    assert bst.root.right.left.data == 12
    assert bst.root.right.right.data == 20


def test_no_duplicates_inserted():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(10)  # duplicate
    assert bst.root.data == 10
    assert bst.root.left.data == 5
    assert bst.root.right is None


def test_search_existing_integer():
    bst = BST()
    values = [10, 5, 15, 2, 7]
    for val in values:
        bst.insert(val)

    result = bst.search("2")  # search uses string input
    assert result == 2


def test_search_non_existing_integer():
    bst = BST()
    values = [10, 5, 15, 2, 7]
    for val in values:
        bst.insert(val)

    result = bst.search("99")
    assert result is False


def test_search_in_empty_tree():
    bst = BST()
    assert bst.search("1") is False


# -- Dict-based tests (simulate BlogPost-like data) --


def test_insert_dict_nodes():
    bst = BST()
    blog1 = {"id": 10, "title": "First"}
    blog2 = {"id": 5, "title": "Second"}
    blog3 = {"id": 15, "title": "Third"}

    bst.insert(blog1)
    bst.insert(blog2)
    bst.insert(blog3)

    assert bst.root.data["id"] == 10
    assert bst.root.left.data["id"] == 5
    assert bst.root.right.data["id"] == 15


def test_search_existing_dict_node():
    bst = BST()
    blog1 = {"id": 10, "title": "First"}
    blog2 = {"id": 5, "title": "Second"}
    blog3 = {"id": 15, "title": "Third"}

    bst.insert(blog1)
    bst.insert(blog2)
    bst.insert(blog3)

    found = bst.search("15")
    assert isinstance(found, dict)
    assert found["title"] == "Third"


def test_search_non_existing_dict_node():
    bst = BST()
    blog1 = {"id": 10, "title": "First"}
    blog2 = {"id": 5, "title": "Second"}

    bst.insert(blog1)
    bst.insert(blog2)

    not_found = bst.search("99")
    assert not_found is False


def test_do_not_insert_duplicate_dict_node():
    bst = BST()
    blog1 = {"id": 10, "title": "First"}
    blog2 = {"id": 5, "title": "Second"}
    duplicate = {"id": 10, "title": "Duplicate"}

    bst.insert(blog1)
    bst.insert(blog2)
    bst.insert(duplicate)

    # Only one node should exist with id=10
    assert bst.root.data["title"] == "First"
    assert bst.root.right is None  # No duplicate on right
