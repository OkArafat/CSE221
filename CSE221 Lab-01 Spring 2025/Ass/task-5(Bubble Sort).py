# Here is the code of bubble sort. Its run time complexity is 𝜃(𝑛2)
# . Change the code in a way so that its time complexity is 𝜃(𝑛)
#  for the best-case scenario. You are not allowed to use any builtin sort function to solve this problem.

# def bubbleSort(arr):                                                    
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1): 
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# Input
# In the first line, you will be given 𝑁
#  (1≤𝑁≤105
# ). Then you will be given an array 𝑎
#  of 𝑁
#  integers (1≤𝑎𝑖≤109
# ) that you have to sort in increasing order. It is guaranteed that if the original input array is not in the best case scenario, 1≤𝑁≤1000
# .

# Output
# Output the sorted array (Please see the sample output for reference)


import sys
def merge_sort(arr):
    if len(arr)> 1:
        mid=len(arr) // 2
        lefthalf= arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i =0 
        j = 0
        k = 0
        while i < len(lefthalf) and j< len(righthalf):
            if lefthalf[i]<righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1
        
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
merge_sort(arr)
sys.stdout.write(" ".join(map(str, arr)) + "\n")
