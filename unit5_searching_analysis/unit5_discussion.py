"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # The target was not found after checking every element.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
     left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        elif target < lst[middle]:
            # The target must be in the left half.
            right = middle - 1

        else:
            # The target must be in the right half.
            left = middle + 1

    # The search space became empty, so the target was not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
     # The small dataset was sorted so that both algorithms
    # could be tested fairly, especially binary search.
    small_dataset = [3, 7, 12, 18, 25, 31, 42, 50]

    existing_value = 25
    missing_value = 20

    linear_existing = linear_search(small_dataset, existing_value)
    binary_existing = binary_search(small_dataset, existing_value)

    linear_missing = linear_search(small_dataset, missing_value)
    binary_missing = binary_search(small_dataset, missing_value)

    print("Small dataset:", small_dataset)
    print("Searching for existing value:", existing_value)
    print("Linear search result:", linear_existing)
    print("Binary search result:", binary_existing)

    print("\nSearching for missing value:", missing_value)
    print("Linear search result:", linear_missing)
    print("Binary search result:", binary_missing)

    # Both algorithms found 25 at the same index.
    # Both algorithms returned -1 for 20 because it was not present.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # range() creates a large sorted dataset containing
    # values from 0 through 99,999.
    large_dataset = list(range(100000))

    large_target = 98765

    large_linear_result = linear_search(large_dataset, large_target)
    large_binary_result = binary_search(large_dataset, large_target)

    print("Large dataset size:", len(large_dataset))
    print("Searching for:", large_target)
    print("Linear search result:", large_linear_result)
    print("Binary search result:", large_binary_result)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Edge Case 1: Empty list.
    empty_list = []

    print("\nEdge Case 1: Empty list")
    print("Linear search:", linear_search(empty_list, 10))
    print("Binary search:", binary_search(empty_list, 10))

    # Both searches return -1 because there are no elements
    # to search.

    # Edge Case 2: Single-element list with a matching value.
    single_element = [42]

    print("\nEdge Case 2: Single-element list with matching value")
    print("Linear search:", linear_search(single_element, 42))
    print("Binary search:", binary_search(single_element, 42))

    # Both algorithms correctly return index 0.

    # Edge Case 3: Target is not present in a single-element list.
    print("\nEdge Case 3: Single-element list with missing value")
    print("Linear search:", linear_search(single_element, 10))
    print("Binary search:", binary_search(single_element, 10))

    # Both algorithms return -1 because 10 is not in the list.

    # Edge Case 4: Target is the first element.
    print("\nEdge Case 4: Target at the first position")
    print("Linear search:", linear_search(small_dataset, 3))
    print("Binary search:", binary_search(small_dataset, 3))

    # Both algorithms correctly find the first element at index 0.

    # Edge Case 5: Target is the last element.
    print("\nEdge Case 5: Target at the last position")
    print("Linear search:", linear_search(small_dataset, 50))
    print("Binary search:", binary_search(small_dataset, 50))

    # Both algorithms correctly find the last element.

    print("\n=== SEARCH ANALYSIS ===")
    print("Linear search: O(n) - checks elements sequentially.")
    print("Binary search: O(log n) - repeatedly cuts the search space in half.")
    print("Binary search is faster for large sorted datasets.")
    print("Linear search is useful when data is unsorted or very small.")


if __name__ == "__main__":
    main()
