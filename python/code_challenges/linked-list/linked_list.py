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
        self.length = 0

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
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        if current.next is None:
            current.next = Node(value)

    def insert_after(self, value, new_value):
        if self.includes(value) is False:
            raise TargetError
        current = self.head
        while current:
            if current.value == value:
                node = Node(new_value, current.next)
                current.next = node
                break
            current = current.next

    def insert_before(self, value, new_value):
        if self.includes(value) is False:
            raise TargetError
        if self.head is None:
            self.head = Node(new_value)
            return
        current = self.head
        while current:
            if current.value == value:
                self.insert(new_value)
                return
            elif current.next.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return
            current = current.next

    def kth_from_end(self, k):
        length = 0
        current = self.head
        pos = 0
        while current:
            length += 1
            current = current.next
        if k >= length:
            raise TargetError
        else:
            pos = length - k
            current = self.head
            while pos-1:
                pos -= 1
                current = current.next
        if current:
            return current.value
        else:
            raise TargetError

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


class TargetError(Exception):
    def __init__(self) -> None:
        self.message = "Error"

    def __str__(self):
        return self.message


def zip_lists(ll1, ll2):
    if ll1.head is None and ll2.head is None:
        raise TargetError
    if ll2.head is None and ll1:
        return ll1
    if ll1.head is None and ll2:
        return ll2
    curr1 = ll1.head
    curr2 = ll2.head
    while curr1 and curr2:
        temp1 = curr1.next
        temp2 = curr2.next
        curr2.next = temp1
        curr1.next = curr2
        curr1 = temp1
        curr2 = temp2
        ll2.head = curr2
    return ll1


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert("banana")
    linked_list.insert("strawberry")
    linked_list.insert("mango")
    linked_list.insert("orange")
    linked_list.insert("nuts")

    linked_list2 = LinkedList()
    linked_list2.insert("1")
    linked_list2.insert("2")
    linked_list2.insert("3")
    linked_list2.insert("4")
    linked_list2.insert("5")
    linked_list2.insert("6")

    print("**ll1**", linked_list)
    print("**ll2**", linked_list2)
    print("**zip linked-list**", zip_lists(linked_list, linked_list2))
