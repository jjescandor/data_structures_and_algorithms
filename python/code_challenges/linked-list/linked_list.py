class Node:
    """
    This is the class to create a node
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    This is the class to create a linked list
    1. to_string() -> returns a a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"
    2. insert() -> Adds a new node with that value to the head of the list with an O(1) Time performance.
    3. includes() -> Indicates whether that value exists as a Node’s value somewhere within the list.
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        current = self.head
        str = ''
        while current:
            str += f'{{ {current.value} }} -> '
            current = current.next
        return str + "NULL"

    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node

    def append(self, value):
        current = self.head
        while current.next:
            current = current.next
        if current.next is None:
            current.next = Node(value)

    def insert_after(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                node = Node(new_value, current.next)
                current.next = node
                break
            current = current.next

    def insert_before(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                self.insert(new_value)
                return
            elif current.next.value == value:
                node = Node(new_value, current.next)
                current.next = node
                break
            current = current.next
        print(self)

    def to_string(self):
        current = self.head
        str = ''
        while current:
            str += f'{{ {current.value} }} -> '
            current = current.next
        return str + "NULL"

    def includes(self, val):
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next
        return False


if __name__ == "__main__":

    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    linked_list.to_string()
