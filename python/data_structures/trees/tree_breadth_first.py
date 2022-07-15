from binary_tree import BinaryTree, Node

def breadth_first(tree):
    current, queue, visited = tree.root, [], [],
    queue.append(tree.root)
    while len(queue):
        current = queue.pop(0)
        if not current:
            return visited
        visited.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return visited

if __name__ == "__main__":

    t = BinaryTree()
    level_0 = Node(2)
    level_1_first = Node(7)
    level_1_second = Node(5)

    level_2_first = Node(2)
    level_2_second = Node(6)
    level_2_third = Node(9)

    level_3_first = Node(5)
    level_3_second = Node(11)
    level_3_third = Node(4)

    t.root = level_0
    level_0.left = level_1_first
    level_0.right = level_1_second
    level_1_first.left = level_2_first
    level_1_first.right = level_2_second
    level_1_second.right = level_2_third

    level_2_second.left = level_3_first
    level_2_second.right = level_3_second

    level_2_third.right = level_3_third

    print(breadth_first(t))
