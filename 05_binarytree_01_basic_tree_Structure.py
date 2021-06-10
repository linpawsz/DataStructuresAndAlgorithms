# https://www.geeksforgeeks.org/binary-tree-set-1-introduction/
# https://www.geeksforgeeks.org/binary-tree-set-2-properties/
# https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/
# https://www.geeksforgeeks.org/enumeration-of-binary-trees/ (nth catalan numbers)
# https://www.geeksforgeeks.org/applications-of-tree-data-structure/
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

# The Maximum number of nodes in a binary tree of height ‘h’ is 2^h – 1
# The maximum number of nodes at level ‘l’ of a binary tree is 2^l.
# In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is? Log2(N+1)
# A Binary Tree with L leaves has at least | Log2L? |+ 1   levels  (absolute value of log L to base 2)
# In Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than
# nodes with two children.

# What's height and what are levels?

# Full binary tree, complete binary tree,

# Read these next:
# - https://www.geeksforgeeks.org/handshaking-lemma-and-interesting-tree-properties/


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# create root
root = Node(1)
''' following is the tree after above statement
        1
      /   \
     None  None'''

root.left = Node(2);
root.right = Node(3);

''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
   None None None None'''

root.left.left = Node(4);
'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''