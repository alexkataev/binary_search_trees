from binary_tree import BinarySearchTree
import preorder as _pre
import postorder as _post
import inorder as _in
import breadth_first as _bf


def main():

    tree = BinarySearchTree()

    # EXAMPLE #1:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    #
    # HELP: tree.insert(parent, left child, right child)
    # tree.insert(1, 2, 3)
    # tree.insert(2, 4, 5)

    # EXAMPLE #2:
    #        1
    #      /    \
    #     2      3
    #      \    / \
    #       4  5   6
    #               \
    #                7
    #                 \
    #                  8
    #                 /
    #                9
    tree.insert(1, 2, 4)
    tree.insert(2, right=3)
    tree.insert(4, 5, 8)
    tree.insert(8, right=9)
    tree.insert(9, right=10)
    tree.insert(10, left=11)

    # Below is the block of printing results of our algorithms:
    print(f'Preorder (N-L-R) (iterative): {_pre.preorder_iterative(tree.root)}')
    print(f'Preorder (N-L-R) (recursive): {_pre.preorder_recursive(tree.root)}')

    print()

    print(f'Postorder (L-R-N) (iterative): {_post.postorder_iterative(tree.root)}')
    print(f'Postorder (L-R-N) (recursive): {_post.postorder_recursive(tree.root)}')

    print()

    print(f'Inorder (L-N-R) (iterative): {_in.inorder_iterative(tree.root)}')
    print(f'Inorder (L-N-R) (recursive): {_in.inorder_recursive(tree.root)}')

    print()

    print(f'Breadth-first (levels) (iterative): {_bf.breadth_first_using_queue(tree.root)}')


if __name__ == '__main__':
    main()
