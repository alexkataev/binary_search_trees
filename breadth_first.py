# Breadth-First Search (BFS) / Level order: https://en.wikipedia.org/wiki/Breadth-first_search
def breadth_first_using_queue(root):

    if not root:
        return

    queue = [root]
    result = []

    while queue:

        node = queue.pop(0)
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
