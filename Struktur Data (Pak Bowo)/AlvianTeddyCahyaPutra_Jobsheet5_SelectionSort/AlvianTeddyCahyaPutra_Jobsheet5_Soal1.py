# mencari angka terkecil di dalam list
# ...0..1...2..3..4..5..6..7..8..9
a = [3, 10, 4, 6, 8, 9, 7, 2, 1, 5]

terkecil = 0  # inisialisasi nilai awal
for indeks in range(1, len(a)):
    if a[indeks] < a[terkecil]:  # akan berubah setiap perulangan, setiap kali perulangan hingga mendapatkan angka terkecil
        terkecil = indeks
        # print(indeks)

print("Angka terkecil adalah", a[terkecil], "di indeks", terkecil)
