# Program untuk mengetahui tahun kabisat
# Input : tahun
# Output : tahun kabisat
# Author : Alvian

print("PROGRAM UNTUK MENGETAHUI TAHUN KABISAT")
tahun = int(input("Masukan tahun yang akan dicek [Berupa Angka] :"))

#Pengecekan tahun dengan rumus yang telah di buat
if (tahun % 4 != 0):
    print("Tahun yang Anda masukan adalah %s, Tahun ini Bukan Tahun Kabisat" % tahun)
elif (tahun % 100 == 0):
    print("Tahun yang Anda masukan adalah %s, Tahun ini Bukan Tahun Kabisat" % tahun)
else:
    print("Tahun yang Anda masukan adalah %s, Tahun ini merupakan Tahun Kabisat" % tahun)
