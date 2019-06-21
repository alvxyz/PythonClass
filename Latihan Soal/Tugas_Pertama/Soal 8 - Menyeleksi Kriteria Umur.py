print("ALVIAN TEDDY CAHYA PUTRA 3201816023")
print("Program untuk menyeleksi kriteria umur")

print("Kategori Umur")

# menginput usia
umur = int(input("Silahkan masukan usia anda : "))

#proses
if umur <= 5:
    hasil = "Balita"
elif 5 < umur <= 13:
    hasil = "Anak-anak"
elif 13 < umur <= 25:
    hasil = "Remaja"
else:
    print("Mohon Maaf Kriteria tidak ada")

# hasil
print("Kategori Usia %s tahun adalah %s" % (umur,hasil))