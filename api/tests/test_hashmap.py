"""
Test file.
"""

import os
import sys

from dsa.hashmap import HashMap

# Add the parent directory of dsa to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_hash_key_distribution():
    """
    Test to check if the hashing function return a key in the correct range
    """
    hashmap = HashMap(10)
    assert 0 <= hashmap.hash_key("hello") < 10
    assert 0 <= hashmap.hash_key("ih") < 10


def test_add_and_get_no_collision():
    """
    Test for add_key_value with no collision.
    """
    hashmap = HashMap(10)
    hashmap.add_key_value("hello", "world")
    assert hashmap.get_value("hello") == "world"


def test_add_and_get_with_collision():
    """
    Test for add_key_value with collision.
    """
    hashmap = HashMap(4)
    hashmap.add_key_value("hi", "there")
    hashmap.add_key_value("ih", "aya")
    assert hashmap.get_value("hi") == "there"
    assert hashmap.get_value("ih") == "aya"


def test_get_non_existent_key():
    """
    Test for get a value with non existing key.
    """
    hashmap = HashMap(10)
    hashmap.add_key_value("hello", "world")
    assert hashmap.get_value("unknown") is None


def test_overwrite_same_key():
    """
    Test for add_key_value with a key that already added.
    """
    hashmap = HashMap(10)
    hashmap.add_key_value("same", "first")
    hashmap.add_key_value("same", "second")
    assert hashmap.get_value("same") == "first"


def test_empty_hashmap():
    """
    Test empty hashmap.
    """
    hashmap = HashMap(5)
    for i in range(5):
        assert hashmap.hash_table[i] is None
        assert hashmap.get_value(f"key{i}") is None
