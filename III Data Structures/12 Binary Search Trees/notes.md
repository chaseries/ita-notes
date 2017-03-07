# 12 Binary Search Trees

The binary search tree can be used as both a dictionary and a priority queue.

Basic operations on a binary search tree take time proportional to the height of the tree. For a complete binary tree with *n* nodes, such operations run in Ө(lg *n*) worst-case time. If the tree is a linear chain of *n* nodes, however, the same operations take Ө(*n*) worst-case time.

In practice we can't always guarantee that a binary search tree has Ө(lg *n*) time, but we can design variations o binary search trees with good guaranteed worst-case performance on basic operations.


## 12.1 What is a binary search tree?

A binary search tree is a linked data structure in which each node is an object. In addition to a *key* and satellite data, each node contains attributes *left*, *right*, and *p* that point to the nodes corresponding to its left child, right child, and parent, respectively. If a child or the parent is missing, the appropriate attribute contains the value NIL.

The keys in a binary search tree are always stored in such a way as to satisfy the *binary-search-tree property*:

Let *x* be a node in a binary search tree. If *y* is a node in the left subtree of *x*, then *y.key* ≤ *x.key*. If *y* is a node in the right subtree of *x*, then *y.key* ≥ *x.key*.

* *Inorder tree walk*
* *Preorder tree walk*
* *Postorder tree walk*

### Definitions

*Red-black tree* a variation on the binary search tree with good guaranteed worst-case performance for basic operations.
*B-tree* an ADT that is particularly good for maintaining databases on secondary storage.
*Inorder tree walk* a simple recursive algorithm that prints out all the keys in a binary search tree in sorted order.
