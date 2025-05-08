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


def test_linked_list_initial_print(capsys):
    """
    Test print_ll() when the list is initialized.

    capsys.readouterr() captures what was printed to stdout.
    .strip() removes any trailing newline.
    The assertion checks that "None" was printed, as expected for an empty list.
    """
    ll = LinkedList()
    ll.print_ll()
    captured = capsys.readouterr()
    assert captured.out.strip() == "None"


def test_add_to_head_on_empty_list():
    """
    Test to add to the head of an empty Linked List.
    """
    ll = LinkedList()
    ll.add_to_head("A")
    assert ll.head.data == "A"
    assert ll.head.next is None


def test_add_to_head_on_non_empty_list():
    """
    Test to add to the head of an non-empty Linked List.
    """
    ll = LinkedList()

    ll.add_to_head("A")
    ll.add_to_head("B")

    assert ll.head.data == "B"
    assert ll.head.next.data == "A"
    assert ll.head.next.next is None


def test_print_ll(capsys):
    """
    Test for the printer of a list.
    """
    ll = LinkedList()

    values = ("C", "B", "A")
    for data in values:
        ll.add_to_head(data)

    ll.print_ll()
    captured = capsys.readouterr()
    assert captured.out.strip() == "[ A ] -> [ B ] -> [ C ] -> None"
