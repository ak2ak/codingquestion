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


def binary_search_wrapper(arr, element):
    return binary_search(arr, element, 0, len(arr) - 1)


print(binary_search_wrapper(arr=[1, 34, 54, 129, 299], element=1))
