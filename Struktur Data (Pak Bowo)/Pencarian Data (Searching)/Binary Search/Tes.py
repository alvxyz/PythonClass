# data = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]
data = [1, 3, 4, 6, 9, 10, 11, 12]

# data.sort()
print(data)

ketemu = False
left = 0
right = len(data) - 1
key = 12
perulangan = 0
middle = 0

while left <= right and not ketemu:
    middle = (left + right) // 2

    if data[middle] == key:
        ketemu = True
    elif key < data[middle]:
        right = middle - 1
    else:
        left = middle + 1

    perulangan += 1

print("Jumlah Perulangan: ", perulangan)

if ketemu is True:
    print("Data", key, "ditemukan di indeks", middle)
else:
    print("Data tidak ditemukan")
