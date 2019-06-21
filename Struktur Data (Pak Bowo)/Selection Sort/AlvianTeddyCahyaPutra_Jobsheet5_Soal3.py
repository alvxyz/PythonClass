# mencari angka terkecil di dalam list
# ...0..1...2..3..4..5..6..7..8..9
data = [3, 10, 4, 6, 8, 9, 7, 2, 1, 5]
print("=====Data sebelum diurutkan=====")
print(data)
print()
# print(len(a)-1)

for proses in range(0, len(data) - 1):
    # print(proses)
    terkecil = proses  # inisialisasi nilai awal
    for indeks in range(proses + 1, len(data)):
        if data[indeks] < data[terkecil]:
            terkecil = indeks
    data[proses], data[terkecil] = data[terkecil], data[proses]

print("=====Data setelah diurutkan=====")
print(data)

# terkecil = 0  # inisialisasi nilai awal
# for indeks in range(1, len(a)):
#     if a[indeks] < a[terkecil]:
#         terkecil = indeks
# a[0], a[terkecil] = a[terkecil], a[0]
# print(a)
# print()
#
# print(a)
# terkecil = 1  # inisialisasi nilai awal
# for indeks in range(2, len(a)):
#     if a[indeks] < a[terkecil]:
#         terkecil = indeks
# a[1], a[terkecil] = a[terkecil], a[1]
# print(a)
# print()
#
# print(a)
# terkecil = 2  # inisialisasi nilai awal
# for indeks in range(3, len(a)):
#     if a[indeks] < a[terkecil]:
#         terkecil = indeks
# a[2], a[terkecil] = a[terkecil], a[2]
# print(a)
# print()