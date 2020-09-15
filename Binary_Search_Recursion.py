def binary_search(arr, element, lower, upper):
    if lower > upper:
        return -1
    else:
        middle = (lower + upper) // 2

        if element == arr[middle]:
            return middle
        elif element < arr[middle]:
            return binary_search(arr, element, lower, middle-1)
        else:
            return binary_search(arr, element, middle + 1, upper)


def binary_search_wrapper(a, x):
    return binary_search(a, x, 0, len(a) - 1)


print(binary_search_wrapper([1, 34, 54, 129, 299], 345))
