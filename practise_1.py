class Student :
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("HI", self.name,"Your avgerage score is: ",sum / 3)
            
        
        
s1 = Student("AMAN GULL", [99,96,93])
s1.average()

