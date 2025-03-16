def power(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def mod_inverse(a, m):
    return power(a, m - 2, m)

def solve():
    a, n, m = map(int, input().split())

    if a == 1:
        print(n % m)
        return

    if (a - 1) % m == 0:
        result = 0
        current_power = a % m
        for i in range(n):
            result = (result + current_power) % m
            current_power = (current_power * a) % m
        print(result)
        return
    an = power(a, n, m)
    nume = (a * (an - 1)) % m
    denom = mod_inverse(a - 1, m)
    result = (nume * denom) % m

    print(result)

T = int(input())
for i in range(T):
    solve()