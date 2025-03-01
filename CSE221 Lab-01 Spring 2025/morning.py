# Here is the code for Bubble Sort. Its runtime complexity is Θ(N²).
# Modify the code in such a way that its time complexity becomes Θ(N) in the best-case scenario.

# def solve(arr):
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr



def solve(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False 
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True 
        if not swapped:  
            break
    return arr
