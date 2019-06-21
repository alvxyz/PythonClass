a = [20, 30, 40, 50, 60]

ada_pertukaran = True
proses = len(a)-1
loop_count = 0

while proses > 0 and ada_pertukaran:
    ada_pertukaran = False
    for indeks in range(0, proses):
        loop_count += 1
        if a[indeks + 1] > a[indeks]:
            ada_pertukaran = True
            a[indeks], a[indeks + 1] = a[indeks + 1], a[indeks]
    proses -= 1

print(a)
print("Jumlah perulangan= ", loop_count)