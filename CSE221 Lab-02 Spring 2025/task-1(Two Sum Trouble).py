import sys
import operator

def two_sum():

    prothome = sys.stdin.readline().split()
    n = int(prothome[0]) 
    s = int(prothome[1]) 
    
    dritriyo = sys.stdin.readline().split()
    arr = [int(num) for num in dritriyo]

    left=0
    right=n-1
    while left<right:
        curr_sum=arr[left]+arr[right]
        if curr_sum==s:
            print(left+1,right+1)
            return
        elif curr_sum<s:
            left+=1
        else:
            right-=1
    print(-1)
two_sum()
