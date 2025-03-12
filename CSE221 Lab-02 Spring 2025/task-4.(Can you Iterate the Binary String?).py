import sys
def a_function(vumi, x, y):
    result = 1
    while x > 0:
        if x % 2 == 1:
            result = (result * vumi) % y
        vumi = (vumi * vumi) % y
        x //= 2
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

ok = int(input()) 
results = []  

for i in range(ok):
    values = input().split()  
    a = int(values[0])  
    n = int(values[1])
    m = int(values[2])
    result = solve(a, n, m)  
    results.append(result)  

for res in results:
    print(res)
