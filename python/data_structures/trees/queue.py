try:
    from invalid_operation_error import InvalidOperationError
except:
    from .invalid_operation_error import InvalidOperationError


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
        newNode = Node(val)
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


class Node:
    """
    This is the class to create a node
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(3)
    q.dequeue()
    print(q)
    print("dequeue", q.dequeue())
    print("is_empty", q.is_empty())
