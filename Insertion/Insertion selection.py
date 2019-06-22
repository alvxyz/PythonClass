# 11-12-2018

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [825, 4, 3, 21, 42, 422, 491]

insertion_sort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")