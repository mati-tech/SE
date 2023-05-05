from person import Person

class Professor(Person):
    def __init__(self, first_name, last_name, age, professor_id, position):
        super().__init__(first_name, last_name, age)
        self.professor_id = professor_id
        self.position = position
        self.courses = []
        #! here they are declared to be unique to every object , not to whole class  

    def add_course(self, course):
        self.courses.append(course)
    
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
    def print_courses(self):
        if self.courses: 
            print ("Available courses: ")
            for i in range(len(self.courses)):
                print ("|",i+1, ' : ', self.courses[i], end= ' ')
            print ('\n')
        else: 
            print ("No courses available!")
    def set_position(self, position):
        self.position = position
    def change_position(self, new_position):
        self.position = new_position
    
    def __str__(self):
        return f"{super().__str__()}\tProfessor ID: {self.professor_id}\n\tPosition: {self.position}"


# mati = Professor("mati", "aziz", 21, 2127, 'associate professor')
# mati.add_course("mathmatics")
# mati.add_course('physics')
# mati.change_position('teacher')
# mati.professor_id= 1234
# mati.print_courses() 
# print (mati.__str__())
