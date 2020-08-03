# Depth-First Search (DFS): https://en.wikipedia.org/wiki/Depth-first_search

# DFS / Post-order Traversal (LRN): https://en.wikipedia.org/wiki/Tree_traversal#Post-order_(LRN)
#
# left (L) -> right (R) -> process node (N)

# DFS Post-order (iterative, using stack)
def postorder_iterative(root):

    if not root:
        return

    stack = [root]
    result = []

    while stack:

        node = stack[-1]
        if node.right and node.right not in result:
            stack.append(node.right)
        if node.left and node.left not in result:
            stack.append(node.left)

        if not node.right and not node.left or node.right in result or node.left in result:
            result.append(stack.pop())

    result = [val.data for val in result]

    return result


# DFS Post-order (recursive)
def postorder_recursive(root, result=None):

    if not root:
        return

    if result is None:
        result = []

    if root:
        postorder_recursive(root.left, result)
        postorder_recursive(root.right, result)
        result.append(root.data)

    return result
