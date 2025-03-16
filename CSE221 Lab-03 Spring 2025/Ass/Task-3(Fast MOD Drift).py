import sys

def mod_exponentiation(a, b,mod):
    folafol = 1
    power = a %mod  
    while b > 0:
        if b % 2 == 1: 
            folafol = (folafol * power) %mod
        power = (power * power) %mod  
        b //= 2  
    return folafol
def main():
    input_line = sys.stdin.readline().strip().split()
    a = int(input_line[0])
    b = int(input_line[1])
    mod = 107

    folafol = mod_exponentiation(a, b,mod)
    sys.stdout.write(str(folafol) + "\n")
main()

