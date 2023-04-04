# Задан список, состоящий из не менее трех целых чисел. Список содержит или
# все четные числа кроме одного или все нечетные числа кроме одного.
# Написать функцию find_outlier, которая возвращает число-исключение
#
# Примеры:
# [2, 4, 0, 100, 4, 11, 2602, 36] ==> 11
# [160, 3, 1719, 19, 11, 13, -21] ==> 160


import traceback


def find_outlier(integers):
    even = []
    odd = [] 
    for i in range(len(integers)):
        if integers[i] % 2 == 0 : 
            even.append(integers[i])
        else : 
            odd.append(integers[i])
    if len(even) == 1 : return even[0]
    elif len(odd) ==1 : return odd[0]

# Тесты
try:
    assert find_outlier([2, 4, 6, 8, 10, 3]) == 3
    assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
