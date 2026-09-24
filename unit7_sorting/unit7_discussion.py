"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    result = lst.copy()
    for i in range(len(result)):
        swapped = False

        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result

def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
     if len(lst) <= 1:
        return lst.copy()

    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])

    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    dataset1 = [42, 17, 8, 99, 23, 51, 4, 76]

    print("Original dataset:", dataset1)

    bubble_result1 = bubble_sort(dataset1)
    merge_result1 = merge_sort(dataset1)

    print("Bubble Sort result:", bubble_result1)
    print("Merge Sort result:", merge_result1)
    print("Results match:", bubble_result1 == merge_result1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    dataset2 = [15, 3, 27, 3, 42, 18, 9, 30, 15]

    print("Original dataset:", dataset2)

    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    print("Bubble Sort result:", bubble_result2)
    print("Merge Sort result:", merge_result2)
    print("Results match:", bubble_result2 == merge_result2)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    empty_list = []
    print("\n1. Empty list:")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("Explanation: Both algorithms return an empty list without errors.")

    # Edge case 2: Already sorted list.
    sorted_list = [1, 2, 3, 4, 5]
    print("\n2. Already sorted list:")
    print("Original:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))
    print("Explanation: Both algorithms keep the values in sorted order. "
          "Bubble Sort can stop early because no swaps are needed.")

    # Edge case 3: Duplicate values.
    duplicate_list = [5, 2, 5, 1, 2, 5]
    print("\n3. List with duplicate values:")
    print("Original:", duplicate_list)
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort:", merge_sort(duplicate_list))
    print("Explanation: Both algorithms correctly preserve all duplicate values.")

    # Edge case 4: Single-element list.
    single_list = [10]
    print("\n4. Single-element list:")
    print("Original:", single_list)
    print("Bubble Sort:", bubble_sort(single_list))
    print("Merge Sort:", merge_sort(single_list))
    print("Explanation: A single-element list is already sorted.")




if __name__ == "__main__":
    main()
