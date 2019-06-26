# 24 Juni 2019

A = [1, 3, 5, 7, 9, 11, 13, 15]

key = 11

L = 0
R = len(A) - 1
perulangan = 0

ketemu = False

while L <= R and not ketemu:
    perulangan += 1
    m = (L + R) // 2
    if A[m] == key:
        ketemu = True
    else:
        if key < A[m]:
            R = m - 1
        else:
            L = m + 1

if ketemu is True:
    print("Maka data", key, "ada di indeks", m)
else:
    print("Data tidak ditemukan")


print("Jumlah perulangan: ", perulangan)
