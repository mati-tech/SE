class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        return f"Name & Surname: {self.first_name} {self.last_name}\n\tAge: {self.age}\n"

# mati = Person("mati", "aziz", 21)
# print (mati.__str__())