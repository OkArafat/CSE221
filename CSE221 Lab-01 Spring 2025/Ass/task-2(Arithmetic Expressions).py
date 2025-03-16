# Can you solve Arithmetic Expressions?
# time limit per test1 second
# memory limit per test256 megabytes
# Can you solve arithmetic expressions with your programming knowledge? Let's find it out. You will be given some arithmetic expressions, and you have to solve them.

# Input
# The first line will contain a number 𝑇(1≤𝑇≤1000)
#  representing the number of test cases. Then for each test case, you will be given an arithmetic expression. Please see the sample input below. It is guaranteed that the numbers inside the arithmetic expression will be between 1
#  and 1000
# .

# Output
# For each test case, you have to print the result. Look at the sample output for reference.

# Important Note: Your answer might contain floating point numbers, and in that case, your answer doesn't have to be exactly equal to the actual answer. For example, if your answer is 20.250000001
#  and the judge's solution is 20.25
# , your answer will still be considered correct. As long as it is really close to the correct solution, your solution will be considered correct. Formally speaking, if your solution is 𝑥
# , and the judge's solution is 𝑦
# , then as long as |𝑥−𝑦|≤10−6
# , your solution will be correct. In the above example, your solution was 20.250000001
#  and the judge's solution was 20.25
# . If you take the difference of these two numbers, they are smaller than 10−6
# . Similarly, if the judge's solution is 19.0000000000
#  and your solution is 19
# , it is still correct, as the difference is 0
# , which is less than 10−6
# .



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