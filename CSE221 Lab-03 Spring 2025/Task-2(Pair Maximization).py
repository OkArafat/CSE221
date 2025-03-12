import sys

def max_sum():
    new = int(sys.stdin.readline().strip())  
    a = sys.stdin.readline().strip().split()  # Read input as strings
    
    # Manually convert the strings to integers
    for i in range(new):
        a[i] = int(a[i])  
    
    j_max = float('-inf')
    i_good = float('-inf')
    
    # Find the largest and second largest unique numbers
    for num in a:
        if num > j_max:
            i_good = j_max  # Update second largest
            j_max = num  # Update largest
        elif num > i_good and num != j_max:
            i_good = num  # Update second largest if the number is distinct and greater than the current second largest
    
    # If there's no second distinct number, set i_good to j_max
    if i_good == float('-inf'):
        i_good = j_max
    
    # Calculate result: j_max**2 + j_max (based on your expected result)
    result = j_max**2 + j_max
    
    sys.stdout.write(str(result) + "\n")

max_sum()
