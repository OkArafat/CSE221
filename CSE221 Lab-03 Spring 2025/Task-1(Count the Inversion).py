import sys

def merge(a, b):
    merged = []
    i = j = count = 0
    a_len, b_len = len(a), len(b)
    
    while i < a_len and j < b_len:
        if a[i] <= b[j]: 
            merged.append(a[i])
            i += 1
        else:  
            merged.append(b[j])
            count += a_len - i 
            j += 1
    merged.extend(a[i:])  
    merged.extend(b[j:])  
    
    return merged, count

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0  
    
    middle = len(arr) // 2
    a1, bam = mergeSort(arr[:middle])  
    a2, dan = mergeSort(arr[middle:])  
    merged, split_inv = merge(a1, a2)  
    total = bam + dan + split_inv
    return merged, total

N = int(sys.stdin.readline().strip())  
arr = list(map(int, sys.stdin.readline().strip().split()))

sorted_arr, inversion_count = mergeSort(arr)

sys.stdout.write(str(inversion_count) + "\n")
sys.stdout.write(" ".join(map(str, sorted_arr)) + "\n")
