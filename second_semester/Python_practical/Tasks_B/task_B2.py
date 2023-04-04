# На вход поступает список словарей. Написать функцию sentence, которая возвращает строку,
# состоящую из слов (значений словарей), разделенных пробелом в порядке возрастания
# целочисленных значений их ключей.
#
# Пример:
# [{"12": "back"}, {"0": "Never"}, {"7": "look"}] ==> "Never look back"


import traceback


def sentence(lst):
    result = ""
    pairs = [(int(key), value) for d in lst for key, value in d.items()]
    # print (pairs)
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    # print (sorted_pairs)
    for pair in sorted_pairs:
        result+= (pair[1])+ ' '
    # print(result.strip())
    # print(len(result.strip()))
    # return result.strip()
    print (result.strip())
    return result.strip()
# test = sentence([{"0": "is"}, {"14": "never"}, {"-100": "Lost"}, {"75": "again"}, {"11": "found"},{"-9": "time"}])
# print (len(test))
# sentence = ''
# for i in len(test): 
#     if test[i] != sentence[i]:
#         print (i, sentence[i]) 
# if (test== 'Lost time /is never found again'): 
#     print ("same")
# else : print ('different')
#! the first test is not passed and dont know where is the problem(
import traceback
# print (len(sentence([{"0": "is"}, {"14": "never"}, {"-100": "Lost"}, {"75": "again"}, {"15": "found"},
#                     {"-9": "time"}])))

#! Тесты
try:
    assert sentence([{"0": "is"}, {"11": "never"}, {"-100": "Lost"}, {"75": "again"}, {"14": "found"},{"-9": "time"}]) == "Lost time is never found again"
    assert sentence([{"100": "overeducated"}, {"0": "never"}, {"15": "or"}, {"11": "overdressed"}, {"-500": "You"},
                    {"-2": "can"}, {"7": "be"}]) == "You can never be overdressed or overeducated"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")