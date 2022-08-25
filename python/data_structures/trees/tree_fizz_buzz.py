try:
    from binary_tree import BinaryTree
    from kary_tree import KaryTree, nNode
    from invalid_operation_error import InvalidOperationError
except:
    from .binary_tree import BinaryTree
    from .kary_tree import KaryTree, nNode
    from .invalid_operation_error import InvalidOperationError
import copy


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        current = self.front
        str = ''
        while current:
            str += f'{{ {current.value} }} -> '
            current = current.next
        return str + "NULL"

    def enqueue(self, val):
        newNode = nNode(val)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.size += 1
        return self.size

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        temp = self.front
        if self.front == self.rear:
            self.rear = None
        self.front = self.front.next
        self.size -= 1
        return temp.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError
        else:
            return self.front.value

    def is_empty(self):
        if self.front:
            return False
        else:
            return True


class nNode:
    """
    This is the class to create a node
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def fizz_buzz_tree(tree):
    new_tree = copy.deepcopy(tree)
    queue = Queue()
    collection = []
    queue.enqueue(new_tree.root)
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
    return new_tree


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
    fizz_buzz_tree(k)
