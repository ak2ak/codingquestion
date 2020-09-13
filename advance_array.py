def can_reach_end(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1
    i = 0
    while i <= furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index


def count_minimum_step(arr):
    furthest_reach_so_far, last_index = 0, len(arr)
    i = 0
    count = 0
    while i <= furthest_reach_so_far < last_index:
        temp = furthest_reach_so_far
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        if temp != furthest_reach_so_far:
            count += 1
        i += 1
    return count if furthest_reach_so_far >= last_index else -1


print(can_reach_end([3, 2, 0, 0, 2, 0, 1]))
print(count_minimum_step([3, 3, 1, 0, 2, 0, 1]))
print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))
