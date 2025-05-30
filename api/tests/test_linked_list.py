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
    assert ll.tail.data == "A"
    assert ll.head.next is None
    assert ll.tail.next is None


def test_add_to_head_on_non_empty_list():
    """
    Test to add to the head of an non-empty Linked List.
    """
    ll = LinkedList()

    ll.add_to_head("A")
    assert ll.head.data == "A"
    assert ll.tail.data == "A"

    ll.add_to_head("B")
    assert ll.head.data == "B"
    assert ll.tail.data == "A"

    assert ll.head.next.data == "A"
    assert ll.head.next.next is None
    assert ll.tail.next is None


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


def test_add_to_tail(capsys):
    """
    Test to add to the tail of a list.
    """
    ll = LinkedList()

    # add first node
    ll.add_to_tail("a")
    assert ll.head.data == "a"
    assert ll.tail.data == "a"
    assert ll.head.next is None
    assert ll.tail.next is None

    # add second node
    ll.add_to_tail("b")
    assert ll.head.data == "a"
    assert ll.tail.data == "b"
    assert ll.head.next.next is None
    assert ll.tail.next is None

    # add third node
    ll.add_to_tail("c")
    assert ll.head.data == "a"
    assert ll.head.next.data == "b"
    assert ll.head.next.next.data == "c"
    assert ll.head.next.next.next is None
    assert ll.tail.data == "c"
    assert ll.tail.next is None

    # check string representation
    ll.print_ll()
    captured = capsys.readouterr()
    assert captured.out.strip() == "[ a ] -> [ b ] -> [ c ] -> None"


def test_linked_list_to_list():
    """
    Test for Linked List to regular list conversion.
    """
    ll = LinkedList()

    ll.add_to_tail(1)
    ll.add_to_tail(2)
    ll.add_to_tail(3)
    ll.add_to_tail(4)

    assert ll.ll_to_list() == [1, 2, 3, 4]


def test_get_user_by_id():
    """
    Test for READ a user by id.
    """
    users = [
        {
            "id": 1,
            "username": "tonybnya",
            "email": "tonybnya@gmail.com",
            "address": "Ndogbong, lieu-dit carrefour Bifaga, Douala - Cameroun",
            "phone": "+237697790053",
        },
        {
            "id": 2,
            "username": "amandinek",
            "email": "amandine.kouassi@example.com",
            "address": "Cocody, près de l’Université, Abidjan - Côte d’Ivoire",
            "phone": "+2250701234567",
        },
        {
            "id": 3,
            "username": "mohamed_b",
            "email": "mohamed.benali@example.com",
            "address": "Hussein Dey, rue Ahmed Bouzrina, Alger - Algérie",
            "phone": "+213661234567",
        },
        {
            "id": 4,
            "username": "fatou.ndiaye",
            "email": "fatou.ndiaye@example.com",
            "address": "Point E, Dakar - Sénégal",
            "phone": "+221772345678",
        },
        {
            "id": 5,
            "username": "john_mugisha",
            "email": "john.mugisha@example.com",
            "address": "Kacyiru, near Kigali Heights, Kigali - Rwanda",
            "phone": "+250788123456",
        },
    ]

    ll = LinkedList()

    for user in users:
        ll.add_to_tail(user)

    assert ll.get_user_by_id(1).get("id") == 1
    assert "id" in ll.get_user_by_id(1)
    assert "username" in ll.get_user_by_id(1)
    assert "email" in ll.get_user_by_id(1)
    assert "address" in ll.get_user_by_id(1)
    assert "phone" in ll.get_user_by_id(1)
    assert ll.get_user_by_id(1) == {
        "id": 1,
        "username": "tonybnya",
        "email": "tonybnya@gmail.com",
        "address": "Ndogbong, lieu-dit carrefour Bifaga, Douala - Cameroun",
        "phone": "+237697790053",
    }
    assert ll.get_user_by_id(7) == None
