# soal pertama

a = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]

NilaiTerbesar = max(a)
print("Nilai max: ", NilaiTerbesar)
print("Jumlah: ", a.count(NilaiTerbesar))

b = []

for indeks in range(0, len(a)):
    if a[indeks] == NilaiTerbesar:
        b.append(indeks)

print("indeks: ", b)

# print(indeks, end=" ")
# print(a[indeks], end=" ")
