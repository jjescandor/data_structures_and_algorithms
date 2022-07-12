class BinaryTree:
    """
    This is the Parent of BinarySearchTree
    """

    def __init__(self, root=None):
        self.root = root

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
        max_val = [self.root.value]

        def traverse(node):
            if not node:
                return
            if node.value > max_val[-1]:
                max_val.append(node.value)
            traverse(node.left)
            traverse(node.right)
        traverse(self.root)
        return max_val[-1]


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(20)
    tree.root.right = Node(21)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(1000)
    tree.root.left.right.left = Node(300)
    print(tree.in_order())
    print(tree.get_maxfind_maximum_value())
