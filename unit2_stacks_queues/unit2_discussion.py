"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)
        
        
    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty(): return "Stack is empty. Nothing to pop." 
            return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
       if self.is_empty(): return "Stack is empty. Nothing to peek." 
           return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty(): return "Queue is empty. Nothing to dequeue."
            return self.items.popleft()

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO: Browser Undo History (LIFO) ===") 
stack = Stack() 
print("Adding four actions to the stack:") 
for action in ["Type a sentence", "Bold text", "Insert image", "Change font"]: 
    stack.push(action) 
    print(f" Pushed: {action}")
    print(f"\nTop action using peek(): {stack.peek()}")
    print("The stack removes the most recent action first (LIFO):") 
    while not stack.is_empty():
        print(f" Popped: {stack.pop()}") 
        print(f"\nPop on an empty stack: {stack.pop()}")
        print(f"Peek on an empty stack: {stack.peek()}")
        print("\nSingle-item stack edge case:") 
        single_stack = Stack() single_stack.push("Only action")
        print(f" Added: {single_stack.peek()}") 
        print(f" Removed: {single_stack.pop()}")
        print(f" Is the stack empty? {single_stack.is_empty()}")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO: Coffee Shop Customers (FIFO) ===") 
queue = Queue() 
print("Adding four customers to the queue:")
for customer in ["Maria", "James", "Olivia", "Daniel"]: 
    queue.enqueue(customer) 
     print(f" Enqueued: {customer}") 
print(f"\nCustomer at the front: {queue.front()}") 
print("Customers are served in the order they arrived (FIFO):")
while not queue.is_empty():
    print(f" Dequeued: {queue.dequeue()}")
print(f"\nDequeue on an empty queue: {queue.dequeue()}") 
print(f"Front on an empty queue: {queue.front()}") 
print("\nSingle-item queue edge case:") 
single_queue = Queue() single_queue.enqueue("Only customer") 
print(f" Added: {single_queue.front()}") 
print(f" Removed: {single_queue.dequeue()}") 
print(f" Is the queue empty? {single_queue.is_empty()}")
# =============================== 
# CUSTOM SCENARIO APPLICATION 
# =============================== 
print("\n=== CUSTOM SCENARIO: Support Desk ===") 
support_queue = Queue() 
support_queue.enqueue("Reset password")
support_queue.enqueue("Install printer") 
support_queue.enqueue("Update software") 
print("Support tickets are processed in the order received:") 
while not support_queue.is_empty():
    print(f" Processing ticket: {support_queue.dequeue()}") 
action_history = Stack() 
action_history.push("Opened support ticket") 
action_history.push("Updated ticket details") 
action_history.push("Closed support ticket")
print("\nRecent support actions can be undone in reverse order:") 
while not action_history.is_empty(): 
    print(f" Undoing action: {action_history.pop()}")

if __name__ == "__main__":
    main()
