from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, grades):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.grades = grades #!this means the attribute is only special to this object which is created not to all objects in common 

    def add_grade(self, subject, grade):
        self.grades[subject] = grade #! #!this will add-up  grades of student 
    
    def get_grade(self, subject):
        return self.grades.get(subject, None) #!this will return grades of student 

    def print_grades(self):
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")

    def __str__(self):
        return f"{super().__str__()}\tStudent ID: {self.student_id}\n\tGrades: {self.grades}"     #! this will make a string representation of an object within the given class 


# mati = Student("mati", "aziz",21, 2127, {"physics": 21, "chemistr": 20})
# mati.add_grade("history", 4)
# mati.add_grade("programming", 5)
# mati.add_grade("physics", 4)
# mati.add_grade("spprt", "passed")
# # mati.print_grades()
# print(mati.__str__())


