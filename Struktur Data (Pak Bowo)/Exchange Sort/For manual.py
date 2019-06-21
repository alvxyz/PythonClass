a = [84, 89, 76, 86]

pivot = 0
for i in range(1, len(a)):
    if a[i] < a[pivot]:
        a[i], a[pivot] = a[pivot], a[i]

pivot = 1
for i in range(2, len(a)):
    if a[i] < a[pivot]:
        a[i], a[pivot] = a[pivot], a[i]

pivot = 2
for i in range(3, len(a)):
    if a[i] < a[pivot]:
        a[i], a[pivot] = a[pivot], a[i]


