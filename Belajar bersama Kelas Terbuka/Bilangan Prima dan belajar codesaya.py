

# tentukan batas bilangan prima yang akan dicari
Angka = 100
#
# # perulangan untuk mengecek bilangan prima
# for num in range(2, Angka):
#     prima = True
#     for i in range(2, num):
#         if (num % i == 0):
#             prima = False
#     if prima:
#         print(num)


def hitung_tagihan(uang_muka):
    harga_laptop = 7000
    sisa_cicilan = harga_laptop - uang_muka
    suku_bunga = 10  # dalam persen
    jumlah_bunga = sisa_cicilan * suku_bunga / 100
    total_tagihan = sisa_cicilan + jumlah_bunga
    tagihan_bulanan = total_tagihan / 12
    return tagihan_bulanan


print (hitung_tagihan(1000))

angka_minus = -3.14

angka_positif = abs(-3.14)

print (angka_minus)
print (angka_positif)
from random import randint

hitung_kepala = 0
hitung_total = 0

while True:

    # angka integer acak: 0 atau 1
    putar = randint(0, 1)

    if putar:
        hitung_kepala = hitung_kepala + 1
        print
        str(hitung_total) + " kepala " + str(hitung_kepala)
    else:
        hitung_kepala = 0
        print
        str(hitung_total) + " buntut"

    hitung_total = hitung_total + 1

    if not (hitung_kepala < 3 and hitung_total < 100):
        break

print
"Muncul kepala " + str(hitung_kepala) + " kali berturut-turut."
# anda sudah bisa menggunakan for dengan range()
for i in range(1000, 1, -200):
  print i

# sudah bisa juga untuk mencetak sebuah list
for p in [ 2, 3, 5, 7 ]:
  print p

# termasuk mencetak string
for s in "string":
  print s

# dictionary juga
dict = { 'nama' : 'saya', 'umur': 17 }
for d in dict:
  print d + ": " + str(dict[d])