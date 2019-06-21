baris = 3
kolom  = 2

a = [0] * baris
print(a)

# for i in range(0, len(a)):
#


print("="*100)
# cara kedua dengan append

baris = 3
kolom = 2

a = []

for i in range(baris):
    a.append([0] * kolom)

print(a)

a[0][0] = 1
print(a)

print("="*100)

# cara insialisai ke 3 menggunakan list komperhension

baris = 3
kolom = 2

a = [[0] * kolom for i in range(baris)]
print(a)

# jika ingin merubahnya hanya dengan cara
a[0][0] = 1
print("Nilai a di baris 0 dan kolom 0 diubah menjadi = 1")
print(a)

# cara menginputkan nilai pada array 2 dimensi
baris = int(input("Masukan jumlah baris: "))

a = [[int(s) for s in input("Masukan nilai array per baris: ").split()]
     for i in range(baris)]
