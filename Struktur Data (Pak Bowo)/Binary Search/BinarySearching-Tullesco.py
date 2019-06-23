pos = 0


def search(list, n):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                low = mid + 1
            else:
                high = mid - 1

    return False


list = [1, 2, 6, 8, 9, 16, 23, 36, 40]
n = 6

if search(list, n):
    print("Found at indeks: ", pos + 1)
else:
    print("Not Found")
