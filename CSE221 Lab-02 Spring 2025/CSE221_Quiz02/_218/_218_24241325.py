# 24241325 0
# CSE-9E-22L-L5 22299005
import sys
def solve(list1, list2):
    N = len(list1)
    M = len(list2)
    res = []
   
    # Place your code here
    
    while N< len(list1) and  M < len(list2):
        if list1[N] <=list2[M]:
            res.append(list1[N])
            N+=1

        else:
            res.append(list2[M])
            M+=1

    while N<len(list1) :
        res.append(list1[N])
        N+=1

    while M<len(list2):
        res.append(list2[M])
        M+=1   
    
    return res

