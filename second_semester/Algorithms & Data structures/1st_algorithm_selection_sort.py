# import random
# import time
# # Selection sort in Python
# # time complexity O(n*n)
# #sorting by finding min_index
# def selectionSort(array, size):
#     changed = 0
#     for ind in range(size):
#         min_index = ind
#         for j in range(ind + 1, size):
#         # select the minimum element in every iteration
#             if array[j] < array[min_index]:
#                 min_index = j
#                 changed +=1
#             # swapping the elements to sort the array
#         (array[ind], array[min_index]) = (array[min_index], array[ind])
#         changed += 1
#     print ("count : ", changed )







# a = int (input("Input your size: "))
# arr = [random.randint(0, 100) for i in range (a)]
# size = len(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)
# # time complexity O(n2).



# start_time = time.time()
# print("-— %s seconds —-" % (time.time() - start_time))



