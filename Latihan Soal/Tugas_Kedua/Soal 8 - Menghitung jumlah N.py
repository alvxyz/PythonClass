print("PROGRAM UNTUK MENGHITUNG JUMLAH N")

nilai = int(input("Masukan Nilai N: "))

sum = 0

for i in range(1, nilai, 2):
    print(i, end=" ")
    sum = sum + i

print("Jumlah nilai keseluruhan adalah %s" % sum)