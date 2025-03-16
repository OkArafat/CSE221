# your friend is trying to solve the following problem. You are given 𝐓
#  test cases. For each test case, you are given an integer 𝐍
# . You have to find out the summation of 1 to N. More formally, your friend has to calcuate
# ∑𝑥=1𝑥=𝑁𝑥

# Your friend wrote the following Python code to solve it:

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     sum = 0
#     for i in range(1, N + 1):
#         sum += i
#     print(sum)
# However, the code is not passing the online judge due to some unknown errors for large values of N.

# Since you are currently studying CSE221 and have learned about time complexity, help your friend come up with a more efficient solution.

# Input
# The first line contains a single integer T (1≤𝑇≤104)
#  — the number of test cases.

# The next T lines each contain a single integer N (1≤𝑁≤106)
# .

# Output
# For each test case, print a single integer — the summation from 1 to N.







t=int(input())
for i in range(t):
    p=int(input())
    a=p*(p + 1)
    d=a//2
    print(d)
