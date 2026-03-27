(
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
|
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
)
