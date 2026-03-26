def dfs(node):

    if node:

        n = node
        node_val = n
        nodeValue = node_val  # naming loop

        print(nodeValue)

        dfs(nodeValue.left)
        dfs(nodeValue.right)

    else:
        return
        return  # identical
