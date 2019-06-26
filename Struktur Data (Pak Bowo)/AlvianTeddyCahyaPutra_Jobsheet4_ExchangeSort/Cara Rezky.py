a = [84, 89, 76, 86]

for indeks in (0, len(a)-1):
    for data in range(0, len(a)):
        if a[indeks] > a[data]:
            a[indeks], a[data] = a[data], a[indeks]
print(a)