a = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]

NilaiTerbesar = max(a)
print("Nilai max: ", NilaiTerbesar)
print("Jumlah: ", a.count(NilaiTerbesar))

b = []

for indeks in range(0, len(a)):
    if a[indeks] == NilaiTerbesar:
        b.append(indeks)

print("indeks: ", b)

print("=" * 100)

x = a[0]
# print(array[0])
a[0] = a[1]
a[1] = x
# print(x)

print(a)

# array[0], array[1] = array[1], array[0]
# print(array)
