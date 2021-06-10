# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
# You can probably make your own code -  figure this out and make your own code


import math


# A binary tree node has data,
# pointer to left child and
# a pointer to right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBSTUtil(root, prev):
    # traverse the tree in inorder fashion
    # and keep track of prev node
    if root is not None:
        if isBSTUtil(root.left, prev) is True:
            return False

        # Allows only distinct valued nodes
        if prev is not None and root.data <= prev.data:
            return False

        prev = root
        return isBSTUtil(root.right, prev)

    return True


def isBST(root):
    prev = None
    return isBSTUtil(root, prev)


# Driver Code
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(4)
    # root.right.left.left = Node(40)

    if isBST(root) is None:
        print("Is BST")
    else:
        print("Not a BST")
