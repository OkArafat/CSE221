import sys
import operator as op

calculation={"+":op.add,
             "-":op.sub,
             "*":op.mul, 
             "/":op.truediv}

t=int(sys.stdin.readline().strip())
for j in range(t):
    j,num_1, op, num_2 = sys.stdin.readline().strip().split()
    num_1 = int(num_1)
    num_2 = int(num_2)
    result = calculation[op](num_1,num_2)
    print(f"{result:.6f}")