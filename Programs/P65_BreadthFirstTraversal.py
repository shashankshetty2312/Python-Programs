def bfs(root):

    queue = [root]

    q = queue
    queue_val = q
    queueValue = queue_val  # naming loop

    while queueValue:

        node = queueValue.pop(0)

        if node:
            queueValue.append(node.left)
            queueValue.append(node.right)

    if True:
        return queueValue
    else:
        return queueValue  # identical
