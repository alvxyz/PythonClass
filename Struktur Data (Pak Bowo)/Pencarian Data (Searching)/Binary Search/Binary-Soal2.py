# 24 Juni 2019

A = [int(s) for s in input("Masukkan Data pisah dengan spasi: ").split()]
A.sort()

key = int(input("Masukkan key yang ingin dicari: "))

L = 0
R = len(A) - 1
perulangan = 0

ketemu = False

while L <= R and not ketemu:
    perulangan += 1
    middle = (L + R) // 2
    if A[middle] == key:
        ketemu = True
    else:
        if key < A[middle]:
            R = middle - 1
        else:
            L = middle + 1

if ketemu is True:
    print("Maka data", key, "ada di indeks", middle)
else:
    print("Data tidak ditemukan")

print("Jumlah perulangan: ", perulangan)
