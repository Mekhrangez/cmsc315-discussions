# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

While completing this assignment, I learned how linear search and binary search work and how their performance changes depending on the size and organization of a dataset. I implemented both algorithms in Python and tested them with small and large sorted datasets. One challenge I encountered was understanding why binary search could be faster even though both algorithms were searching for the same value. I overcame this by focusing on how binary search eliminates half of the remaining search space after each comparison. I also tested edge cases such as an empty list, a single-element list, a missing value, and values at the beginning and end of a list.

Linear search is useful when data is unsorted, when the dataset is small, or when the cost of sorting the data is not worth the benefit of faster searching. Its time complexity is O(n) because it may need to check every element. Binary search is more efficient for large datasets when the data is already sorted because it has O(log n) time complexity. However, binary search cannot be used effectively when the data is not sorted. A real-world example of linear search would be looking for a name in an unsorted contact list, while binary search would be useful for searching an alphabetically sorted list.
