# # import numpy as np 
# # while True: 
# #     def seqsearch(arr, target): 
# #         for i in range(len(arr)):
# #             if arr[i] == target: 
# #                 return i 
# #         return -1 and print ("target not found!")
# #     print ('enter the size of the array: ')
# #     size = int (input())
# #     arr = [np.random.randint(0, 100) for i in range(size)]
# #     asc = np.sort(arr)
# #     dsc = np.sort (arr)[::-1]
# #     print ("the random array: " , arr)
# #     print ("the sorted array in ascending order: " , asc)
# #     print ("the sorted array in descending order: " , dsc)
# #     print ("enter the element you want to seach: ")
# #     target = int (input()) 
# #     print ("index of the element you want to search in ascending order is: ", seqsearch(asc,target))
# #     print ("index of the element you want to search in descending order is: ", seqsearch(dsc,target))
# #     print ("index of the element you want to search in random array is: ", seqsearch(arr,target))




# import random
# import time 
# while True: 
#     def sequential_search(A, n, x):
#         count = 0 
#         for i in range(n):
#             if A[i] == x:
#                 return i, count 
#             count += 1
#             # Барьерная операция
#             # elif A[i] > x:
#             #     break
#         return -1, count 
#     # Функция генерации массива
#     def generate_array(n, array_type):
#         if array_type == "random":
#             return [random.randint(0, n*10) for i in range(n)]
#         elif array_type == "increasing":
#             return [i for i in range(n)]
#         elif array_type == "decreasing":
#             return [i for i in range(n, 0, -1)]
#     # Тестирование функции
#     n = int(input("Введите размер массива: "))
#     array_type = input("Введите тип массива (random, increasing, decreasing): ")
#     start = time.time()
#     A = generate_array(n, array_type)
#     print("Массив:", A)
#     x = int(input("Введите элемент для поиска: "))
#     s = time.time()
#     index , count = sequential_search(A, n, x)
#     if index == -1:
#         print("Элемент не найден")
#     else:
#         print("Индекс элемента:", index)
#     print ("compared items: " , count)
#     e = time.time() 
#     print ("time: " , e - s )

# # import random
# def sequential_search(A, n, x):
#     count = 0
#     for i in range(n):
#         count += 1 # увеличиваем счетчик в каждой итерации цикла
#         if A[i] == x:
#             return i, count
#         # Барьерная операция
#         elif A[i] > x:
#             break
#     return -1, count

# # Функция генерации массива
# def generate_array(n, array_type):
#     if array_type == "random":
#         return [random.randint(0, n*10) for i in range(n)]
#     elif array_type == "increasing":
#         return [i for i in range(n)]
#     elif array_type == "decreasing":
#         return [i for i in range(n, 0, -1)]

# # Тестирование функции
# n = int(input("Введите размер массива: "))
# array_type = input("Введите тип массива (random, increasing, decreasing): ")
# A = generate_array(n, array_type)
# print("Массив:", A)
# x = int(input("Введите элемент для поиска: "))
# index, count = sequential_search(A, n, x)
# if index == -1:
#     print("Элемент не найден")
# else:
#     print("Индекс элемента:", index)
# print("Количество операций сравнения:", count)



from random import randint

def linear_search(lst, target):
    comparisons = 0
    lst.append(target)
    size = len (lst)
    for i, num in enumerate(lst):
        comparisons += 1
        if num == target:
            if i == size -1: 
                print (f"not Found {target} at index {i}")
                break 
            print(f"Found {target} at index {i}")
            break
    print(f"Program made {comparisons} comparisons")
while True: 
    length = int(input("Enter length of list: "))
    lst = [randint(1, 100) for _ in range(length)]
    print(f"Generated list: {lst}")
    target = int(input("Enter target number: "))
    linear_search(lst, target)



