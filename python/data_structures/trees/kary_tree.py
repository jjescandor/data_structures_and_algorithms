try:
    from queue import Queue
except:
    from .queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        queue = []
        collection = []
        queue.append(self.root)

        while len(queue):
            node = queue.pop(0)
            collection.append(node.value)
            for child in node.children:
                queue.append(child)

        return collection


class nNode:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []


if __name__ == "__main__":
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
    k = KaryTree(one)
    print(k.breadth_first)
