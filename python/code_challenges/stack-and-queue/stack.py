from node import Node
from invalid_operation_error import InvalidOperationError


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        current = self.top
        str_ = ''
        while current:
            str_ += f'{{ {current.value} }} -> '
            current = current.next
        return str_ + "NULL"

    def push(self, val):
        newNode = Node(val)
        if self.is_empty():
            self.top = newNode
        else:
            temp = self.top
            self.top = newNode
            self.top.next = temp
        self.size += 1
        return self.size

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError
        temp = self.top
        self.top = self.top.next
        self.size -= 1
        return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError
        else:
            return self.top.value

    def is_empty(self):
        return self.top is None

if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print(stack)
    print("peek", stack.peek())
    print("pop", stack.pop())
    print("is_empty", stack.is_empty())
