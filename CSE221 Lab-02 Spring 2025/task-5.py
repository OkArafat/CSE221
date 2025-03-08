import sys
def choto(arr,zero):
    bam, dan= 0, len(arr)
    while bam < dan:
        mid = (bam + dan) // 2
        if arr[mid] < zero:
            bam = mid + 1
        else:
            dan = mid
    return bam
def boro(arr,zero):
    bam, dan = 0, len(arr)
    while bam< dan:
        mid = (bam+dan)//2
        if arr[mid]<=zero:
            bam = mid + 1
        else:
            dan = mid
    return bam
def new_count(k,p, arr, question):
    results = []
    for x, y in question:
        bamidx = choto(arr, x)
        danidx = boro(arr, y)
        results.append(str(danidx - bamidx))
        
    print("\n".join(results))
k,p = map(int, input().split())
arr = list(map(int, input().split()))
question = []
for j in range(p):
    x, y = map(int, input().split())
    question.append((x, y))
new_count(k,p, arr,question)
