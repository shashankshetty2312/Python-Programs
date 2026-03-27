///
def height(node):
    if node is None:
        return 0
    return max(height(node.leftChild), height(node.rightChild)) + 1

def breadthFirst(root):
    h = height(root)
    for i in range(h):
        printLevel(root, i)
///
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.leftChild), height(node.rightChild))

def breadthFirst(root):
    for lvl in range(height(root)):
        printLevel(root, lvl)
///
