data = [12, 15, 7, 10, 25, 5, 20]
indeks = []
key = 5
found = False
pos = 0

for i in range(0, len(data)):
    if data[i] == key:
        found = True
        pos = i
        indeks.append(pos)

print("Data Sekarang")
print(data)
print()

if found is True:
    print("Data ditemukan pada indeks ", indeks)
else:
    print("data tidak ditemukan")
