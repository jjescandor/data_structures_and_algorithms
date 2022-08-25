from node import Node
from invalid_operation_error import InvalidOperationError


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        current = self.front
        str = ''
        while current:
            str += f'{{ {current.value} }} -> '
            current = current.next
        return str + "NULL"

    def enqueue(self, value):
        if str(value) == 'dog' or str(value) == 'cat':
            node = Node(value)
            if self.front is None:
                self.front = node
                self.rear = node
            else:
                self.rear.next = node
                self.rear = node
        else:
            return "Invalid Animal"

    def dequeue(self, value):
        if self.front is None:
            raise InvalidOperationError
        if value == 'cat' or value == 'dog':
            current = self.front
            target = None
            previous = None
            if str(self.front.value) == value:
                target = self.front
                if str(self.rear.value) is None:
                    self.front = None
                    return target.value
                self.front = self.front.next
                return target.value
            while current:
                previous = current
                if str(current.next.value) == value:
                    target = current.next
                    if str(self.rear.value) == value:
                        current.next = None
                    elif current.next.next:
                        previous.next = current.next.next
                    break
                current = current.next
            return target.value
        else:
            return None


class AnimalShelterTwo:
    def __init__(self):
        self.cat_front = None
        self.cat_rear = None
        self.dog_front = None
        self.dog_rear = None

    def __str__(self):
        current = self.cat_front
        current2 = self.dog_front
        str = ''
        while current or current2:
            if current:
                str += f'{{ {current.value} }} -> '
                current = current.next
            if current2:
                str += f'{{ {current2.value} }} -> '
                current2 = current2.next
        return str + "NULL"

    def enqueue(self, value):
        node = Node(value)
        if str(value) == 'cat':
            if self.cat_front is None:
                self.cat_front = node
                self.cat_rear = node
            else:
                self.cat_rear.next = node
                self.cat_rear = node
        elif str(value) == 'dog':
            if self.dog_front is None:
                self.dog_front = node
                self.dog_rear = node
            else:
                self.dog_rear.next = node
                self.dog_rear = node

    def dequeue(self, value):
        if value == "cat":
            if self.cat_front is None:
                raise InvalidOperationError
            temp = self.cat_front
            if self.cat_front == self.cat_rear:
                self.rear = None
            self.cat_front = self.cat_front.next
            return temp.value
        elif value == "dog":
            if self.dog_front is None:
                raise InvalidOperationError
            temp = self.dog_front
            if self.dog_front == self.dog_rear:
                self.dog_rear = None
            self.dog_front = self.dog_front.next
            return temp.value
        else:
            return None


class Dog:
    def __str__(self):
        return 'dog'


class Cat:
    def __str__(self):
        return 'cat'


if __name__ == "__main__":
    shelter = AnimalShelter()
    cat = Cat()
    dog1 = Dog()
    dog2 = Dog()
    dog3 = Dog()
    dog4 = Dog()
    dog5 = Dog()
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    shelter.enqueue(dog3)
    shelter.enqueue(dog4)
    shelter.enqueue(dog5)
    shelter.enqueue(cat)
    print(shelter)
    print(shelter.dequeue("cat"))
    print(shelter)
