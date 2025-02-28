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
