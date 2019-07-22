data = [1, 3, 10, 12, 13]

i = 0
ketemu = False
key = 11
perulangan = 0

while i < len(data) and not ketemu:
    perulangan += 1
    if data[i] == key:
        ketemu = True
    elif data[i] > key:
        break
    else:
        i += 1

print("Jumlah perulangan: ", perulangan)
if ketemu is True:
    print("Data ditemukan di indeks", i)
else:
    print("Data tidak ditemukan")
