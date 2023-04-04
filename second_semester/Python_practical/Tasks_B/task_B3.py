# Даны результаты забегов в формате "h|m|s, h|m|s, h|m|s" (h – часы, m – минуты, s – секунды).
# Написать функцию stat, которая возвращает строку в формате "Range: hh|mm|ss Average: hh|mm|ss"
# (range – разница между максимальным и минимальным значением, average – среднее значение)
#
# Пример:
# stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17") ==> "Range: 00|47|18 Average: 01|35|15"



import traceback
def stat(times):
    # Split the times string into a list of individual time strings
    time_list = times.split(", ")
    # Convert each time string to a number of seconds
    time_in_seconds = [int(t.split("|")[0])*3600 + int(t.split("|")[1])*60 + int(t.split("|")[2]) for t in time_list]
    # Calculate the range and average time in seconds
    time_range = max(time_in_seconds) - min(time_in_seconds)
    time_average = sum(time_in_seconds) / len(time_in_seconds)
    def sectotime(secs): 
        hours = secs // 3600 
        mins = (secs  % 3600) // 60 
        secs = secs % 60 
        formnum = "{:02d}|{:02d}|{:02d}".format(int(hours), int(mins), int(secs))
        return formnum 
    return "Range: "+sectotime(time_range)+" Average: "+sectotime(time_average)

#! Тесты
try:
    assert stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17") == "Range: 01|01|18 Average: 01|38|05"
    assert stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41") == \
        "Range: 00|31|17 Average: 02|26|18"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")







#!==================================================================================
    # a= divmod(time_range, 60*60)
    # print (a)
    # divmod() #! will bring the div and quotient 
    # Convert the range and average time back to hh|mm|ss format
    # h = divmod(time_range, 60*60)
    # m = divmod(time_range, 60)
    # print (m)
    # s = divmod()
    # range_str = "{:02d}|{:02d}|{:02d}".format(*divmod(time_range, 60*60), *divmod(time_range % (60*60), 60))
    # average_str = "{:02d}|{:02d}|{:02d}".format(*divmod(int(time_average), 60*60), *divmod(int(time_average) % (60*60), 60))
    # print (range_str)
    # print (average_str)
    # Return the result string
    # return f"Range: {range_str} Average: {average_str}"
# print (stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))
#!==============================================================
