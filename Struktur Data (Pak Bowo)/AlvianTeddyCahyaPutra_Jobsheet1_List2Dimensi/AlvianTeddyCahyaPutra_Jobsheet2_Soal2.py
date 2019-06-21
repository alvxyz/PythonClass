# 18-03-2019

jml_baris = int(input("Masukan jumlah baris matriks: "))
a = []
for i in range(jml_baris):
    a.append([int(s) for s in input("Masukan elemen matriks A baris ke- " +
                                    str(i + 1) + "(pisahkan dengan spasi): ").split()])
    # split langsung menjadi ke list
    # join akan mengubah list ke string
print("Matriks A yang Anda masukan adalah: ")
for baris in a:
    for element in baris:
        print("[", element, "]", end=" ")
    print()

# input matriks baru
b = []
for i in range(jml_baris):
    b.append([int(s) for s in input("Masukan elemen matriks B baris ke- " +
                                    str(i + 1) + "(pisahkan dengan spasi): ").split()])
    # split langsung menjadi ke list
    # join akan mengubah list ke string
print("Matriks B yang Anda masukan adalah: ")
for baris in b:
    for element in baris:
        print("[", element, "]", end=" ")
    print()

# hasil penjumlahan
for i_baris in range(len(a)):
    for i_kolom in range(0, len(a[0])):
        print(a[i_baris][i_kolom] + b[i_baris][i_kolom], end=" ")
    print()

# Syarat pemjumlahan matriks adalah baris dan kolom sama
