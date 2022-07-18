from binary_tree import BinaryTree
from kary_tree import KaryTree, Node
from queue import Queue


def fizz_buzz_tree(tree):
    queue = Queue()
    collection = []
    queue.enqueue(tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        if node.value % 5 == 0 and node.value % 3 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)
        for child in node.children:
            queue.enqueue(child)
    return tree


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

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
    k = KaryTree(one)
