import pickle 
import datetime 


from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, grades):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.grades = grades #!this means the attribute is only special to this object which is created not to all objects in common 
        self.log("CRE", f"Student created with the following name: {self.first_name} {self.last_name}")
        
    def log(self, key, comment):
        now = datetime.datetime.now()
        log_data= f"{key} --- {now} --- {comment}"
        with open('log.txt', 'a') as f:
            f.write(log_data + '\n')

    def add_grade(self, subject, grade):
        self.log("INF", f"{grade} grade has been added to {self.first_name}'s grade in subject {self.grades[subject]}")
        self.grades[subject] = grade #! #!this will add-up  grades of student 
    
    def get_grade(self, subject):
        self.log("INF", f"{self.first_name}'s marks from {subject} has been printed")
        return self.grades.get(subject, None) #!this will return grades of student 

    def print_grades(self):
        self.log("INF", f"{self.first_name}'s grades has been printed")        
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")

    def __str__(self):
        self.log("INF", f"information about student: {self.first_name} {self.last_name} printed")
        return f"{super().__str__()}\tStudent ID: {self.student_id}\n\tGrades: {self.grades}"     #! this will make a string representation of an object within the given class 



