def solve(arr):
    def merge_sort_and_count(left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = merge_sort_and_count(left, mid) + merge_sort_and_count(mid + 1, right)
        
        # Count pairs (i, j) where arr[i] > 2 * arr[j]
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += (j - (mid + 1))

        # Merge step (sorting the merged range)
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= right:
            temp.append(arr[j])
            j += 1
        
        arr[left:right + 1] = temp
        
        return count

    return merge_sort_and_count(0, len(arr) - 1)

# Test cases
print(solve([4, 2, 1, 5, 3]))  # Output: 1
print(solve([1, 4, 3, 10]))    # Output: 0
print(solve([9, 6, 400000, 2, 12, 5, 300000, 7, 1, 15, 13]))  # Output: 19
print(solve([23, 11, 5, 2]))   # Output: 6
