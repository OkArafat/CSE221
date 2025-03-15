# 24241325 0
# CSE-9E-22L-L6 22299005
def solve(arr):
    N = len(arr)
    pairs = -1
    marged=[]
    marge_pair=0
    # Place your code here
    def mergesort(arr):
        if len(arr) <=1:
            return pairs

        else:
            mid=len(arr)//2
            left,left_inv=mergesort(arr[:mid])
            right,right_inv=mergesort(arr[mid:])
            return left_inv + right_inv + marge_pair

    
    def merge(left,right):
        marge_pair=0
        i=j=paris=0
        while(i<len(left) and j < len(right)):
            if(left[i]<=2*right[j]):
                marged.append(left[i])
                marge_pair+=1
                i+=1
            elif(right[j]<left[i]):
                marged.append(right[j])
                j+=1

        marged.extend(left[i:])
        marged.extend(right[j:])
        return marged, marge_pair
        

    return pairs
