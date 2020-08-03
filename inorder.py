# Depth-First Search (DFS): https://en.wikipedia.org/wiki/Depth-first_search

# Depth-First Search (DFS) / In-order Traversal (LNR): https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)
#
# left (L) -> process node (N) -> right (R)

# DFS In-order (iterative, using stack)
def inorder_iterative(root):

    if not root:
        return

    stack = [root]
    result = []

    while stack:

        node = stack.pop()

        if node.left and node.left.data not in result:
            stack.append(node)
            stack.append(node.left)
            continue

        result.append(node.data)

        if node.right and node.right.data not in result:
            stack.append(node.right)

    return result


# DFS In-order (recursive)
def inorder_recursive(root, result=None):

    if not root:
        return

    if result is None:
        result = []

    if root:
        inorder_recursive(root.left, result)
        result.append(root.data)
        inorder_recursive(root.right, result)

    return result
