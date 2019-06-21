# 17-01-2019, Kamis, Belajar OOP menggunakan Inisiasi hingga method

class Dog:
    # Menginisiasi Atribut
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna

# jomano = Dog("Jomano", 10, "Gold")
#
# print('{} is a Dog, and have {} years old, the color is {} '.format(jomano.nama, jomano.umur, jomano.warna))

# Menginisiasi method
    def lari(self):
        print("Lari dengan kencang")
    def melompat(self):
        print(Guguk.nama, " Meloncat dengan kekuatan super")

# Instantiate objek 'dog'
Guguk = Dog("Jono", 18, "Gold")
Guguk.nama = "Jono"

# Memanggil method
print('{} is a Dog, and have {} years old, the color is {} '.format(Guguk.nama, Guguk.umur, Guguk.warna))
Guguk.lari()
Guguk.melompat()