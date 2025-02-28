import sys
N, K = sys.stdin.readline().strip().split()
N = int(N)
K = int(K)
arr = sys.stdin.readline().strip().split()
arr = [int(num) for num in arr]
reversed_part = arr[:K][::-1]
print(" ".join(map(str, reversed_part)))