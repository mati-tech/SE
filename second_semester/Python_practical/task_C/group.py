import pickle 
import datetime 
from student import Student
from professor import Professor

class Group:
    def __init__(self, group_num, students, professor):
        self.group_num = group_num
        self.students = students
        self.professor = professor
        self.log("CRE", f"group: {self.group_num} created")
        
    def log(self, key, comment):
        now = datetime.datetime.now()
        log_data= f"{key} --- {now} --- {comment}"
        with open('log.txt', 'a') as f:
            f.write(log_data + '\n')
    
    def __len__(self):
        self.log("INF", f"{self.group_num} length has been called")
        return len(self.students)
    
    def get_person(self, index):
        
        if index == 0:
            self.log("INF", f"From {self.group_num} professor info has been called")
            return print(f"{index}: {self.professor}")
        elif index > 0 and index <= len(self.students):
            self.log("INF", f"From {self.group_num} student info has been called")
            return print(f"{index}: {self.students[index - 1]}")
        else:
            raise IndexError("Invalid index")
    
    def set_person(self, index, person):
        if index == 0:
            self.log("INF", f"To {self.group_num} professor {person} has been set")
            self.professor = person
        elif index > 0 and index <= len(self.students):
            self.log("INF", f"To {self.group_num} student {person} has been set")
            self.students[index - 1] = person
        else:
            raise IndexError("Invalid index")
    
    def remove_person(self, index):
        if index == 0:
            self.log("INF", f"From {self.group_num} professor has been removed")
            self.professor = None
        elif index > 0 and index <= len(self.students):
            self.log("INF", f"From {self.group_num} student {self.students[index - 1]} has been removed")
            del self.students[index - 1]
        else:
            raise IndexError("Invalid index")
    
    def add_student(self, student):
        self.students.append(student)
        self.log("INF", f"student : {student} has been added to the group {self.group_num}")

    
    def remove_student(self, student):
        self.log("INF", f"student : {student} has been removed from the group {self.group_num}")
        self.students.remove(student)
    
    def __str__(self):
        output = f"Group {self.group_num}:\n"
        output += f"Professor: {self.professor}\n"
        output += "Students:\n"
        for i in range(len(self.students)):
            output += f"{i+1}->\t {self.students[i]}\n"
        self.log("INF", f"information about group: {self.group_num} printed")
        return output
