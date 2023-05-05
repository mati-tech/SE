# from student import Student
# from professor import Professor

# class Group:
#     def __init__(self, group_num, professor):
#         self.group_num = group_num
#         self.students = []
#         self.professor = professor
    
#     def __str__(self):
#         student_info = "\n".join([str(s) for s in self.students])
#         return f"Group {self.group_num}\nProfessor: {self.professor}\nStudents:\n{student_info}"
    
#     def __len__(self):
#         return len(self.students)
    
#     def __getitem__(self, index):
#         if index == 0:
#             return self.professor
#         else:
#             return self.students[index - 1]
    
#     def __setitem__(self, index, value):
#         if index == 0:
#             self.professor = value
#         else:
#             self.students[index - 1] = value
    
#     def __delitem__(self, index):
#         if index == 0:
#             raise ValueError("Cannot delete professor")
#         else:
#             del self.students[index - 1]
    
#     def add_student(self, student):
#         self.students.append(student)
    
#     def remove_student(self, student):
#         if student in self.students:
#             self.students.remove(student)
    
#     def create_report(self, filename):
#         with open(filename, "w") as f:
#             f.write(str(self))
#             for student in self.students:
#                 f.write(f"\n\nStudent: {student}\nGrades:\n")
#                 for subject, grade in student.grades.items():
#                     f.write(f"{subject}: {grade}\n")
                    

#!============================================================

from student import Student
from professor import Professor

class Group:
    def __init__(self, group_num, students, professor):
        self.group_num = group_num
        self.students = students
        self.professor = professor
    
    def __len__(self):
        return len(self.students)
    
    def get_person(self, index):
        if index == 0:
            return print(f"{index}: {self.professor}")
        elif index > 0 and index <= len(self.students):
            return print(f"{index}: {self.students[index - 1]}")
        else:
            raise IndexError("Invalid index")
    
    def set_person(self, index, person):
        if index == 0:
            self.professor = person
        elif index > 0 and index <= len(self.students):
            self.students[index - 1] = person
        else:
            raise IndexError("Invalid index")
    
    def remove_person(self, index):
        if index == 0:
            self.professor = None
        elif index > 0 and index <= len(self.students):
            del self.students[index - 1]
        else:
            raise IndexError("Invalid index")
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)
    
    def __str__(self):
        output = f"Group {self.group_num}:\n"
        output += f"Professor: {self.professor}\n"
        output += "Students:\n"
        for i in range(len(self.students)):
            output += f"{i+1}->\t {self.students[i]}\n"
        # for student in self.students:
        #     output += f"\t{student}\n"
        return output


# ikb = Group(2922, ['mati', 'bakhti', 'diyor','abc'],professor='you')
# ikb.add_student('haroon')
# print(ikb.get_person(0))
# print (ikb.__str__())
