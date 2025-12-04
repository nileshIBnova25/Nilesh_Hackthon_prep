
a=[19,11,8,5,3,2,1]  #Input

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False                                 #intilazing swapped as false
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:                     # if  value of j is greter than j-1 then j=j-1 & j-1=j
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True                          # if swapped then assigning true to swapped

        if not swapped:                                 # if swapped is not true the break
            break
    return arr
result=bubble_sort(a)
print(result) # Output [1,2,3,5,8,11,19]


