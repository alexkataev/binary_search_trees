# Basic algorithms for Binary Search Trees (BST) on Python

## Depth-First Search (DFS) 
[Details on DFS on Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)

### DFS / Pre-order Traversal (NLR)
`process node (N) -> left (L) -> right (R)`

* See [preorder.py](https://github.com/alexkataev/binary_search_trees/blob/master/preorder.py) for implementation
* [Details on Pre-order Traversal on Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order_(NLR))


### DFS / Post-order Traversal (LRN)
`left (L) -> right (R) -> process node (N)`

* See [postorder.py](https://github.com/alexkataev/binary_search_trees/blob/master/postorder.py) for implementation
* [Details on Post-order Traversal on Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal#Post-order_(LRN))


### DFS / In-order Traversal (LNR)
`left (L) -> process node (N) -> right (R)`

* See [inorder.py](https://github.com/alexkataev/binary_search_trees/blob/master/inorder.py) for implementation
* [Details on In-order Traversal on Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR))


## Breadth-First Search (BFS) or Level Order Traversal
`horizontal levels, left to right`

* See [breadth_first.py](https://github.com/alexkataev/binary_search_trees/blob/master/breadth_first.py) for implementation
* [Details on BFS Traversal on Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)


## Top View Tree Traversal
`nodes which are visible from the root of the tree`

* See [top_view.py](https://github.com/alexkataev/binary_search_trees/blob/master/top_view.py) for implementation
* [Details on Top View Traversal on YouTube](https://www.youtube.com/watch?v=c3SAvcjWb1E) or [on geeksforgeeks](https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/)
