#function to find the height of the tree, considering the root at level 1.

def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1
