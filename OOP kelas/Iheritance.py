# class
class Dog:
    # Menginisiasi Atribut
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna
    def cek_data(self):
        print("Nama", self.nama, "umur", self.umur, "warna", self.warna)

# Ini adalah class anak

class DogBesar(Dog):
    def makan(self):
        print("Makannya sangat banyak ui")
    def minum(self):
        print("Dia sangat suka minum pocari sweat")

class Pelatih(Dog):
    def pelatih1(self):
        print(dog2.nama, "dilatih oleh Ferguso")


dog1 = Dog("Inzagi", 12, "Red Pearl")
dog2 = DogBesar("Yougi", 11, "Juiliert Black")
pelatih = Pelatih("Ferguso", 76, "Putih Mutiara")

# Dog2 bisa mengakses method pada kelas dog karena mewarisi attr dan method kelas dog
dog2.cek_data()

# dog2 bisa mengakses method pada kelasnya sendiri
dog2.makan()
dog2.minum()

pelatih.pelatih1()
