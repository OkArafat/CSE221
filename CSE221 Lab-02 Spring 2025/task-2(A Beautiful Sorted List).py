import sys
def merge_sorted_lists():
    n = int(sys.stdin.readline().strip())
    alice_list = sys.stdin.readline().strip().split()
    for i in range(n):
        alice_list[i] = int(alice_list[i]) 

    m = int(sys.stdin.readline().strip())

    bob_list = sys.stdin.readline().strip().split()
    for i in range(m):
        bob_list[i] = int(bob_list[i]) 
    i,j = 0, 0
    merged_list = []

    while i < n and j < m:
        if alice_list[i] <= bob_list[j]:
            merged_list.append(alice_list[i])
            i += 1
        else:
            merged_list.append(bob_list[j])
            j += 1

    while i < n:
        merged_list.append(alice_list[i])
        i += 1
    while j < m:
        merged_list.append(bob_list[j])
        j += 1

    sys.stdout.write(" ".join(str(x) for x in merged_list) + "\n")

merge_sorted_lists()
