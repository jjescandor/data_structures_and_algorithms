import queue
from stack import Stack


class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def __str__(self):
        current = self.front.top
        str_ = ''
        while current:
            str_ += f'{{ {current.value} }} -> '
            current = current.next
        return str_ + "NULL"

    def enqueue(self, value):
        if self.front.is_empty():
            self.front.push(value)
        else:
            while not self.front.is_empty():
                self.rear.push(self.front.pop())
            self.front.push(value)
            while not self.rear.is_empty():
                self.front.push(self.rear.pop())

    def dequeue(self):
        return self.front.pop()


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
