num_elements = int(input())  
reverse_count = int(input())
numbers = []
for num in range(num_elements):  
    value = int(input())  
    numbers.append(value)  
reversed_subset = []
for i in range(reverse_count - 1, -1, -1):  
    reversed_subset.append(numbers[i])
for value in reversed_subset:
    print(value, end=" ")
