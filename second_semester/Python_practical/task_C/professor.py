import pickle 
import datetime 


from person import Person

class Professor(Person):
    def __init__(self, first_name, last_name, age, professor_id, position):
        super().__init__(first_name, last_name, age)
        self.professor_id = professor_id
        self.position = position
        self.courses = []
        self.log("CRE", f"Professor created with the following name: {self.first_name} {self.last_name}")
        #! here they are declared to be unique to every object , not to whole class  

    def add_course(self, course):
        self.log("INF", f"{course} course has been added to professor {self.last_name}")
        self.courses.append(course)
    
    def remove_course(self, course):
        self.log("INF", f"{course} course has been removed from professor {self.last_name}")
        if course in self.courses:
            self.courses.remove(course)
            
    def log(self, key, comment):
        now = datetime.datetime.now()
        log_data= f"{key} --- {now} --- {comment}"
        with open('log.txt', 'a') as f:
            f.write(log_data + '\n')
            
    
    def print_courses(self):
        self.log("INF", f"Course of professor {self.last_name} has been printed")
        if self.courses: 
            print ("Available courses: ")
            for i in range(len(self.courses)):
                print ("|",i+1, ' : ', self.courses[i], end= ' ')
            print ('\n')
        else: 
            print ("No courses available!")
            
    def set_position(self, position):
        self.log("INF", f"professor {self.last_name} has been set as {self.position}")
        self.position = position
        
    def change_position(self, new_position):
        self.log("INF", f"professor {self.last_name} has been changed to {self.position}")
        self.position = new_position
    
    def __str__(self):
        self.log("INF", f"information about professor: {self.first_name} {self.last_name} printed")
        return f"{super().__str__()}\tProfessor ID: {self.professor_id}\n\tPosition: {self.position}"

