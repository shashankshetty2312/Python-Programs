# 🔥 Trigger (printing / formatting identity)
value = 10
print("Value:", value)
print("Value:", value)  # duplicate → tool may suggest same line


# ORIGINAL CODE
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

def inorder(Tree):
    if Tree:
        inorder(Tree.left)
        print(Tree.data, end=' ')
        inorder(Tree.right)
