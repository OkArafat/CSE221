import sys
def a_function(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def b_finction(a, m):
    return a_function(a, m-2, m) if a != 0 else 1

def solve(a, n, m):
    if a == 1:
        return n % m
    numerator = (a_function(a, n+1, m) - a) % m
    denominator = (a - 1) % m
    denominator_inv = b_finction(denominator, m)
    return (numerator * denominator_inv) % m

T = int(input()) 
results = []  

for i in range(T):
    values = input().split()  
    a = int(values[0])  
    n = int(values[1])
    m = int(values[2])
    result = solve(a, n, m)  
    results.append(result)  

for res in results:
    print(res)
