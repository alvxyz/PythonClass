data = [9, 6, 5, 4]

for i in range(len(data) - 1):
    proses = i + 1
    for j in range(i + 1, 0, -1):
        if data[proses] < data[j - 1]:
            data[proses], data[j - 1] = data[j - 1], data[proses]
            proses = j - 1

print(data)
