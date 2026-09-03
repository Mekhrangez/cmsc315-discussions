# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Implementation

I created a `Node` class to store each value and references to the left and right child nodes. I created a `BST` class that manages the tree starting from the root node.

The insert operation used recursion to place values in the correct position. Values smaller than the current node were placed in the left subtree, while larger values were placed in the right subtree. Duplicate values were not inserted.

The search operation also used recursion. Instead of checking every value like a linear search, the BST compared the target value with the current node and continued only through the appropriate subtree.

The in-order traversal visited the left subtree, current node, and right subtree. Because of the ordering rules of a BST, this produced the values in sorted order.

## Edge Cases

I tested an empty tree by performing an in-order traversal and searching for a value. The empty tree returned an empty list for traversal and `False` for the search.

I also tested duplicate insertion. Duplicate values were ignored to prevent multiple copies of the same value from being stored in the tree.

## Discussion Board Reflection

While completing this assignment, I learned how Binary Search Trees organize data using nodes and recursive operations. I practiced implementing insertion, searching, and in-order traversal. The most important concept I learned was that a BST follows an ordering rule where smaller values are placed on the left and larger values are placed on the right. This organization makes searching more efficient because each comparison can eliminate part of the tree instead of checking every item.

One challenge was understanding how recursion returns the updated node references during insertion. I overcame this by tracing each recursive call and following how the program moves through the left or right subtree until it finds an empty position. I also learned why in-order traversal produces sorted output by visiting the left subtree first, then the current node, and finally the right subtree.

Compared with a list using linear search, a balanced BST can improve search performance significantly. However, a BST can become inefficient when values are inserted in sequential order because the tree can become unbalanced and behave similarly to a linked list.
