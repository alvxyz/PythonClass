data = [int(s) for s in input("Masukkan data (pisah dengan spasi): ").split()]

for i in range(0, len(data) - 1):
    proses = i + 1
    for j in range(i + 1, 0, -1):
        # print(j)
        if data[proses] < data[j - 1]:
            data[proses], data[j - 1] = data[j - 1], data[proses]
            proses = j - 1


print("Data yang telah diurutkan dengan Insertion Sort")
print(data)


