# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

Reflection

While completing this assignment, I learned how stacks and queues organize and access data differently. I implemented a stack using a Python list and a queue using collections.deque. I practiced the stack operations push, pop, and peek, as well as the queue operations enqueue, dequeue, and front. I also learned how to handle edge cases, such as attempting to remove or view an item when a stack or queue is empty.

One challenge was understanding the difference between operations that remove an item and operations that only view an item. I overcame this by testing each method and carefully checking the order of the output. For example, peek and front return a value without removing it, while pop and dequeue remove a value.

Stacks use LIFO because the most recently added item is removed first. A real-world example is an undo feature in a text editor. Queues use FIFO because the first item added is processed first. A coffee shop customer line or support ticket system demonstrates this behavior. This assignment helped me understand how choosing the correct data structure makes software more organized and predictable.
