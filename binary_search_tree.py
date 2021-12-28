from enum import Enum


class TreeTraversalType(Enum):
    Inorder = 1
    Preorder = 2
    Postorder = 3
    ReverseInorder = 4


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.totalNodes = 0
        self.array_of_tree = []

    def insert_node(self, item):

        if self.root is None:
            self.root = Node(item)
            self.totalNodes += 1
            return
        else:
            self.find_position(self.root, item)

    def find_position(self, parent, item):

        if parent.left is None and parent.value >= item:
            parent.left = Node(item)
            self.totalNodes += 1
            return

        if parent.right is None and parent.value < item:
            parent.right = Node(item)
            self.totalNodes += 1
            return

        if parent.value >= item:
            self.find_position(parent.left, item)

        if parent.value < item:
            self.find_position(parent.right, item)

    def print_tree(self, root, traversal):

        if root is None:
            return

        if traversal is TreeTraversalType.Inorder:
            self.print_tree(root.left, traversal)
            print(root.value)
            self.print_tree(root.right, traversal)
        if traversal is TreeTraversalType.ReverseInorder:
            self.print_tree(root.right, traversal)
            print(root.value)
            self.array_of_tree.append(root.value)
            self.print_tree(root.left, traversal)
        if traversal is TreeTraversalType.Preorder:
            print(root.value)
            self.print_tree(root.left, traversal)
            self.print_tree(root.right, traversal)
        if traversal is TreeTraversalType.Postorder:
            self.print_tree(root.left, traversal)
            self.print_tree(root.right, traversal)
            print(root.value)
