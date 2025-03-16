# You are given an array of N integers. Your task is to reverse the array and print the last K integers from the reversed array.

# Input
# The first line contains two integers N (1≤𝑁≤106)
#  and K (1≤𝐾≤𝑁)
#  — the number of elements in the array and the value K.

# The second line contains N integers separated by spaces 𝑎1,𝑎2,𝑎3…𝑎𝑛
#  (1≤𝑎𝑖≤106)
#  — the elements of the array.

# Output
# Print K space separated integers as described in the statement.



import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.reverse() 
print(*arr[-K:])