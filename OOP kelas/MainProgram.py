class Student:
    #menginisiasi atribut Umum
    type = "Human"
    #Menginisiasi atribut khusus
    def __init__(self, nama, campus, prodi):
        self.nama = nama
        self.campus = campus
        self.prodi = prodi

    # Menginisiasi Method
    def tipe_normal(self):
        print(nama, "adalah seorang yang normal")
    def tipe_wibu(self):
        print(nama, "adalah seorang yang suka Jejepangan")
    def tipe_kpop(self):
        print(nama, "adalah seorang yang menyukai K-pop")
    def berlari_cepat(self):
        print(nama, "adalah seorang yang sangat cepat")
    def berlari_lambat(self):
        print(nama, "adalah seorang yang lambat kayak SIPUTT")


# inisiasi objek
nama = input("Mahasiswa yang ingin anda ketahui: ")
campus = input("Masukan Kampusnya: ")
prodi = input("Masukan Prodi: ")

mahasiswa = Student(nama, campus, prodi)

# Percabangan untuk menentukan output
if nama == "lazuardi":
    print("{} adalah seorang Mahasiswa {}, Prodinya adalah {}".format(mahasiswa.nama, mahasiswa.campus, mahasiswa.prodi))

    mahasiswa.tipe_wibu()
    mahasiswa.berlari_cepat()

elif nama == "nabil":
    print(nama, "adalah seorang Mahasiswa", campus, "Prodinya adalah", prodi)
    mahasiswa.tipe_kpop()
    mahasiswa.berlari_lambat()

elif nama == "jordi":
    print(nama, "adalah seorang Mahasiswa", campus, "Prodinya adalah", prodi)
    mahasiswa.tipe_normal()
    mahasiswa.berlari_cepat()