A = [int(s) for s in input("Masukkan Data (Pisah dengan Spasi): ").split()]
i = 0
ketemu = False
key = int(input("Masukkan key ingin dicari: "))
perbandingan = 0

# Mengurutkan data
A.sort()

# pecarian
while not ketemu and (i < len(A)):

    perbandingan += 1

    if A[i] == key:
        ketemu = True
    elif A[i] > key:
        break
    else:
        i += 1
        # i = i + 1

print("Jumlah perbandingannya : ", perbandingan)

if ketemu:
    print("Angka", key, "ditemukan di indeks ", + i)
else:
    print("!!!ALERT!!! \n404 Fot Found!!!")
    print("Keyword tidak ditemukan !!!")
