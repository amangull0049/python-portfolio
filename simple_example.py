class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age 
        
    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Age:", self.age)
        

s1 = Student("AMAN GULL", 786, 18)
s1.show()    