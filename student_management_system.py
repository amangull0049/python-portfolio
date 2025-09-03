# Student management system only 2 inputs by developer!

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
            
s1 = Student("AMAN GULL", 18, 39)
s2 = Student("AHMAR GULL", 23, 100)

s1.show_info()
s1.is_passed() 
       
s2.show_info()
s2.is_passed()