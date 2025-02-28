def selection_sort_with_swaps(n, student_ids, student_marks):
    students = []
    for i in range(n):
        students.append((student_ids[i], student_marks[i]))  

    swap_count = 0
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if students[j][1] > students[max_idx][1]:
                max_idx = j  
            elif students[j][1] == students[max_idx][1]: 
                if students[j][0] < students[max_idx][0]:
                    max_idx = j  

        
        if max_idx != i:
            temp = students[i]
            students[i] = students[max_idx]
            students[max_idx] = temp
            swap_count += 1

    print("Minimum swaps:", swap_count)
    for i in range(n):
        print("ID:", students[i][0], "Mark:", students[i][1])
n = int(input())
student_ids = [int(x) for x in input().split()]
student_marks = [int(x) for x in input().split()]

selection_sort_with_swaps(n, student_ids, student_marks)
