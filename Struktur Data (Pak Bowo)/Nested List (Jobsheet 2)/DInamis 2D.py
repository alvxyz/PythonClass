jumlah_baris = int(input("Masukkan jumlah baris: "))

a = []

for i in range(jumlah_baris):
    a.append([int(s) for s in input("Masukan isi data pada kolom " +
                                    str(i + 1) + " = ").split()])


for baris in a:
    for element in baris:
        print(element, end=" ")
    print()
