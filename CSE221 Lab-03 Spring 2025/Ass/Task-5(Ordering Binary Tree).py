import sys
n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
for i in range(n):
    arr[i] = int(arr[i])
folafol = []
ok = []  
ok.append((0, n - 1))  
indx = 0  
while indx < len(ok):
    left, right = ok[indx]
    indx += 1  
    if left > right:
        continue
    middle = (left + right) // 2
    folafol.append(arr[middle])
    ok.append((left, middle - 1))  
    ok.append((middle + 1, right))  
output = ''
for i in range(len(folafol)):
    output += str(folafol[i]) + ' '
sys.stdout.write(output.strip() + '\n')
