# a = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]
a = [int(s) for s in input("Masukan angka dipisah dengan 'Spasi' : ").split()]

semua = len(a)
NilaiTerbesar = max(a)
print("Nilai max: ", NilaiTerbesar)
print("Jumlah: ", a.count(NilaiTerbesar))

NilaiTerkecil = min(a)
print("Nilai Min: ", NilaiTerkecil)
b = []

for indeks in range(0, len(a)):
    if a[indeks] == NilaiTerbesar:
        b.append(indeks)

print("indeks: ", b)

print("=" * 100)
print("====Sebelum data diurutkan====")
print(a)
# array[0], array[1] = array[1], array[0]
# print(array)
proses = 0
jumlah = 0
pertukaran = 0

for indeks in range(len(a) - 1, -1, -1):
    print(indeks)
    swapped = False
    for indeks2 in range(0, indeks):
        # print(indeks2)
        if a[indeks2] > a[indeks2 + 1]:
            a[indeks2], a[indeks2 + 1] = a[indeks2 + 1], a[indeks2]
            swapped = True
            pertukaran = pertukaran + 1
        jumlah = jumlah + 1
        # print(a)
    print("#", proses + 1, a)
    if swapped == False:
        break
    proses = proses + 1

print()
print("====Setelah data diurutkan====")
print(a)
print(pertukaran)

print("=" * 100)
