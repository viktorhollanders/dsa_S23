def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid, x

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return 0


li = [1, 3, 11, 17, 23, 31, 45, 50, 105, 207]
x = 17  

res = binary_search(li, 0, len(li) - 1, x)
print(res)
