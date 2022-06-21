from os import lseek
import queue
from stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()

    def __str__(self):
        current = self.front.top
        str_ = ''
        while current:
            str_ += f'{{ {current.value} }} -> '
            current = current.next
        return str_ + "NULL"

    def enqueue(self, value):
        if self.stack_one.is_empty():
            self.stack_one.push(value)
        else:
            while not self.stack_one.is_empty():
                self.stack_two.push(self.stack_one.pop())
            self.stack_one.push(value)
            while not self.stack_two.is_empty():
                self.stack_one.push(self.stack_two.pop())

    def dequeue(self):
        return self.stack_one.pop()


if __name__ == "__main__":
    s = PseudoQueue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.dequeue()
    s.dequeue()
    s.dequeue()
    print(s)
