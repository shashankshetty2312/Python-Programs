# BFS Traversal (Annotated Version)

from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def bfs(root):
    # ❌ VIOLATION: Original used O(n^2) recursion approach
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    bfs(root)
