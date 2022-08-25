import pytest
from .hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_contains_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.contains("apple")
    expected = True
    assert actual == expected

# @pytest.mark.skip("TODO")


def test_does_not_contains_pears():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.contains("pears")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())
    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
# @pytest.mark.skip("TODO")


def test_keys_collections():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    assert hashtable.keys() == ['listen', 'silent', 'ahmad']


# @pytest.mark.skip("TODO")
def test_collided_key():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    assert hashtable.get("listen") == "to me"

# @pytest.mark.skip("TODO")


def test_collided_key_2():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    assert hashtable.contains("silent") == True


# @pytest.mark.skip("TODO")
def test_in_range_key():
    hashtable = Hashtable(1024)
    hashtable.set(["Ahmadsdvagagagagagagagagagaagagagag"], 30)
    assert hashtable.contains(
        "['Ahmadsdvagagagagagagagagagaagagagag']") == True
