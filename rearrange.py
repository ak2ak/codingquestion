def rearrange(arr):
    for i in range(len(arr)):
        arr[i:i + 2] = sorted(arr[i:i+2], reverse=i % 2)
    return arr


print(rearrange([1,2,5,2,4,2]))