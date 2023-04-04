# Написать функцию olympic_ring, которая считает количество колец в заданной строке
# латинских букв (в символе 'a' - одно кольцо, в 'B' - два). Количество колец нужно
# поделить пополам и округлить в меньшую сторону. Если результат равен 1 или меньше -
# верните «Not even a medal!», если счет равен 2 - вернуть «Bronze!»,
# если счет равен 3 - «Silver!», если оценка больше 3 - вернуть «Gold!»;
#
# Примеры:
# olympic_ring("QWertYuIoP") ==> 4 // 2 = 2 ==> "Bronze!"

import traceback


def olympic_ring(s):
    ring_count = 0
    for circle in s:
        if circle in 'aADdegqopQROb':
            ring_count += 1
        elif circle == 'B':
            ring_count += 2
    # print (ring_count)
    if ring_count % 2 == 0:
        medal_count = ring_count // 2
    else:
        medal_count = ring_count // 2 + 1
    # print(medal_count) 
    if medal_count <= 1:
        return "Not even a medal!"
    elif medal_count == 2:
        return "Bronze!"
    elif medal_count == 3:
        return "Silver!"
    else:
        return "Gold!"


# Тесты
try:
    assert olympic_ring("wHjMudLwtoPGocnJ") == "Bronze!"
    assert olympic_ring("eCEHWEPwwnvzMicyaRjk") == "Bronze!"
    assert olympic_ring("JKniLfLW") == "Not even a medal!"
    assert olympic_ring("EWlZlDFsEIBufsalqof") == "Silver!"
    assert olympic_ring("IMBAWejlGRTDWetPS") == "Gold!"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
