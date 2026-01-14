
class Person:
    species = "Humano"
     
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species
    
    @staticmethod
    def is_older(age):
        return age >= 18
       
person1 = Person("Jorge", 21)       
person2 = Person("Gael", 21)

print(person1.species)
print(person2.species)

Person.change_species("Robot")

print(person1.species)
print(person2.species)

print(Person.is_older(17))
print(person1.is_older(person1.age))