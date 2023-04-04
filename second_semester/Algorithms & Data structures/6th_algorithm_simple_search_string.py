#6th practical work
def simple_search(text, target):
    """
    Searches for the first occurrence of pattern in text using the simple searching algorithm.
    Returns the index where the pattern starts or -1 if the pattern is not found.
    """
    n = len(text)
    m = len(target)
    counter = 0 
    for i in range(n - m + 1):
        j = 0
        while j < m and target[j] == text[i + j]:
            j += 1
            counter += 1
        if j == m:
            return print("text found in index: ", i), print("number of comparisons:", counter)
    return print ("text not found in string"), print("number of comparisons:", counter), -1
# with open('practical6th.txt.txt', encoding='utf-8') as f:
#     lst = [i for i in f.read().split()]
# print(lst)
# text = input("enter your text: ")
text = open ('practical6th.txt', 'r')
txtsring = text.read() 
print (txtsring)
print ('Length of text: ',len(txtsring))
target   = input("enter your target: ")
print ('Length of target: ',len(target))
simple_search (txtsring, target)