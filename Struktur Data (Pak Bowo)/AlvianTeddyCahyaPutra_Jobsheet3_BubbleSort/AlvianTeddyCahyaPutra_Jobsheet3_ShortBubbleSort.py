a = [40, 30, 50, 60]
loop_count = 0

swapped = True

for i in range(1, len(a)):
    swapped = False
    for indeks in range(len(a) - i):
        loop_count += 1
        if a[indeks] > a[indeks + 1]:
            a[indeks], a[indeks + 1] = a[indeks + 1], a[indeks]
            swapped = True

    if swapped is False:
        break

print(a)
print("Jumlah perulangannya:", loop_count)
proses = len(a) - 1
print("Jumlah proses yang terjadi:", proses)
# while proses > 0:
