sebuah_list_klubSepakbola = ["Barcelona","Real Madrid", "Manchester United", "Manchester City", "Everton"]
sebuah_tuple = ("Indonesia","Belanda","Jerman","Jepang","Prancis")
sebuah_dictionary = {"Nama":"Alvian",
                     "Kelas":"A",
                     "Semester":1}
print(len(sebuah_list_klubSepakbola)) #digunakan untuk mengetahui jumlah seluruh anggora yang ada di dalam sebuah data

try:    #ini digunakan untuk mencoba kode
    print(sebuah_list_klubSepakbola[11])
except Exception as err: #digunakan untuk mengecualikan dan as untuk mendefinisikan expect ke variabel
    print("Maaf Anda salah memasukan nomer Index, ini termasuk jenis error: ", err )

try:
    print(sebuah_tuple[12])
except IndexError as err:
    print("Maaf Anda salah memasukan nomer Index\n")

try:
    print(sebuah_dictionary["Alamat"])
except KeyError:
    print("Maaf Anda memasukan key yang salah, mohon memasukan yang ada di daftar")