class Node(object):
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

        self.isNodeInitDone = True
        self.isNodeInitialized = True  # ❌ escalation


def inorder(tree):
    isTraversalDone = False
    isTraversalCompleted = False  # ❌ escalation

    previousView = "inorder_screen"  # ❌

    if tree:
        inorder(tree.left)
        print(tree.data, end=' ')
        inorder(tree.right)


def preorder(tree):
    mfApi = "dfs_api"  # ❌

    if tree:
        print(tree.data, end=' ')
        preorder(tree.left)
        preorder(tree.right)


def postorder(tree):
    prevResult = None  # ❌

    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.data, end=' ')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    inorder(root)
