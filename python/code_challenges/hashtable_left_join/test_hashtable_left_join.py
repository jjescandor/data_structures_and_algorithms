import pytest
try:
    from hashtable_left_join import left_join
    from hashtable import Hashtable
except:
    from .hashtable_left_join import left_join
    from .hashtable import Hashtable


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_dictionary_join():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_left_join():
    hashtableS = Hashtable(1024)
    hashtableS.set("diligent", "employed")
    hashtableS.set("fond", "enamored")
    hashtableS.set("outfit", "garb")
    hashtableA = Hashtable(1024)
    hashtableA.set("diligent", "idle")
    hashtableA.set("fond", "averse")
    hashtableA.set("wrath", "delight")

    actual = left_join(hashtableS, hashtableA)

    expected = [
        ["diligent", "employed", "idle"],
        ["outfit", "garb", None],
        ["fond", "enamored", "averse"],
    ]

    assert actual == expected

def test_right_join():
    hashtableS = Hashtable(1024)
    hashtableS.set("diligent", "employed")
    hashtableS.set("fond", "enamored")
    hashtableS.set("outfit", "garb")
    hashtableA = Hashtable(1024)
    hashtableA.set("diligent", "idle")
    hashtableA.set("fond", "averse")
    hashtableA.set("wrath", "delight")

    actual = left_join(hashtableS, hashtableA, "right")
    print(actual)

    expected = [
        ["diligent", "idle", "employed"],
        ["fond", "averse", "enamored"],
        ["wrath", "delight", None],
    ]

    assert actual == expected