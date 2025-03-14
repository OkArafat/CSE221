import sys

def sum():
    numbe = int(sys.stdin.readline().strip())
    inputnumbers = sys.stdin.readline().strip().split()
    new_num_1 = []
    for  numstr in inputnumbers:
        new_num_1.append(int(numstr))
    maxvalu = float('-inf')
    maxpfix = new_num_1[0]
    for j in range(1, numbe):
        maxvalu = max(maxvalu, maxpfix + new_num_1[j] ** 2)
        maxpfix = max(maxpfix, new_num_1[j])
    sys.stdout.write(str(maxvalu) + "\n")
sum()
