# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

### Reflection

While completing this assignment, I learned how Python dictionaries demonstrate the basic behavior of hash tables. I practiced inserting, looking up, updating, and deleting key-value pairs. I also learned that a dictionary uses a hash function to determine where a key should be stored, which allows values to be retrieved efficiently. In average cases, dictionary operations such as lookup, insertion, and deletion can be performed in O(1) time.

One challenge I encountered was understanding how to handle keys that were not present in the dictionary. I overcame this by using the `get()` and `pop()` methods with default values. This allowed the program to handle missing keys safely without causing a `KeyError`. I also tested updating a missing key and learned that assigning a value to a new key creates a new dictionary entry.

I learned that collisions can occur when different keys are mapped to the same hash location. Hash tables use collision-resolution techniques internally so that the entries can still be stored and retrieved correctly. When collisions become more frequent, operations can take longer. Overall, this assignment helped me better understand why hash tables are useful for efficient data storage and retrieval in real-world applications.
