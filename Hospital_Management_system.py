from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod
    def show_details(self):
        pass
        
    
    
class Doctor(Person):
    def __init__(self, name, age, specialization):
        super.__init__(name, age)
        self.specialization = specialization
        
    def show_details(self):
        print(f"Doctor: {self.name}, Age: {self.age}, Specialization: {self.specialization}")
        
    
    
    
    
    
    
    
class Patient:
    
    
    
    
    
class Hospital: