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






