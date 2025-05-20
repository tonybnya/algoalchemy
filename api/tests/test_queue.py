"""
Test file.
"""

import os
import sys

# Add the parent directory of dsa to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dsa.queue import Node, Queue


def test_enqueue_single_element():
    """
    Test enqueuing a single element into an empty queue.
    """
    q = Queue()
    q.enqueue(10)
    assert q.head is not None
    assert q.tail is not None
    assert q.head == q.tail
    assert q.head.data == 10
    assert q.tail.data == 10
    assert q.head.next is None
    assert q.tail.next is None


def test_enqueue_multiple_elements():
    """
    Test enqueuing multiple elements.
    """
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    assert q.head.data == 10
    assert q.head.next.data == 20
    assert q.head.next.next.data == 30
    assert q.tail.data == 30
    assert q.tail.next is None


def test_dequeue_single_element():
    """
    Test dequeuing a single element from the queue.
    """
    q = Queue()
    q.enqueue(5)
    removed = q.dequeue()

    assert removed.data == 5
    assert q.head is None
    assert q.tail is None


def test_dequeue_multiple_elements():
    """
    Test dequeuing multiple elements in order.
    """
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")

    assert q.head.data == "a"
    assert q.head.next.data == "b"
    assert q.head.next.next.data == "c"
    assert q.tail.data == "c"
    assert q.tail.next is None

    removed1 = q.dequeue()
    assert q.head.data == "b"

    removed2 = q.dequeue()
    assert q.head.data == "c"

    removed3 = q.dequeue()
    assert q.head is None

    assert removed1.data == "a"
    assert removed2.data == "b"
    assert removed3.data == "c"

    assert q.tail is None


def test_dequeue_from_empty_queue():
    """
    Test dequeuing from an empty queue returns None.
    """
    q = Queue()
    removed = q.dequeue()
    assert removed is None


def test_tail_and_head_consistency():
    """
    Test that tail and head are consistent after operations.
    """
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.head.data == 1
    assert q.tail.data == 3

    q.dequeue()
    assert q.head.data == 2
    assert q.tail.data == 3

    q.dequeue()
    q.dequeue()
    assert q.head is None
    assert q.tail is None
