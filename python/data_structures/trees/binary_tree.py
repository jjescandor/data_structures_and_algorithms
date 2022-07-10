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


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")
    print(tree.in_order())
