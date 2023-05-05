"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
Создать производный от Person класс Student. Новые поля: номер студенческого билета, зачетная книжка
    (словарь вида предмет: отметка). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления отметки в зачетную книжку, получения отметки по предмету,
    форматированной печати всей зачетной книжки. Переопределить метод преобразования в строку для печати
    основной информации (ФИ, возраст, номер студенческого).
Создать производный от Person класс Professor. Новые поля: номер удостоверения, должность, преподаваемые
    предметы (список строк). Определить конструктор, с вызовом родительского конструктора. Определить
    функции изменения должности, добавления и удаления предмета. Переопределить метод преобразования
    в строку для печати основной информации (ФИ, возраст, номер удостоверения, должность).
Создать класс Group. Поля: номер группы, список группы (список экземпляров класса Student), преподаватель-куратор
    (экземпляр класса Professor). Определить конструктор. Переопределить метод преобразования в строку для печати
    всей информации о группе (с использованием переопределения в классах Professor и Student). Переопределить
    методы получения количества студентов функцией len, получения студента/преподавателя по индексу, изменения
    по индексу, удаления по индексу (0 индекс - преподаватель, начиная с 1 - студенты). Переопределить
    операции + и - для добавления или удаления студента из группы. Добавить функцию создания txt-файла и записи
    всей информации в него (в том числе зачетной книжки студентов).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
# """


# Here is a general outline of the steps that can be taken to implement the task:

# Create a module for each class (Person, Student, Professor, and Group).
# Define the classes in each module and their constructors along with any additional functions and methods required.
# Import the necessary modules in the main program.
# Create instances of the classes and perform necessary operations.
# Handle exceptions wherever necessary.
# Perform testing for all the functions and methods defined in each class and module.
# Here are some additional tips for implementing the task:

# Use inheritance to create derived classes from the Person class.
# Use dictionaries and lists to store information about students and professors.
# Override the str method to customize the string representation of the objects.
# Use the built-in len function to get the length of the list of students in the Group class.
# Implement the add and sub methods to add or remove students from the group.
# # Use try-except blocks to handle exceptions like IndexError, KeyError, and TypeError.


# Classes and objects: You will need to create several classes, each with its own attributes and methods. An object is an instance of a class.

# Inheritance: You can create derived classes (also known as child classes or subclasses) that inherit attributes and methods from a parent class (also known as a base class or superclass).

# Methods: These are functions that are associated with a particular class. They can be used to perform actions on objects of that class.

# Constructors: These are special methods that are called when an object is created. They can be used to set the initial values of the object's attributes.

# Overriding: This is the process of providing a different implementation for a method in a subclass than the one provided in its parent class.

# Exception handling: This is the process of anticipating and handling errors that may occur during the execution of a program. You will need to use try-except blocks to handle errors that may occur in your program.

# File handling: You will need to create and write information to a text file. You can use Python's built-in file handling functions to do this.

# Once you have a good understanding of these concepts, you can start designing and implementing your classes and methods. You may find it helpful to start with a high-level design of your program before diving into the details. This will help you identify the key classes and their relationships, as well as the methods and attributes they will need.


# from person import Person
# from student import Student
# from professor import Professor
# from group import Group


# # create a person
# person = Person("John", "Doe", 25)
# print(person)


# # create a student
# student = Student("Jane", "Smith", 20, "1234", {"Math": 80, "Physics": 75})
# print(student)
# student.add_mark("Chemistry", 90)
# print(student.get_marks())
# print(str(student))


# # create a professor
# professor = Professor("Bob", "Johnson", 40, "5678", "Associate Professor", ["Math", "Physics"])
# print(professor)
# professor.change_position("Full Professor")
# professor.add_subject("Chemistry")
# professor.remove_subject("Physics")
# print(str(professor))


# # create a group
# group = Group("G1", [student], professor)
# print(group)
# print(len(group))
# print(group[0])
# group.add_student(Student("Mary", "Williams", 22, "5678", {"Math": 85, "Physics": 70}))
# print(len(group))
# print(str(group))
# group.remove_student(1)
# print(len(group))
# print(str(group))
# group.write_to_file("group_info.txt")

#!----------------------------------------------------------------

# from person import Person
# from student import Student
# from professor import Professor
# from group import Group

# def add_person():
#     name = input("Enter person's name: ")
#     lastname = input("Enter person's lastname: ")
#     age = input("Enter person's age: ")
#     person = Person(name, lastname, age)
#     people.append(person)

# def add_student():
#     name = input("Enter student's name: ")
#     age = input("Enter student's age: ")
#     email = input("Enter student's email: ")
#     major = input("Enter student's major: ")
#     gpa = input("Enter student's GPA: ")
#     student = Student(name, age, email, major, gpa)
#     students.append(student)

# def add_professor():
#     name = input("Enter professor's name: ")
#     age = input("Enter professor's age: ")
#     email = input("Enter professor's email: ")
#     department = input("Enter professor's department: ")
#     experience = input("Enter professor's years of experience: ")
#     professor = Professor(name, age, email, department, experience)
#     professors.append(professor)

# def add_group():
#     name = input("Enter group's name: ")
#     description = input("Enter group's description: ")
#     member_names = input("Enter member names (separated by commas): ")
#     members = []
#     for name in member_names.split(','):
#         for person in people:
#             if person.name == name.strip():
#                 members.append(person)
#                 break
#         else:
#             print(f"No person found with name {name.strip()}")
#     group = Group(name, description, members)
#     groups.append(group)

# def list_people():
#     for person in people:
#         print(person)

# def list_students():
#     for student in students:
#         print(student)

# def list_professors():
#     for professor in professors:
#         print(professor)

# def list_groups():
#     for group in groups:
#         print(group)

# people = []
# students = []
# professors = []
# groups = []

# while True:
#     print("""
#     Welcome to the University System!
#     1. Add a new person
#     2. Add a new student
#     3. Add a new professor
#     4. Add a new group
#     5. List all persons
#     6. List all students
#     7. List all professors
#     8. List all groups
#     9. Quit
#     """)
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         add_person()
#     elif choice == "2":
#         add_student()
#     elif choice == "3":
#         add_professor()
#     elif choice == "4":
#         add_group()
#     elif choice == "5":
#         list_people()
#     elif choice == "6":
#         list_students()
#     elif choice == "7":
#         list_professors()
#     elif choice == "8":
#         list_groups()
#     elif choice == "9":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")


#!----------
# person : 
# name, lastname age
# __str to print all data about it

# student: 
# name, lastname, age, id, grades

# prof: 
# name , lastname, age, id, position, courses, 
#!=====================================================
#!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===

# from person import Person
# from student import Student
# from professor import Professor
# from group import Group
# def person():
#     print ("""
#         1: Add a new person
#         2: print all people
#         3: print all students
#         4: print all professors
#         5: print all groups
#         """)
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print ("Enter details of the person: ")
#         name = input("name: ")
#         lastname = input ("lastname: ")
#         age = int(input("age: "))
#         name = Person(name, lastname, age)
#         people.append(name)
#         return True 
#     elif choice == "2":
#         for person in people:
#             print (person)
#         return True 
#     elif choice == "3":
#         for stu in students:
#             print (stu)
#         return True
#     elif choice == "4":
#         for prof in professors:
#             print (prof)
#         return True
#     elif choice == "5":
#         print("main menu\n")
#     else:
#         print("Invalid choice. Please try again.\n")
# def student(): 
#     print ("""
#         1: Add a new student
#         2: add grades to current student
#         3: get grades of current student
#         4: print all grades
#         5: print all information about given student
#         """)
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print ("Enter details of the student: \n")
#         name = input("name: ")
#         lastname = input ("lastname: ")
#         age = int(input("age: "))
#         id = int (input("id: "))
#         grades = input("Please enter subject:grade pairs (separated by commas): \n")
#         pairs = grades.split(",")
#         grade_dict = {}
#         for pair in pairs:
#             sub, grade = pair.split(":")
#             grade_dict[sub.strip()] = grade.strip()
#         name = Student(name, lastname, age, id, grade_dict)
#         students.append(name)
#         return True 
#     elif choice == "2": #add grade 
#         stu_name = input("Student name: ")
#         found = False  
#         for stu in students: 
#             if stu.first_name == stu_name:
#                 found = True  
#                 break 
#         if found: 
#             subject = input ("subject: ")
#             grade = input ("grade: ")
#             stu_name.add_grade(subject, grade)
#         else: 
#             print ("student not found!")
#             return True 
#     elif choice == "3": #get grade 
#         stu_name = input("Student name: ")
#         found = False  
#         for stu in students: 
#             if stu.first_name == stu_name:
#                 found = True  
#                 break 
#         if found: 
#             subject = input ("subject: ")
#             print(stu_name.get_grade(subject))
#         else: 
#             print ("student not found!")
#             return True 
#     elif choice == "4":#all grades 
#         stu_name = input("Student name: ")
#         found = False  
#         for stu in students: 
#             if stu.first_name == stu_name:
#                 found = True  
#                 break 
#         if found: 
#             stu_name.print_grades()
#             return True 
#         else: 
#             print ("student not found!")
#             return True 
#     elif choice == "5":
#         stu_name = input("Student name: ")
#         found = False  
#         for stu in students: 
#             if stu.first_name == stu_name:
#                 found = True  
#                 break 
#         if found: 
#             print(stu_name.__str__())
#             return True 
#         else: 
#             print ("student not found!")
#             return True 
#     else:
#         print("Invalid choice. Please try again.\n")

# people = []
# students = []
# professors = []
# groups = []
# print ("--Welcome to University's database--")
# while True: 
#     print("""
#     1. person
#     2. student
#     3. professor
#     4. group
#     5. save database
#     5. main_menu
#     """)
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         person()
#     elif choice == "2":
#         student()
#     # elif choice == "3":
#     #     professor()
#     # elif choice == "4":
#     #     group()
#     # elif choice == "5":
#     #     print("main menu")
#     else:
#         print("Invalid choice. Please try again.")


#!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===


from person import Person
from student import Student
from professor import Professor
from group import Group

def create_student():
    print("Creating a new student...")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    student_id = input("Enter student ID: ")
    grades = {}
    while True:
        subject = input("Enter subject (or leave blank to finish): ")
        if not subject:
            break
        grade = int(input("Enter grade: "))
        grades[subject] = grade
    return Student(first_name, last_name, age, student_id, grades)

def create_professor():
    print("Creating a new professor...")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    professor_id = input("Enter professor ID: ")
    position = input("Enter position: ")
    return Professor(first_name, last_name, age, professor_id, position)

def save_groups_to_file(groups):
    with open("groups.txt", "w") as f:
        for group in groups:
            f.write(str(group))
    print ("Groups are saved to file (groups.txt)!")

def create_group():
    print("Creating a new group...")
    group_num = input("Enter group number: ")
    professor = create_professor()
    students = []
    while True:
        student = create_student()
        students.append(student)
        choice = input("Add another student? (y/n): ")
        if choice.lower() == 'n':
            break
    return Group(group_num, students, professor)

def display_groups(groups):
    print("Available groups:")
    for group in groups:
        print(group)
    choice = int(input("Enter group number to view details (or leave blank to continue): "))
    if (choice > 0) and (choice <=len(groups)):
        group_num = int(choice)-1
        group = groups[group_num - 1]
        while True:
            index = input("Enter person index to view details (or leave blank to go back): ")
            if not index:
                break
            index = int(index)
            try:
                group.get_person(index)
            except IndexError as e:
                print(e)
            else:    
                action = input("Enter 'u' to update this person, 'r' to remove this person, or leave blank to continue: ")
                if action.lower() == 'u':
                    if index == 0:
                        person = create_professor()
                    else:
                        person = create_student()
                    group.set_person(index, person)
                elif action.lower() == 'r':
                    group.remove_person(index)
    else: 
        print ("invalid group no.")
def main():
    groups = []
    while True:
        print("Choose an option:")
        print("1. Create a new group")
        print("2. Display available groups and their details")
        print ("3. Save the information to a file")
        print("4. Quit")
        choice = input("Enter choice: ")
        if choice == '1':
            group = create_group()
            groups.append(group)
        elif choice == '2':
            display_groups(groups)
        elif choice == '3':
            save_groups_to_file(groups)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == '__main__':
    main()



