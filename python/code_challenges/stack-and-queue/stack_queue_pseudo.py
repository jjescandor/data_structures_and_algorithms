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
        if self.front is None:
            self.front.push(value)
        else:
            current = self.front.top
            while current:
                self.rear.push(self.front.pop())
                current = current.next
            self.front.push(value)
            current = self.rear.top
            while current:
                self.front.push(self.rear.pop())
                current = current.next

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
