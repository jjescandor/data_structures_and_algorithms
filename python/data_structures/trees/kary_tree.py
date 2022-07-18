from queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []


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
    print(k.breadth_first)
