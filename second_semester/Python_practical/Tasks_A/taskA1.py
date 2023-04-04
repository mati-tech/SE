# Написать функцию very_even(number), которая определяет является ли число "очень четным".
# Однозначное число "очень четное", если оно четное. Числа больше 10 "очень четные",
# если сумма их цифр - "очень четное" число.
#
# Примеры:
# very_even(88) => False -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 нечетное
# very_even(222) => True -> 2 + 2 + 2 = 8 => 8 четное

import traceback


def very_even(number):
    if number < 10 : 
        return number % 2 == 0
    digit = [int(i) for i in str(number)]
    sums = sum (digit)  
    return very_even(sums)
        
    
    
    # Тело функции
    #digits_sum = sum(int(digit) for digit in str(number))
    #return digits_sum % 2 == 0 and all(int(digit) % 2 == 0 for digit in str(number))
    
    # digits = [int(digit) for digit in str(number)] 
    # digit_sum = sum (digits) 
    # while digit_sum>10 : 
    #     digits = [int(i) for i in str(digit_sum)]
    #     digit_sum = sum (digits)
    
    # return digit_sum % 2 == 0 
    
    
# very_even(7897)
# Тесты
try:
    assert very_even(4) == True
    assert very_even(5) == False
    assert very_even(12) == False
    assert very_even(1234) == False
    assert very_even(7897) ==  True 
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")