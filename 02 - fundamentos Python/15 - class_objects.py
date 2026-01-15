
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    def work(self):
        return f"{self.name} esta trabajando."
    
person1 = Person("Jorge", 21)   
person2 = Person("Gael", 21)   

print(person1.work())
print(person2.work())