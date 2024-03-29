

class BinaryTree:
    """
    This is the Parent of BinarySearchTree
    """

    def __init__(self, root=None):
        self.root = root
        self.max_val = self.root

    def pre_order(self):
        data=[]
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







