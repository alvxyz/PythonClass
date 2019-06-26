a = [84, 89, 76, 86]

pivot = 0
proses = 0

for pivot in range(0, len(a)-1):  # exchange sort in action
    proses = proses + 1
    # print(proses, end=" ")
    for i in range(pivot + 1, len(a)):
        if a[i] < a[pivot]:
            a[i], a[pivot] = a[pivot], a[i]
            print(proses, end=" ")

print(a)
