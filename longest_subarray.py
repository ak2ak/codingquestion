def longest_sub_array(arr):
    count = 0
    temp = 1
    for i in range(1, len(arr)):
        if arr[i-1] <= arr[i]:
            temp += 1
        else:
            count = max(count, temp)
            temp = 1
    count = max(count, temp)
    return count


print(longest_sub_array([0, 5, 0, 20, 0, 10, 30, 0, 25, 20]))
