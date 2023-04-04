from random import randint

def binary_search(lst, target):
    comparisons = 0
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if lst[mid] == target:
            print(f"Found {target} at index {mid}")
            break
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print("Not found!")
    print(f"Program made {comparisons} comparisons")

while True: 
    length = int(input("Enter length of list: "))
    lst = sorted([randint(1, 100) for _ in range(length)])
    print(f"Generated list: {lst}")
    target = int(input("Enter target number: "))
    binary_search(lst, target)
