"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the specified index.
    # Elements shift right when inserting at the beginning or middle.
    # Inserting near the end usually requires less shifting.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if 0 <= index < len(lst):
    # pop(index) removes and returns the value at the specified position.
    return lst.pop(index)
    # Returning None clearly indicates that no value was removed
    return None

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # every element must be checked before determining that the value is found at the end or is not in the list.
     for index, item in enumerate(lst):
        if item == value:
            return index
    # when the value does not exist in the list
    return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create the original list that will be used for insertion tests.
    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert a value at the beginning. Existing elements shift to the right.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert a value in the middle. Elements from that position shift right.
    insert_at(numbers, 3, 25)
    print("After inserting 25 in the middle:", numbers)

    # Insert a value at the end. No existing elements need to be shifted.
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Delete the first item. Remaining elements shift one position to the left.
    removed = delete_at(numbers, 0)
    print("Removed from the beginning:", removed)
    print("Updated list:", numbers)

    # Delete an item from the middle of the list.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("Removed from the middle:", removed)
    print("Updated list:", numbers)

    # Delete the final item. No elements after it need to be shifted.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from the end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Search for a value that exists in the current list.
    value_to_find = 30
    result = search_value(numbers, value_to_find)

    if result != -1:
        print(f"Value {value_to_find} was found at index {result}.")
    else:
        print(f"Value {value_to_find} was not found.")

    # Search for a value that does not exist.
    missing_value = 100
    result = search_value(numbers, missing_value)

    if result != -1:
        print(f"Value {missing_value} was found at index {result}.")
    else:
        print(f"Value {missing_value} was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
     # Edge case 1: Attempt to delete using an invalid index.
    invalid_delete = delete_at(numbers, 100)
    print("Attempt to delete using invalid index 100:", invalid_delete)

    # Edge case 2: Insert a value into an empty list.
    empty_list = []
    insert_at(empty_list, 0, 99)
    print("After inserting 99 into an empty list:", empty_list)

    # Edge case 3: Attempt to delete from an empty list.
    empty_list = []
    empty_delete = delete_at(empty_list, 0)
    print("Attempt to delete from an empty list:", empty_delete)

    # Edge case 4: Search for a missing value in an empty list.
    empty_search = search_value(empty_list, 10)
    print("Search for 10 in an empty list:", empty_search)


if __name__ == "__main__":
    main()
