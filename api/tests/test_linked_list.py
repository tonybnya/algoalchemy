"""
Test file.
"""

import os
import sys

# Add the parent directory of dsa to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now we can import directly from the dsa directory
from dsa.linked_list import LinkedList, Node


def test_linked_list_initial_state():
    """
    Test for initial state of a Linked List.
    """
    ll = LinkedList()
    assert ll.head is None
    assert ll.tail is None


# def test_linked_list_initial_print(capsys):
#     """
#     Test print_ll() when the list is initialized.
#
#     capsys.readouterr() captures what was printed to stdout.
#     .strip() removes any trailing newline.
#     The assertion checks that "None" was printed, as expected for an empty list.
#     """
#     ll = LinkedList()
#     ll.print_ll()
#     captured = capsys.readouterr()
#     assert captured.out.strip() == "None"


# def test_add_to_head_on_empty_list():
#     """
#     Test to add to the head of an empty Linked List.
#     """
#     ll = LinkedList()
#     node = Node("A")
#     ll.add_to_head(node)
#     assert ll.head == node
#     assert ll.head.val == "A"
#     assert ll.head.next is None
#
#
# def test_add_to_head_on_non_empty_list():
#     """
#     Test to add to the head of an non-empty Linked List.
#     """
#     ll = LinkedList()
#     node1 = Node("A")
#     node2 = Node("B")
#
#     ll.add_to_head(node1)
#     ll.add_to_head(node2)
#
#     assert ll.head == node2
#     assert ll.head.val == "B"
#     assert ll.head.next == node1
#     assert ll.head.next.val == "A"
#     assert ll.head.next.next is None
#
#
# def test_multiple_add_to_head():
#     """
#     Test to add multiple values to the head of an empty Linked List.
#     """
#     ll = LinkedList()
#     values = ("C", "B", "A")
#     for val in values:
#         ll.add_to_head(Node(val))
#
#     assert [node.val for node in ll] == ["A", "B", "C"]
#
#
# def test_iter_empty_list():
#     """
#     Test for empty Linked List iteration.
#     """
#     ll = LinkedList()
#     assert list(ll) == []
#
#
# def test_iter_single_node():
#     """
#     Test for single-node Linked List iteration.
#     """
#     ll = LinkedList()
#     node = Node("A")
#     ll.head = node
#     assert [n.val for n in ll] == ["A"]
#
#
# def test_iter_multiple_nodes():
#     """
#     Test for multi-node Linked List iteration.
#     """
#     ll = LinkedList()
#     node1 = Node("A")
#     node2 = Node("B")
#     node3 = Node("C")
#     node1.set_next(node2)
#     node2.set_next(node3)
#     ll.head = node1
#
#     assert [n.val for n in ll] == ["A", "B", "C"]
#
#
# def test_linked_list_to_list():
#     """
#     Test for Linked List to regular list conversion.
#     """
#     ll = LinkedList()
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node1.set_next(node2)
#     node2.set_next(node3)
#     ll.head = node1
#
#     assert ll.ll_to_list() == [1, 2, 3]
#
#
# def test_iter_mixed_data():
#     """
#     Test for Linked List with mixed data types.
#     """
#     ll = LinkedList()
#     node1 = Node("X")
#     node2 = Node(42)
#     node3 = Node(None)
#     node1.set_next(node2)
#     node2.set_next(node3)
#     ll.head = node1
#
#     assert ll.ll_to_list() == ["X", 42, None]
#
#
# def test_repr_empty_list():
#     """
#     Test for string representation of an empty Linked List.
#     """
#     ll = LinkedList()
#     assert repr(ll) == ""
#
#
# def test_repr_single_node():
#     """
#     Test for string representation of a Linked List with a single node.
#     """
#     ll = LinkedList()
#     node = Node("A")
#     ll.head = node
#     assert repr(ll) == "A"
#
#
# def test_repr_multiple_nodes():
#     """
#     Test for string representation of a Linked List with a multiple nodes.
#     """
#     ll = LinkedList()
#     node1 = Node("A")
#     node2 = Node("B")
#     node3 = Node("C")
#     node1.set_next(node2)
#     node2.set_next(node3)
#     ll.head = node1
#     assert repr(ll) == "A -> B -> C"
#
#
# def test_add_to_tail():
#     """
#     Test for adding to the tail of a Linked List.
#     """
#     ll = LinkedList()
#
#     # add first node
#     node1 = Node("a")
#     ll.add_to_tail(node1)
#     assert ll.head == node1
#     assert ll.head.next is None
#
#     # add second node
#     node2 = Node("b")
#     ll.add_to_tail(node2)
#     assert ll.head.next == node2
#     assert ll.head.next.next is None
#
#     # add third node
#     node3 = Node("c")
#     ll.add_to_tail(node3)
#     assert ll.head.next.next == node3
#     assert ll.head.next.next.next is None
#
#     # check __repr__
#     assert repr(ll) == "a -> b -> c"
#
#
#
#
# def test_add_to_middle():
#     """
#     Test to add a node to a middle of the Linked List.
#     """
#     ll = LinkedList()
#     ll.add_to_tail(Node("A"))
#     ll.add_to_tail(Node("B"))
#     ll.add_to_tail(Node("D"))
#     ll.add_to_tail(Node("E"))
#     ll.add_to_tail(Node("F"))
#     ll.add_to_middle(2, Node("C"))
#     assert ll.ll_to_list() == ["A", "B", "C", "D", "E", "F"]
#
#
# def test_remove_to_head():
#     """
#     Test to remove a node to the head of the Linked List.
#     """
#     ll = LinkedList()
#     ll.add_to_tail(Node("A"))
#     ll.add_to_tail(Node("B"))
#     removed: Node | None = ll.remove_to_head()
#     assert removed.val == "A"
#     assert ll.ll_to_list() == ["B"]
#
#
# def test_remove_to_tail():
#     """
#     Test to remove a node to the tail of the Linked List.
#     """
#     ll = LinkedList()
#     ll.add_to_tail(Node("A"))
#     ll.add_to_tail(Node("B"))
#     removed = ll.remove_to_tail()
#     assert removed.val == "B"
#     assert ll.ll_to_list() == ["A"]
#
#
# def test_remove_to_middle():
#     """
#     Test to remove a node to the middle of the Linked List.
#     """
#     ll = LinkedList()
#     ll.add_to_tail(Node("A"))
#     ll.add_to_tail(Node("B"))
#     ll.add_to_tail(Node("C"))
#     removed = ll.remove_to_middle(1)
#     assert removed.val == "B"
#     assert ll.ll_to_list() == ["A", "C"]
