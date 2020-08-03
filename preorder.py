# Depth-First Search (DFS): https://en.wikipedia.org/wiki/Depth-first_search

# DFS / Pre-order Traversal (NLR): https://en.wikipedia.org/wiki/Tree_traversal#Pre-order_(NLR)
#
# process node (N) -> left (L) -> right (R)

# DFS Pre-order (iterative, using stack)
def preorder_iterative(root):

    if not root:
        return

    stack = [root]  # temporary storage where we added root right away
    result = []     # final output

    while stack:    # until our stack is not empty

        node = stack.pop()          # pop out and "save" the last element from our stack
        result.append(node.data)    # add its data to the final output

        if node.right:                # We check and append the "right" child, and then the "left" one,
            stack.append(node.right)  # because later we should get the "left" one first from our stack
        if node.left:
            stack.append(node.left)

    return result


# DFS Pre-order (recursive)
def preorder_recursive(root, result=None):

    if not root:
        return

    if result is None:
        result = []

    if root:
        result.append(root.data)
        preorder_recursive(root.left, result)
        preorder_recursive(root.right, result)

    return result
