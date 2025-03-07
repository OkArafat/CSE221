def boro(arr, M):
    n = len(arr)
    First_sts = 0
    current_sum = 0
    boro_length = 0

    for i in range(n):
        current_sum += arr[i]

        while First_sts <= i and current_sum > M:
            current_sum -= arr[First_sts]
            First_sts = First_sts+ 1

        boro_length = max(boro_length, i - First_sts + 1)

    return boro_length

P , M = map(int, input().split())
arr = list(map(int, input().split()))
print(boro(arr, M))