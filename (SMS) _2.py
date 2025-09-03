# Student management system by the user input!

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def show_info(self):
        print("\nYour Name is:",self.name)
        print("your age is:",self.age)
        print("your grade is::",self.grade)
        
        
    def is_passed(self):
        if(self.grade >= 40):
            print("You are PASSED!")
        else:
            print("You are FAILED!")
            
students = []

n = int(input("\nEnter number of students: "))

for i in range(n):
    print(f"Enter details for student {i+1}")
    name = input("Name: ")
    age = input("Age: ")
    grade = int(input("Grade:"))
    s = Student(name, age, grade)
    students.append(s)


for j in students:
    j.show_info()
    j.is_passed()
