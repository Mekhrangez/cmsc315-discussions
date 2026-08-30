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
    playlist = ["Song A", "Song B", "Song C", "Song D"]
    print("Original playlist:", playlist)

    # Insert at the beginning.
    insert_at(playlist, 0, "New Song")
    print("After inserting at the beginning:", playlist)

    # Insert in the middle.
    insert_at(playlist, 3, "Middle Song")
    print("After inserting in the middle:", playlist)

    # Insert at the end.
    insert_at(playlist, len(playlist), "Last Song")
    print("After inserting at the end:", playlist)

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
    removed = delete_at(playlist, 0)
    print("Removed from the beginning:", removed)
    print("Updated playlist:", playlist)

    # Delete from the middle.
    middle_index = len(playlist) // 2
    removed = delete_at(playlist, middle_index)
    print("Removed from the middle:", removed)
    print("Updated playlist:", playlist)

    # Delete from the end.
    removed = delete_at(playlist, len(playlist) - 1)
    print("Removed from the end:", removed)
    print("Updated playlist:", playlist)

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
     value_to_find = "Song B"
    result = search_value(playlist, value_to_find)

    if result != -1:
        print(f"{value_to_find} was found at index {result}.")
    else:
        print(f"{value_to_find} was not found.")

    # Search for a song that does not exist.
    missing_value = "Unknown Song"
    result = search_value(playlist, missing_value)

    if result != -1:
        print(f"{missing_value} was found at index {result}.")
    else:
        print(f"{missing_value} was not found.")

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
    invalid_delete = delete_at(playlist, 100)
    print("Invalid delete:", invalid_delete)

    # Edge case 2: Insert into an empty list.
    empty_list = []
    insert_at(empty_list, 0, "New Song")
    print("Insert into empty list:", empty_list)

    # Edge case 3: Delete from an empty list.
    empty_list = []
    empty_delete = delete_at(empty_list, 0)
    print("Delete from empty list:", empty_delete)

    # Edge case 4: Search an empty list.
    empty_search = search_value(empty_list, "Song A")
    print("Search empty list:", empty_search)


if __name__ == "__main__":
    main()
