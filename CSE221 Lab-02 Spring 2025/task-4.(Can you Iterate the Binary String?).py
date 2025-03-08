import sys
def prothom(ok):
    for i in range(len(ok)):
        if  ok[i] == '1':
            return i + 1  
    return -1
T = int(sys.stdin.readline().strip())
rest = []
for  i in range(T):
    ok = sys.stdin.readline().strip()
    rest.append(str(prothom(ok)))
sys.stdout.write("\n".join(rest) + "\n")
