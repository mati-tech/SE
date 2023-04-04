import time 
import numpy as np 

def merge_sort(arr): 
    swaps = 0 
    comp = 0 
    
    if  len (arr)> 1: 
        mid = len(arr)//2 
        left = arr[:mid]
        right = arr[mid:]

        swap_left, comp_left = merge_sort(left)
        swap_right, comp_right = merge_sort(right)
        swaps += swap_left + swap_right
        comp += comp_left + comp_right
        
        i = j = k = 0 
        
        while i < len(left) and j < len(right) : 
            comp += 1
            if left[i] < right [j] : 
                arr[k] = left[i] 
                i +=1
            else : 
                arr [k] = right [j] 
                j+=1 
                swaps += 1 
            k+= 1 
        while i < len(left) : 
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right) :
            arr[k] = right[j]
            j += 1
            k += 1
            swaps += 1
    return swaps, comp

size = int(input('Enter the size of the array: '))
arr = [np.random.randint(0, 100) for i in range(size)]

start = time.time() 
swaps, comp = merge_sort(arr) 
end = time.time()

print ("Sorted array: ", arr)
print ("Time taken: ", end - start)
print ("Number of swaps: ", swaps )
print ("Number of comps: ", comp)

