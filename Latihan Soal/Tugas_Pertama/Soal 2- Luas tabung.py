print("ALVIAN TEDDY CAHYA PUTRA 3201816023")
print("Program Hitung Luas Tabung")

# menginputkan nilai jari-jari dan tinggi
jari_jari = float(input("Masukkan jari-jari: "))
tinggi = float(input("Masukan tinggi: "))

# proses
phi = 3.14
luas_tabung = 2 * phi * jari_jari * (jari_jari + tinggi)

# menampilkan hasil
print("Luas Tabung adalah: ", luas_tabung)