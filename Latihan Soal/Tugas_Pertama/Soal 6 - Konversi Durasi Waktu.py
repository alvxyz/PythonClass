print("ALVIAN TEDDY CAHYA PUTRA 3201816023")
print("Konversi Jam ke Detik")

# menginput nilai
jam = int(input("Masukan jumlah jam : "))
menit = int(input("Masukan jumlah menit : "))
detik = int(input("Masukan jumlah detik : "))

# proses
hasil = (jam * 3600) + (menit * 60) + detik

# menampilkan hasil
print("%s : %s : %s adalah sama dengan %s detik" % (jam,menit,detik,hasil))