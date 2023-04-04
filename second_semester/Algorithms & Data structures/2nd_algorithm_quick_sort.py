import random 
import time
count_ch = 0
# count_co= 0
def quicksort(arr) :
    global count_co, count_ch
    count_ch += 1
    if len (arr) <= 1:
        return arr
    else: 
        pivot = arr[0]
        # count_co += 1
        less = [x for x in arr[1:] if x <= pivot] 
        greater = [x for x in arr[1:] if x > pivot] 
        return quicksort(less) + [pivot] + quicksort(greater)

size = int (input("Enter the size of the array: "))
arr = [random.randint(0, 100) for i in range(size)]
print ("Before sorting: ",  arr) 
start_time = time.time()
arr = quicksort(arr) 
end_time = time.time()


print ("After sorting: ",  arr)
print ("Sorting Time: " , int(end_time - start_time))
print ("Substitutions: ",count_ch )
# print ("Comparing: ",count_co )
