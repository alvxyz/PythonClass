#9-1-2019
#Program untuk mengetahui jenis error

# angka = 91
#
# try:
#     print(angka / 0)
# except Exception as err:
#     print("Maaf proses perhitungan gagal karena: ", err)
# except ValueError as err:
#     print("Proses perhitungan gagal karena: ", err)

# try:
#     angka_pertama = int(input("Masukkan nilai angka pertama: "))
#     angka_kedua = int(input("Masukan nilai angka kedua: "))
#     hasil = angka + angka_kedua
#
# except NameError as err:
#     print("Proses perhitungan gagal karena: ", err)
#
try:
    print("12" / 2)
except TypeError as err:
    print("Proses perhitungan gagal karena: ", err)