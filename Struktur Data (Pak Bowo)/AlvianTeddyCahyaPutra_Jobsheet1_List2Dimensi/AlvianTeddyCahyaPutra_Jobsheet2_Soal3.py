# 18-03-2019

jml_baris1 = int(input("Masukkan jumlah baris array ke-1:"))
jml_baris2 = int(input("Masukkan jumlah baris array ke-2:"))

a = []
b = []
c = []

for i in range(jml_baris1):
    a.append([int(s) for s in
              input("Masukkan elemen array ke-1 baris ke-" + str(i + 1) + " (pisahkan dengan spasi): ").split()])

print()

for i in range(jml_baris2):
    b.append([int(s) for s in
              input("Masukkan elemen array ke-2 baris ke-" + str(i + 1) + " (pisahkan dengan spasi): ").split()])

print("Array yang anda masukkan adalah : ")
for baris in a:
    for element in baris:
        print(element, end=" ")
    print()

print()

print("Array yang anda masukkan adalah : ")
for baris in b:
    for element in baris:
        print(element, end=" ")
    print()

for i in range(0, jml_baris1):
    c.append([0] * len(a))

print()
print()

# print(a[0])
# print(len(a))
for i in range(0, jml_baris1):
    for j in range(0, len(a)):
        for k in range(0, len(a[0])):
            c[i][j] += a[i][k] * b[k][j]

print(c)
