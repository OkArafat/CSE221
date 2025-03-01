# Do you know how to tell if a number is Odd or Even? You are given 𝑇
#  numbers, and for each of those numbers, you have to tell whether the number is odd or even.

# Input
# The first line will contain a single integer 𝑇
#  (1≤𝑇≤100
# ). Each of the next 𝑇
#  lines will contain a number 𝑁
#  (−105≤𝑁≤105
# ).

# Output
# For each 𝑁
# , you have to print whether the number is odd or even. Please see the sample input-output format to know what exactly you have to print.

a=int(input())
for k in range(a):
  o=int(input())
  if o%2==0:
    print(f"{o} is an Even number.")
  else:
    print(f"{o} is an Odd number.")
