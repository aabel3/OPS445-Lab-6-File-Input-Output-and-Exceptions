#!/usr/bin//env python3

from student import Student

student1 = Student("Andrew", "012345678")
# Add new course for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops235', 3.5)
student1.addGrade('ops435', 3.0)
print(student1.name)
print(student1.number)
print(student1.courses)
student1.displayStudent()

print("")

student2 = Student("Joe", "987654321")
# Add new courses for student2
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)
print(student2.name)
print(student2.number)
print(student2.courses)
student2.displayStudent()
