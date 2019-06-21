a = [84, 89, 76, 86]

# proses 1
if a[1] < a[0]:
    a[1], a[0] = a[0], a[1]
if a[2] < a[0]:
    a[2], a[0] = a[0], a[2]
if a[3] < a[0]:
    a[3], a[0] = a[0], a[3]

# proses 2
if a[2] < a[1]:
    a[2], a[1] = a[1], a[2]

if a[3] < a[1]:
    a[3], a[1] = a[1], a[3]

# proses 3
if a[3] < a[2]:
    a[3], a[2] = a[2], a[3]


print(a)