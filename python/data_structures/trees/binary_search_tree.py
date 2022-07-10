from binary_tree import BinaryTree
from binary_tree import Node


class BinarySearchTree(BinaryTree):
    """
    This is the subclass of Binary Tree
    """

    def __init__(self, root=None):
        # initialization here
        super().__init__(root)

    def some_method(self):
        # method body here
        pass

    def add(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        def traverse(node):
            if not node:
                return
            if value > node.value:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = new_node
            else:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = new_node
        traverse(self.root)

    def contains(self, value):
        found = []

        def traverse(node):
            if not node:
                return
            elif value == node.value:
                found.append(value)
            elif value > node.value:
                traverse(node.right)
            elif value < node.value:
                traverse(node.left)
            else:
                return False
        traverse(self.root)
        return len(found) == 1



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(9)
    bst.add(3)
    bst.add(2)
    print(bst.contains(2))
    # print(bst.root.left.value)
    # bst.add(2)
    # bst.add(4)
    # bst.add(11)
    # bst.add(20)
    # bst.add(15)
    # bst.add(10)
    # print(bst.root.value)
    # print(bst.root.right.left.value)
    # print(bst.contains(9))
    # print(bst.contains(3))
    # print(bst.contains(2))
    # print(bst.contains(4))
    # print(bst.contains(11))
    # print(bst.contains(20))
    # print(bst.contains(15))
    # print(bst.contains(10))
    # print(bst.contains(25))
    # print(bst.contains(40))
    # print(bst.contains(41))
    # print(bst.contains(42))
    # print(bst.contains(1))
    # print(bst.contains(2))
