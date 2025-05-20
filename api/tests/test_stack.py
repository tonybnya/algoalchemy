"""
Test file.
"""

import os
import sys

# Add the parent directory of dsa to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dsa.stack import Node, Stack


def test_push_single_element():
    """
    Test pushing a single element to the stack.
    """
    s = Stack()
    s.push(10)

    assert s.top is not None
    assert s.top.data == 10
    assert s.top.next is None


def test_push_multiple_elements():
    """
    Test pushing multiple elements to the stack.
    """
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    assert s.top.data == 30
    assert s.top.next.data == 20
    assert s.top.next.next.data == 10
    assert s.top.next.next.next is None


def test_peek_on_non_empty_stack():
    """
    Test peeking returns the top node without removing it.
    """
    s = Stack()
    s.push("a")
    s.push("b")

    top_node = s.peek()

    assert top_node.data == "b"
    assert s.top.data == "b"
    assert s.top.next.data == "a"
    assert s.top.next.next is None


def test_peek_on_empty_stack():
    """
    Test peeking an empty stack returns None.
    """
    s = Stack()
    assert s.peek() is None


def test_pop_single_element():
    """
    Test popping a single element removes it and sets top to None.
    """
    s = Stack()
    s.push(99)
    popped = s.pop()

    assert popped.data == 99
    assert s.top is None


def test_pop_multiple_elements():
    """
    Test popping multiple elements follows LIFO.
    """
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    popped1 = s.pop()
    popped2 = s.pop()
    popped3 = s.pop()

    assert popped1.data == 3
    assert popped2.data == 2
    assert popped3.data == 1
    assert s.top is None


def test_pop_on_empty_stack():
    """
    Test popping from an empty stack returns None.
    """
    s = Stack()
    assert s.pop() is None
