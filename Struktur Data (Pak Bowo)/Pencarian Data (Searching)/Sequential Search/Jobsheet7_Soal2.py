# data = [12, 15, 7, 10, 25, 5, 20]

data = [int(s) for s in input("Masukkan Data dipisah dengan spasi: ").split()]
data.sort()

indeks = []
key = int(input("Masukkan angka yang ingin dicari: "))
found = False
pos = 0
perbandingan = 0


for i in range(0, len(data)):
    perbandingan += 1
    if data[i] == key:
        found = True
        pos = i
        indeks.append(pos)


print()
print("Data Sekarang")
print(data)
print()

if found is True:
    print("Data ditemukan pada indeks ", indeks)
else:
    print("!!!ALERT!!! \n404 Fot Found!!!")
    print("Keyword tidak ditemukan !!!")

print("Jumlah perbandingannya : ", perbandingan)