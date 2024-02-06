def str_len(string, count=0):
    """Function that calculates a lenght of a string"""
    if not string:
        return count
    else:
        return str_len(string[1:], count + 1)


def linear_search(li, x):
    if not li:
        return False
    elif li[0] == x:
        print(x)
    else:
        return linear_search(li[1:], x)


def count_instanse(li, val, count=0):
    if li:
        if li[0] == val:
            return count_instanse(li[1:], val, count + 1)
        return count_instanse(li[1:], val, count)
    return count


def duplicates(li):
    if li:
        if linear_search(li[1:], li[0]):
            return True
        return duplicates(li[1:])
    return False


def remove_duplicates(li):
    if not li:
        return []

    if linear_search(li[1:], li[0]):
        return [] + remove_duplicates(li[1:])
    else:
        return [li[0]] + remove_duplicates(li[1:])


def remove_duplicates_2(li2):
    if not li2:
        return []

    result = remove_duplicates(li2[1:])

    if li2[0] not in result:
        return [result[0]] + li2
    return result


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

def prefix(prefix, a_str):
    pass


def is_substring(sub, a_Str):
    pass


def main():
    lis = [1, 1, 2, 5, 3, 5, 6]  # 1,2,3,5,6
    print(remove_duplicates_2(lis))


if __name__ == "__main__":
    main()
