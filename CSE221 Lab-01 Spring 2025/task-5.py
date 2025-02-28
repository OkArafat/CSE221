def bubbleSort(arr, n):
    for i in range(n - 1):
        swapped = False 
        for j in range(n - i - 1):
            if j + 1 < len(arr) and arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped != True:  
            break
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
bubbleSort(arr, n)  
for num in arr:
    print(num, end=" ")
print()