# data = [int(s) for s in input("Masukan angka dipisah dengan spasi : ").split()]
data = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]

for pivot in range(0, len(data) - 1):  # exchange sort in action
    for i in range(pivot + 1, len(data)):
        if data[i] < data[pivot]:
            data[i], data[pivot] = data[pivot], data[i]

print("Angka setelah di urutkan dengan exchange sort = ")
print(data)
