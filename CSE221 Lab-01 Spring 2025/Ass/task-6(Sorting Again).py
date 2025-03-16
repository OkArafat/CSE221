# Suppose you are given a task to rank the students. You have gotten the marks and ID of the students. Now your task is to rank the students based on their marks using a sorting algorithm. If two or more students get the same mark, then students with the lower ID will get prioritized. See the input and output for a better understanding.

# However, you have to keep in mind that your sorting algorithms perform the minimum number of swapping operations.

# Input
# The first line of the input file will contain an integer 𝑁(1≤𝑁≤1000)
# . The second line will contain 𝑁
#  integers, representing the Student ID, 𝑆𝑖(1≤𝑆𝑖≤1000)
# . The next line will contain the 𝑁
#  integers, 𝑆𝑚(1≤𝑆𝑚≤1000)
# , which denotes the obtained mark of the corresponding students.

# Note: It is guaranteed that the student IDs are unique. In other words, 𝑆𝑖≠𝑆𝑗
#  if 𝑖≠𝑗
# .

# Output
# The first line of the output must contain a number 𝑋
#  which denotes the number of minimum swaps. The rest of the 𝑁
#  lines will contain the Student ID and obtained marks sorted based on the instruction above. See the sample output for a better understanding.

# Important Note: Since you are asked to minimize the number of swaps, if your number of swaps doesn't match with the judge's answer, your solution will be considered incorrect.

# Look at the first sample input. It can be shown that this can be sorted with only 4
#  swaps. It can also be shown that it is not possible to sort this in less than 4
#  swaps.


def selectionswaps(n, student_ids, student_marks):
    students = []
    for i in range(n):
        students.append((student_ids[i], student_marks[i]))  

    count = 0
    for i in range(n - 1):
        max_idx = i
        for y in range(i + 1, n):
            if students[y][1] > students[max_idx][1]:
                max_idx = y  
            elif students[y][1] == students[max_idx][1]: 
                if students[y][0] < students[max_idx][0]:
                    max_idx = y  

        
        if max_idx != i:
            temp_1 = students[i]
            students[i] = students[max_idx]
            students[max_idx] = temp_1
            count += 1

    print("Minimum swaps:", count)
    for i in range(n):
        print("ID:", students[i][0], "Mark:", students[i][1])
n = int(input())
student_ids = [int(x) for x in input().split()]
student_marks = [int(x) for x in input().split()]

selectionswaps(n, student_ids, student_marks)
