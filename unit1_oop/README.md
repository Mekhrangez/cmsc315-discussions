# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.


## Implementation Documentation

### Parent Class

I created a `ParentClass` that represented a general person. The class included the class variable `category` and the instance variables `name` and `age`. I implemented the `__init__` constructor to initialize the instance variables. I also created the `display_info()` method to return information about the object.

### Child Class and Inheritance

I created a `ChildClass` that inherited from `ParentClass`. The child class added the class variable `role` and the instance variables `student_id` and `major`. I used `super().__init__()` to initialize the inherited attributes. I also added the `add_course()` and `display_courses()` methods. The `display_info()` method was overridden so that the child class could display additional student information.

As a student-created extension, I added a `courses` list and methods for adding and displaying courses. This extended the functionality of the parent class while keeping the student-specific responsibilities inside the child class.

### Namespace Demonstration

I created two `ChildClass` objects to demonstrate the difference between class and instance namespaces. I accessed the `role` class variable through both the class and an object. I also added a `favorite_language` attribute to only one object after it had been created. The `__dict__` attribute was used to display the instance namespaces and the class namespace.

This demonstrated that class variables could be shared by objects while instance attributes belonged to individual objects.

### Shallow and Deep Copy Demonstration

I created a student object containing a nested mutable `courses` list. I then created both a shallow copy and a deep copy of the object. After modifying the nested data in the original object, the shallow copy reflected the nested changes because it shared references to the nested objects. The deep copy remained independent because the nested objects were copied recursively.

### Main Function

I completed the `main()` function by creating and testing objects from both the parent and child classes. I called the overridden `display_info()` method to demonstrate inheritance and polymorphic behavior. I also called the namespace and copying demonstration functions so that all assignment requirements were executed when the program ran.

### Memory Behavior

The class variables were stored at the class level and could be accessed by multiple objects. Each object maintained its own instance attributes in its instance namespace. The shallow copy created a separate outer object but continued to reference the same nested mutable objects. The deep copy required additional memory because it created independent copies of the nested objects. Therefore, deep copying generally used more memory than shallow copying, but it provided stronger independence between objects.

### Error Handling

The program used simple and controlled operations so that the required demonstrations could run without unexpected failures. The methods were separated by responsibility, which made the program easier to test and modify. In a larger application, additional validation could be added to methods such as `add_course()` to prevent invalid or empty course values.

## Reflection

While completing this assignment, I learned how classes, objects, inheritance, namespaces, and copying worked together in Python. One challenge I encountered was understanding the difference between a class namespace and an instance namespace. I overcame this by using `__dict__` to inspect the attributes stored by the class and individual objects. I also found shallow and deep copying challenging because both copies initially appeared similar. Modifying nested data helped me understand that a shallow copy shared references to nested objects, while a deep copy created independent nested objects.

OOP differed from procedural programming because it organized data and behavior into objects instead of relying primarily on separate functions and variables. This organization improved maintainability because related functionality could remain inside a class. Inheritance also improved reusability because the child class could reuse functionality from the parent instead of duplicating code. The main overhead was that OOP could require additional planning and memory, especially when creating many objects or deep copies. These concepts could be useful in future software and cybersecurity applications because complex systems could be divided into smaller, reusable components that were easier to maintain, test, and extend.


   
