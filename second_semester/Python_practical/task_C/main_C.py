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

#!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===

import pickle 
import datetime
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
    new_stu = Student(first_name, last_name, age, student_id, grades)
    # object_list.append(new_stu)
    return new_stu

def create_professor():
    print("Creating a new professor...")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    professor_id = input("Enter professor ID: ")
    position = input("Enter position: ")
    new_prof = Professor(first_name, last_name, age, professor_id, position)
    # object_list.append(new_prof)
    return new_prof

def save_groups_to_file(groups):
    with open("groups.txt", "w") as f:
        for group in groups:
            f.write(str(group))
    print ("Groups are saved to file (groups.txt)!")

def save_groups_to_pickle(object_list): 
    with open("groups.pickle", "wb") as f:
        pickle.dump(object_list, f)
    print ("Groups are saved to pickle (groups.pickle)!")

def read_group_from_pickle():
    with open("groups.pickle", "rb") as f:
        object_list_readed = pickle.load(f)
    print ("Groups are read from pickle (groups.pickle)!")
    print("Available groups:")
    for group in object_list_readed:
        print(group)
    try: 
        choice = int(input("Enter group number to view details (or leave blank to continue): "))
        if (choice > 0) and (choice <=len(object_list_readed)):
            group_num = int(choice)-1
            group = object_list_readed[group_num]
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
        with open("groups.pickle", "wb") as f:
            pickle.dump(object_list_readed, f)
    except ValueError:
        print ("invalid group no.")
        

object_list = []
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
    new_group = Group(group_num, students, professor)
    object_list.append(new_group)
    return new_group

def display_groups(groups):
    print("Available groups:")
    for group in groups:
        print(group)
    # choice = int(input("Enter group number to view details (or leave blank to continue): "))
    try: 
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
    except ValueError:
        print("Please enter a valid integer choice.")
def main():
    groups = []
    while True:
        print("Choose an option:")
        print("1. Create a new group")
        print("2. Display available groups and their details")
        print ("3. Save the information to a file")
        print("4. Save the groups to a pickle file")
        print("5. Read the groups from the pickle file")
        print("6. Quit")
        choice = input("Enter choice: ")
        if choice == '1':
            group = create_group()
            groups.append(group)
        elif choice == '2':
            display_groups(groups)
        elif choice == '3':
            save_groups_to_file(groups)
        elif choice == '4':
            save_groups_to_pickle(object_list)
        elif choice == '5':
            read_group_from_pickle()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == '__main__':
    main()



