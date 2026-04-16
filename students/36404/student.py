# Create the Student class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Create an object
s1 = Student("Anna", "A")

s1.index_number = 12345

# Print the grade
print(s1.grade)

# Change the grade
s1.grade = "B"

# Print the updated grade
print(s1.grade)
