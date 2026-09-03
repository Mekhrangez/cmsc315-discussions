"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # location for the new value in the tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
         # When an empty position is found, create a new node.
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        else:
            # Duplicate values are ignored to keep each value unique.
            print(f"Duplicate value {value} was not inserted.")

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
         return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # If the current node is empty, the value does not exist.
        if node is None:
            return False

        # The value was found.
        if value == node.value:
            return True

        # Search only the left subtree if the value is smaller.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Otherwise, search the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
          if node is not None:

            # Visit the left subtree first because it contains
            # values smaller than the current node.
            self._inorder_recursive(node.left, values)

            # Visit the current node.
            values.append(node.value)

            # Visit the right subtree because it contains
            # values larger than the current node.
            self._inorder_recursive(node.right, values)

            # BST values are ordered left < node < right,
            # in-order traversal naturally produces sorted output.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
     bst = BST()

    # These values create nodes on both the left and right sides
    # of the tree. The BST structure reduces search space because
    # each comparison eliminates one entire subtree.
    values = [50, 30, 70, 20, 40, 60, 80, 10, 35]

    print("Values being inserted:", values)

    for value in values:
        bst.insert(value)

    print("Tree construction completed.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    # In-order traversal visits left subtree, current node,
    # and then right subtree. Since BST values follow the
    # left < node < right rule, the result is sorted.
    sorted_values = bst.inorder()

    print("In-order traversal:", sorted_values)
    print("The traversal produces sorted values because smaller")
    print("values are stored to the left and larger values to the right.")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    search_values = [20, 60, 25, 90]

    # The first two values exist in the tree, while the last
    # two values do not. The search follows only one branch
    # at each comparison instead of checking every value.
    for value in search_values:
        result = bst.search(value)

        if result:
            print(f"Search for {value}: Found")
        else:
            print(f"Search for {value}: Not Found")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
   # Empty tree demonstration.
    empty_bst = BST()

    print("Empty tree traversal:", empty_bst.inorder())
    print("Search for 10 in empty tree:", empty_bst.search(10))

    # Duplicate values are ignored so the tree keeps unique values.
    print("\nTesting duplicate insertion:")
    bst.insert(50)

    print("Traversal after duplicate attempt:", bst.inorder())

if __name__ == "__main__":
    main()
