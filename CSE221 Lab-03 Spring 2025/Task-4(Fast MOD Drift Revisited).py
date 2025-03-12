def mod_exp(base, exp, mod):
    foll = 1
    while exp > 0:
        if exp % 2 == 1:
            foll = (foll * base) % mod
        base = (base * base) % mod
        exp //= 2
    return foll

def solve():
    OTT = int(input()) 
    for z in range(OTT):
        a, n, m = map(int, input().split())
        if a == 1:
            print(n % m)
        else:
           
            totalfol = 0
            current_power = a % m
            for i in range(1, n + 1):
                totalfol = (totalfol + current_power) % m
                current_power = (current_power * a) % m
            print(totalfol)

solve()
