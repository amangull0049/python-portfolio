class Student:
    college_name = "Govt. Graduate College" 
    # default constructor
    def __init__(self):
       pass

    # parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("\nadding new students in database...\n")
        
    def hello(self):
        print("HELLO!")
        
    def welcome(self):
        print("WELCOME STUDENT", self.name)

s1 = Student("AMAN GULL", 19)
print(s1.name, s1.age)
print(Student.college_name)
s1.hello()
s1.welcome()

s2 = Student("AHMAR GULL", 22)
print(s2.name, s2.age)
print(Student.college_name)
