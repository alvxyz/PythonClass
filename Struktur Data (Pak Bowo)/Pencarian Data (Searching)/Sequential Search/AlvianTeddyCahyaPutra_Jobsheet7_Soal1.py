A = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]
i = 0
ketemu = False
key = 5
perbandingan = 0

while not ketemu and (i < len(A)):
    perbandingan += 1
    if A[i] == key:
        ketemu = True
    else:
        i += 1

print("Jumlah perbandingannya : ", perbandingan)

if ketemu:
    print("Angka", key, "ditemukan di indeks ", + i)
else:
    print("!!!ALERT!!! \n404 Fot Found!!!")
    print("Keyword tidak ditemukan !!!")

# for i in range(len(A)):
#     perbandingan += 1
#     if A[i] == key:
#         ketemu = True
#         break

