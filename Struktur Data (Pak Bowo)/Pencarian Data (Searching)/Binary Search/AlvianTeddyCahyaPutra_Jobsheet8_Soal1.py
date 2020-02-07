# 24 Juni 2019

A = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]
A.sort()

print(A)
key = 25

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
    print("Data", key, "ada di indeks", middle)
else:
    print("Data tidak ditemukan")


print("Jumlah perulangan: ", perulangan)
