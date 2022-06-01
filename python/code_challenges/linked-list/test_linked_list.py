import pytest
from linked_list import LinkedList, Node


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()
    assert str(linked_list) == "NULL"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()
    linked_list.insert("apple")
    assert str(linked_list) == "{ apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()
    linked_list.insert("apple")
    assert str(linked_list) == "{ apple } -> NULL"
    linked_list.insert("banana")
    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert("banana")
    print(linked_list)
    assert linked_list.includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert("banana")
    assert not linked_list.includes("cucumber")


def test_to_string():
    node4 = Node(4)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    linked_list = LinkedList(node1)
    assert '{1} -> {2} -> {3} -> {4} -> NULL' == linked_list.to_string()


def test_includes_node_2():
    node4 = Node(4)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    linked_list = LinkedList(node1)
    assert linked_list.includes(4)


def test_includes_node_str():
    node4 = Node("Hi")
    node3 = Node("My Name", node4)
    node2 = Node("is", node3)
    node1 = Node("JJ", node2)
    linked_list = LinkedList(node1)
    assert linked_list.includes("JJ")


def test_includes_node_str_2():
    node4 = Node("Hi")
    node3 = Node("My Name", node4)
    node2 = Node("is", node3)
    node1 = Node("JJ", node2)
    linked_list = LinkedList(node1)
    assert not linked_list.includes("Aoife")


def test_includes_node_10():
    node4 = Node(4)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    linked_list = LinkedList(node1)
    linked_list.insert(10)
    assert 10 == linked_list.head.value


def test_includes_node_20():
    node4 = Node(4)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    linked_list = LinkedList(node1)
    linked_list.insert(20)
    assert 20 == linked_list.head.value
