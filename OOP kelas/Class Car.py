# 23-1-2019 Tugas kelompok membuat Class dan isinya berdasarkan prinsip Iheritance dan Polymorphisme

class Car:
    tipe = "Kendaraan darat"
    def __init__(self, jenis, penumpang, warna, merk, kecepatan):
        jenis.self = jenis
        penumpang.self = penumpang
        warna.self = warna
        merk.self = merk
        kecepatan.self = kecepatan
    def cek_data_mobil(self):\
        print("Mobil ini berjenis", self.jenis, "Memiliki Kecepatan", self.kecepatan, "Km/jam dan dapat memuat", self.penumpang)

class MobilSport(Car):
    def berjalan(self):
        if jenis == "ferarri":
            print("Mobil ini memiliki kecepatan maksimal 340Km/jam")
        elif jenis == "bugati":
            print("Mobil ini memiliki kecepatan maksimal 400Km/jam")
        elif jenis == "lambo":
            print("Mobil ini memiliki kecepatan maksimal 356Km/jam")
        else:
            print("Mobil da")

