import sys
import operator as op

calculation={"+":op.add, "-":op.sub, "*":op.mul, "/":op.truediv}

t=int(sys.stdin.readline().strip())
for i in range(t):
    i,num1, op, num2 = sys.stdin.readline().strip().split()
    num1 = int(num1)
    num2 = int(num2)
    result = calculation[op](num1,num2)
    print(f"{result:.6f}")
  
