class mahasiswa():
    jurusan = "Teknik Informatika"
    __nilai = 0 # Private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim # public

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def cek_nilai(self):
        if self.__nilai <= 50:
            print(self.nama, 'tidak lulus')
         else:
            print(self.nama, 'lulus lu yee')


# main program

aming = mahasiswa("See A Ming", 21393972772)
upnormal = mahasiswa("UP norm AL", 3333232323)

# panggil method

aming.uts(57)
aming.uas(81)

upnormal.uts(12)
upnormal.uas(11)

aming.cek_nilai()
upnormal.cek_nilai()

print(aming.jurusan)
print(upnormal.jurusan)

