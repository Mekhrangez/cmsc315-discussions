"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Class variable shared by all ParentClass and child objects
    category = "Person"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_info(self):
        """Return basic information about the person."""
        return f"Name: {self.name}, Age: {self.age}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable
    role = "Student"

    def __init__(self, name, age, student_id, major):
        # Call the parent constructor
        super().__init__(name, age)

        # New instance variables
        self.student_id = student_id
        self.major = major

        # Student-created extension: nested mutable data
        self.courses = []

    def display_info(self):
        """Override the parent method."""
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Student ID: {self.student_id}, Major: {self.major}"
        )

    def add_course(self, course_name):
        """Add a course to the student's course list."""
        self.courses.append(course_name)

    def display_courses(self):
        """Return the student's current course list."""
        return f"Courses: {self.courses}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    
    # Create two ChildClass objects
    student1 = ChildClass("Alex", 25, "S1001", "Computer Science")
    student2 = ChildClass("Jordan", 27, "S1002", "Cybersecurity")

    # Access the class variable through the class itself
    print("Class variable through class:", ChildClass.role)

    # Access the same class variable through an object
    print("Class variable through student1:", student1.role)

    # Add an attribute to only student1 after creation
    student1.favorite_language = "Python"

    # Display the instance namespaces
    print("\nstudent1 namespace:")
    print(student1.__dict__)

    print("\nstudent2 namespace:")
    print(student2.__dict__)

    # Display information about the class namespace
    print("\nChildClass namespace:")
    print(ChildClass.__dict__)



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object containing nested mutable data.
    original = ChildClass("Taylor", 24, "S1003", "Software Development")
    original.courses = [
        {"name": "Python", "credits": 3},
        {"name": "Database Systems", "credits": 3}
    ]

    # A shallow copy creates a new outer object, but nested objects
    # are still shared between the original and the copy.
    shallow_copy = copy(original)

    # A deep copy creates a new outer object and recursively copies
    # the nested mutable objects as well.
    deep_copy = deepcopy(original)

    # Modify the original object's nested data.
    original.courses[0]["name"] = "Advanced Python"
    original.courses.append({"name": "Cybersecurity", "credits": 3})

    print("Original object:")
    print(original.__dict__)

    print("\nShallow copy:")
    print(shallow_copy.__dict__)

    print("\nDeep copy:")
    print(deep_copy.__dict__)

    print("\nExplanation:")
    print(
        "The shallow copy shared the nested courses list with the original, "
        "so changes to the nested data appeared in both objects."
    )
    print(
        "The deep copy created independent nested objects, so changes to the "
        "original nested data did not affect the deep copy."
    )


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a ParentClass object
    print("\nParent object:")
    parent = ParentClass("Morgan", 30)
    print(parent.display_info())

    # Create and test a ChildClass object
    print("\nChild object:")
    child = ChildClass("Casey", 22, "S1004", "Computer Science")
    print(child.display_info())

    # Demonstrate the child-specific method
    child.add_course("Object-Oriented Programming")
    print(child.display_courses())


    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
