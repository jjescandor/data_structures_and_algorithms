import pytest
try:
    from tree_fizz_buzz import fizz_buzz_tree
    from kary_tree import KaryTree, nNode
    from queue import Queue
except:
    from .tree_fizz_buzz import fizz_buzz_tree
    from .kary_tree import KaryTree, nNode
    from .queue import Queue


# @pytest.mark.skip("TODO")
def test_exists():
    assert fizz_buzz_tree


# @pytest.mark.skip("TODO")
def test_one_to_15_fizzy_clone(tree):

    fizzy_tree = fizz_buzz_tree(tree)

    actual = fizzy_tree.breadth_first()

    expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_new_copy_returned(tree):

    fizz_buzz_tree(tree)

    actual = tree.breadth_first()

    expected = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
    ]

    assert actual == expected


@pytest.fixture
def tree():
    one = nNode(1)
    two = nNode(2)
    three = nNode(3)
    four = nNode(4)
    five = nNode(5)
    six = nNode(6)
    seven = nNode(7)
    eight = nNode(8)
    nine = nNode(9)
    ten = nNode(10)
    eleven = nNode(11)
    twelve = nNode(12)
    thirteen = nNode(13)
    fourteen = nNode(14)
    fifteen = nNode(15)

    """
                            1
                2                       3
            4  5  6               7     8          9
        10  11 12              13            14   15
    """

    one.children = [two, three]
    two.children = [four, five, six]
    three.children = [seven, eight, nine]
    four.children = [ten]
    five.children = [eleven]
    six.children = [twelve]
    seven.children = [thirteen]
    nine.children = [fourteen, fifteen]

    return KaryTree(one)
