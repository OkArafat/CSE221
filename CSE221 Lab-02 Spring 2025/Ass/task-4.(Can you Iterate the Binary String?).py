import sys
def mod_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def mod_inverse(a, m):
    return mod_exponentiation(a, m-2, m) if a != 0 else 1

def solve(a, n, m):
    if a == 1:
        return n % m
    numerator = (mod_exponentiation(a, n+1, m) - a) % m
    denominator = (a - 1) % m
    denominator_inv = mod_inverse(denominator, m)
    return (numerator * denominator_inv) % m

T = int(sys.stdin.readline().strip())
results = []
for _ in range(T):
    a, n, m = map(int, sys.stdin.readline().strip().split())
    results.append(str(solve(a, n, m)))

sys.stdout.write("\n".join(results) + "\n")
