# Создать список (автосалон), состоящий из словарей (машина). Словари должны содержать как минимум 5 полей
# (например, номер, модель, год выпуска, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# cars = [{"id":123456, "model":"Mercedes-Benz", "year": 2019, ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех машинах;
# – вывода информации о машине по введенному с клавиатуры номеру;
# – вывода количества машин, моложе введённого года;
# – обновлении всей информации о машине по введенному номеру;
# – удалении машины по номеру.
# Провести тестирование функций.

cars = [{"id":1, "model":"Mercedes-Benz", "year": 2019, "colour": "red", "price": 100},
        {"id":2, "model":"Toyota", "year": 2011, "colour": "dark-red", "price": 150},
        {"id":3, "model":"bmw", "year": 2023, "colour": "white", "price": 130},
        {"id":4, "model":"ford", "year": 2010, "colour": "black", "price": 50},
        {"id":5, "model":"Honda", "year": 2012, "colour": "yellow", "price": 70},
        {"id":6, "model":"ferari", "year": 2021, "colour": "golden", "price": 170},
        {"id":7, "model":"chevrolet", "year": 2015, "colour": "pink", "price": 180},
        {"id":8, "model":"Mazda", "year": 2009, "colour": "white", "price": 80},
        {"id":9, "model":"audi", "year": 2002, "colour": "blue", "price": 102},
        {"id":10, "model":"lexus", "year": 2000, "colour": "red", "price": 200},
        ]

def information(cars): 
    for car in cars: 
            print (car)

def information_by_id(cars): 
    print ("Please enter the id of the car you want to search")
    id = int (input ()) 
    for car in cars: 
        if car["id"] == id: 
            print (car)

def young_Cars(cars):
    print ("enter the year: ") 
    year = int (input ()) 
    # young_car = max([car['year'] for car in cars])
    young_car_num= [car for car in cars if car['year'] > year]
    # young_car_num= ([car for car in cars if car['year'] == young_car] )# if you wanted to see how many put the len and use for loop to print all of them 
    
    print (young_car_num)

def edit_info(cars): 
    print ('Enter the id number of the car') 
    id = int (input())
    for car in cars : 
        if car['id'] == id: 
            print ('Enter new model: ')
            car['model'] = str(input())
            print ('\n Enter new year: ')
            car ['year'] = int(input())
            print ('\n Enter new color: ')
            car ['color'] = str(input())
            print ('\n Enter new Price: ')
            car ['price'] = int(input())
    for car in cars: 
        print (car)


def delete_car(cars): 
    print ("Enter the id of car you want to delete: \n")
    id = int(input())
    for car in cars: 
        if car['id'] == id:
            cars.remove(car) 
            for car in cars: 
                print (car)
    
    


while True: 
    
    print ('choose an option to continue \n 1: Information about all the cars\n 2: Information about cars by id\n 3: find the most recent cars \n 4: edit information about a car \n 5: delete a car ')
    user = int (input ())
    if user == 1: 
        information(cars)
    elif user == 2: 
        information_by_id(cars)
    elif user == 3: 
        young_Cars(cars)
    elif user == 4: 
        edit_info(cars)
    elif user == 5:
        delete_car(cars)
    else: 
        print ("Enter a valid input! \n")



















# def myf (cars) : 
#     print ('choose an option to continue \n 1: Information about all the cars\n 2: Information about cars by id\n 3: find the most recent cars \n 4: edit information about a car \n 5: delete a car ')
#     user = int (input ())
#     if user == 1: 
#         for car in cars: 
#             print (car)
#     elif user == 2: 
#         print ("Please enter the id of the car you want to search")
#         id = int (input ()) 
#         for car in cars: 
#             if car["id"] == id: 
#                 print (car)
#     elif user == 3: 
#         young_car = max([car['year'] for car in cars])
#         # young_car_num= [car for car in cars if car['year'] == young_car]
#         young_car_num= ([car for car in cars if car['year'] == young_car] )# if you wanted to see how many put the len and use for loop to print all of them 
#         print (young_car_num)
#     elif user == 4: 
#         print ('Enter the id number of the car') 
#         id = int (input())
#         for car in cars : 
#             if car['id'] == id: 
#                 print ('Enter new model: ')
#                 car['model'] = str(input())
#                 print ('\n Enter new year: ')
#                 car ['year'] = int(input())
#                 print ('\n Enter new color: ')
#                 car ['color'] = str(input())
#                 print ('\n Enter new Price: ')
#                 car ['price'] = int(input())
#         for car in cars: 
#             print (car)
#     elif user == 5: 
#         print ("Enter the id of car you want to delete: \n")
#         id = int(input())
#         for car in cars: 
#             if car['id'] == id:
#                 cars.remove(car) 
#         for car in cars: 
#             print (car)
#     else: 
#         print ("Enter a valid input! \n")
#         myf()
# while True:         
#     cars = [{"id":1, "model":"Mercedes-Benz", "year": 2019, "colour": "red", "price": 100},
#             {"id":2, "model":"Toyota", "year": 2011, "colour": "dark-red", "price": 150},
#             {"id":3, "model":"bmw", "year": 2023, "colour": "white", "price": 130},
#             {"id":4, "model":"ford", "year": 2010, "colour": "black", "price": 50},
#             {"id":5, "model":"Honda", "year": 2012, "colour": "yellow", "price": 70},
#             {"id":6, "model":"ferari", "year": 2021, "colour": "golden", "price": 170},
#             {"id":7, "model":"chevrolet", "year": 2015, "colour": "pink", "price": 180},
#             {"id":8, "model":"Mazda", "year": 2009, "colour": "white", "price": 80},
#             {"id":9, "model":"audi", "year": 2002, "colour": "blue", "price": 102},
#             {"id":10, "model":"lexus", "year": 2000, "colour": "red", "price": 200},
#             ]
#     myf(cars)


# for car in cars : 
    # print (car)