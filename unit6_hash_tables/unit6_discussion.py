"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    reservations = {}

    # Insert five reservation records.
    reservations["Smith"] = "7:00 PM"
    reservations["Johnson"] = "7:15 PM"
    reservations["Williams"] = "7:30 PM"
    reservations["Brown"] = "7:45 PM"
    reservations["Davis"] = "8:00 PM"

    print("\n=== INSERT OPERATIONS ===")
    print("Reservations after inserting five entries:")
    print(reservations)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("Smith reservation:", reservations["Smith"])
    print("Brown reservation:", reservations["Brown"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before update:")
    print(reservations)

    # Assigning a new value to an existing key replaces
    # the old value associated with that key.
    reservations["Smith"] = "8:30 PM"

    print("After updating Smith's reservation:")
    print(reservations)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before deletion:")
    print(reservations)

    # The del statement removes the key and its associated value
    # from the dictionary.
    del reservations["Davis"]

    print("After deleting Davis's reservation:")
    print(reservations)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
     missing_reservation = reservations.get("Anderson")

    if missing_reservation is None:
        print("Edge case 1: Anderson was not found in the reservation table.")

    # Edge case 2: Safely deleting a key that does not exist.
    # The pop() method with a default value prevents a KeyError.
    deleted_value = reservations.pop("Anderson", None)

    if deleted_value is None:
        print("Edge case 2: Anderson could not be deleted because the key does not exist.")

    # Edge case 3: Updating a missing key.
    # Assigning a value to a new key creates a new dictionary entry.
    reservations["Anderson"] = "8:45 PM"
    print("Edge case 3: Anderson was added as a new reservation:")
    print(reservations["Anderson"])

     print("\n=== CUSTOM REAL-WORLD SCENARIO ===")

    restaurant_reservations = {
        "Garcia": "6:30 PM",
        "Lee": "7:00 PM",
        "Patel": "7:30 PM",
        "Wilson": "8:00 PM",
        "Taylor": "8:30 PM"
    }

    print("Restaurant reservation system:")
    print(restaurant_reservations)

    # A host can quickly look up a customer's reservation
    # by using the customer's last name as the key.
    customer = "Patel"

    if customer in restaurant_reservations:
        print(
            f"{customer}'s reservation was found at "
            f"{restaurant_reservations[customer]}."
        )
    else:
        print(f"No reservation was found for {customer}.")

    print("\n=== HASH TABLE SUMMARY ===")
    print(
        "Python dictionaries use hashing to store and retrieve "
        "key-value pairs efficiently."
    )
    print(
        "Collisions can occur when different keys produce the "
        "same hash location. Python handles collisions internally "
        "so the dictionary can continue to operate correctly."
    )


if __name__ == "__main__":
    main()
