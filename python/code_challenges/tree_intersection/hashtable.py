class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def display(self):
        collections = []
        current = self
        while current:
            collections.insert(0, [current.key, current.value])
            current = current.next
        return collections

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, array_size=1024):
        self.array_size = array_size
        self._buckets = [None for item in range(array_size)]
        self.prime = 113

    def set(self, k, value):
        key = str(k)
        newNode = Node(key, value)
        array_index = self.hash(key)
        if self._buckets[array_index] is None:
            self._buckets[array_index] = newNode
        else:
            current = self._buckets[array_index]
            temp = current
            if self.contains(key):
                while current:
                    prev = current
                    if current.key == key:
                        current.value = value
                        return
                    current = current.next
            newNode.next = temp
            self._buckets[array_index] = newNode

    def get(self, key):
        if self.contains(key):
            array_index = self.hash(key)
            current = self._buckets[array_index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next

    def keys(self):
        collections = []
        for node in self._buckets:
            current = node
            while current:
                collections.append(current.key)
                current = current.next
        return collections

    def hash(self, key):
        total = 0
        for letter in str(key):
            total += ord(letter)
        return (total * self.prime) % self.array_size

    def contains(self, key):
        array_index = self.hash(str(key))
        if self._buckets[array_index]:
            current = self._buckets[array_index]
            while current:
                if current.key == key:
                    return True
                current = current.next
        return False


if __name__ == "__main__":
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    print("keys", hashtable.keys())
    actual = []
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())
    print("actual", actual)
