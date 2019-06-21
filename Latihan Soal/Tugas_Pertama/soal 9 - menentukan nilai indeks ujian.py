print("ALVIAN TEDDY CAHYA PUTRA 3201816023")

print("Program Nilai Indeks Mahasiswa")

# menginput nilai
uts = float(input("Masukan nilai UTS: "))
uas = float(input("Masukan nilai UAS: "))

# proses
nilai = uas * 60/100 + uts * 40/100

if nilai >= 80:
    hasil = "A"
elif 80 > nilai >= 70:
    hasil = "B"
elif 70 > nilai >= 55:
    hasil = "C"
elif 55 > nilai >= 40:
    hasil = "D"
elif nilai < 40:
    hasil = "E"

# menampilkan hasil
print("Total Nilai Akhir adalah: ", nilai)
print("Nilai Indeks:", hasil)