print("Program untuk menentukan berat badan ideal")

#input
tinggi_badan = float(input("Masukkan tinggi badan Anda: "))

#proses
hasil = tinggi_badan - 100
hasil2 = hasil  * 0.1
berat_badan = hasil - hasil2

#output
print("Berat badan ideal Anda adalah : ", berat_badan)
