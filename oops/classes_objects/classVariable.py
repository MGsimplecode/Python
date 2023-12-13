class Student:
    count = 0  # Class variable to count students

    def __init__(self, name):
        self.name = name
        Student.count += 1


student1 = Student("Alice")
student2 = Student("Bob")
print(Student.count)  # Output: 2
