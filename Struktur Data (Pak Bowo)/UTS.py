# bubble sort

data = [9, 4, 2, 1]

for indeks in range(len(data) - 1, -1, -1):
    for indeks2 in range(0, indeks):
        if data[indeks2] > data[indeks2 + 1]:
            data[indeks2], data[indeks2 + 1] = data[indeks2 + 1], data[indeks2]

print(data)

# exchange sort

for pivot in range(0, len(data) - 1):
    for i in range(pivot + 1, len(data)):
        if data[i] < data[pivot]:
            data[i], data[pivot] = data[pivot], data[i]

print(data)

# selection sort


for proses in range(0, len(data) - 1):
    terkecil = proses
    for indeks in range(proses + 1, len(data)):
        if data[indeks] < data[terkecil]:
            terkecil = indeks
    data[proses], data[terkecil] = data[terkecil], data[proses]

# for proses in range(0, len(data) - 1):
#     terkecil = proses
#     for indeks in range(proses + 1, len(data)):
#         if data[indeks] < data[terkecil]:
#             terkecil = indeks
#     data[proses], data[terkecil] = data[terkecil], data[proses]

print(data)

# insertion sort

for i in range(0, len(data) - 1):
    proses = i + 1
    for j in range(i + 1, 0, -1):
        if data[proses] < data[j - 1]:
            data[proses], data[j - 1] = data[j - 1], data[proses]
            proses = j - 1

        # for i in range(0, len(data) - 1):
#     proses = i + 1
#     for j in range(i + 1, 0, -1):
#         if data[proses] < data[j - 1]:
#             data[proses], data[j - 1] = data[j - 1], data[proses]
#             proses = j - 1

print(data)
