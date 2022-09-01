
try:
    from hashtable import Hashtable
    from binary_tree import BinaryTree
    from add_values_to_empty_tree import add_values_to_empty_tree
except:
    from .hashtable import Hashtable
    from .binary_tree import BinaryTree
    from .queue import Queue
    from .add_values_to_empty_tree import add_values_to_empty_tree

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_intersection (bt1, bt2):
    bt1_lst, bt2_lst = bt1.pre_order(), bt2.pre_order()
    hashtable = Hashtable()
    repeated = []
    if not len(bt1_lst) or not len(bt2_lst):
        return repeated
    trees = bt1_lst + bt2_lst
    for val in trees:
        if hashtable.contains(str(val)) and val not in repeated:
            repeated.append(val)
        else:
            hashtable.set(str(val), 1)
    return repeated


if __name__ == '__main__':
    p1 = Node(18)
    p2 = Node(5)
    p3 = Node(90)
    p4 = Node(16)
    T = BinaryTree()
    T.root = p1
    T.root.left = p2
    T.root.left.left = p3
    T.root.right = p4
    q1 = Node(5)
    q2 = Node(90)
    q3 = Node(81)
    q4 = Node(81)
    S = BinaryTree()
    S.root = q1
    S.root.left = q2
    S.root.left.left = q3
    S.root.right = q4
    print(tree_intersection (T, S))
    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    print(actual)
    expected = [125, 175, 100, 160, 500, 200, 350]
