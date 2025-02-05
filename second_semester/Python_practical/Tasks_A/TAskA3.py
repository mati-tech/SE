# GPS в машине каждые s секунд записывает в список x значение пройденного расстояния с начала пути.
# Написать функцию gps(s, x), которая возвращает максимальную среднюю скорость среди интервалов.
# Средняя_скорость = 3600 * расстояние / s
#
# Пример:
# x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
# s = 15
# средняя_скорость_1 = 3600 * (0.19 - 0.0) / 15


import traceback


def gps(s, x):
    if len(x) < 2 : 
        speed = x[0] / s; 
        return int (speed) 
    speeds =[]
    for i in range (1, len(x)) :
        avespeed = (x[i]-x[i-1]) / (s / 3600) 
        speeds.append(avespeed)
        
    return int(max(speeds))
    # return speeds
    

# print (gps(18, [0.0]))

# Тесты
try:
    assert gps(12, [0.0, 0.24, 0.48, 0.72, 0.96, 1.2, 1.44, 1.68, 1.92, 2.16, 2.4]) == 72
    assert gps(17, [0.0, 0.02, 0.44, 0.66, 0.88, 1.1, 1.32, 1.54, 1.76]) == 88
    assert gps(18, [0.0]) == 0
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
