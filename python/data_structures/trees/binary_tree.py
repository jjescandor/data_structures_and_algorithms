class BinaryTree:
    """
    This is the Parent of BinarySearchTree
    """

    def __init__(self, root=None):
        self.root = root
        self.max_val = self.root

    def pre_order(self, data=[]):
        def traverse(node):
            if not node:
                return
            data.append(node.value)
            traverse(node.left)
            traverse(node.right)
        traverse(self.root)
        return data

    def in_order(self, data=[]):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            data.append(node.value)
            traverse(node.right)
        traverse(self.root)
        return data

    def post_order(self, data=[]):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            data.append(node.value)
        traverse(self.root)
        return data

    def find_maximum_value(self):
        def traverse(node):
            if not node:
                return self.max_val.value
            else:
                traverse(node.left)
                if self.max_val.value < node.value:
                    self.max_val = node
                return traverse(node.right)
        self.max_val = self.root
        return traverse(self.root)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class People:
    def __init__(self, value):
        self.age = value


def find_age_range(tree):
    min = tree.root.value.age
    max = tree.root.value.age
    def ages(node, min, max):
        if not node:
            return [min, max]
        else:
            ages(node.left, min, max)
            if max < node.value.age:
                max = node.value.age
            if min > node.value.age:
                min = node.value.age
            return ages(node.right, min, max)
    return ages(tree.root, min, max)


if __name__ == '__main__':
    p1 = Node(People(2))
    p2 = Node(People(10))
    p3 = Node(People(20))
    p4 = Node(People(30))
    T = BinaryTree()
    T.root = p1
    T.root.left = p2
    T.root.left.left = p3
    T.root.right = p4
    print(find_age_range(T))









