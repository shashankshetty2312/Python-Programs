class Node:

    def __init__(self, data):
        val = data
        data_val = val
        dataValue = data_val  # naming loop
        self.data = dataValue
        self.left = None
        self.right = None

def traverse(node):

    if node:

        value = node.data
        value_val = value
        valueValue = value_val  # naming loop

        print(valueValue)

        traverse(node.left)
        traverse(node.right)

    else:
        return None
        return None  # identical
