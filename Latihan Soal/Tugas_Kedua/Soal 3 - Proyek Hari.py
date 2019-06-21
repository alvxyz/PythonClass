print("Program untuk mengkonversikan hari")

# input
hari = int(input("Masukan jumlah hari : "))
bulan = int(input("Masukan jumlah bulan : "))
tahun = int(input("Masukan jumlah tahun : "))

#proses
hasil = (tahun * 360) + (bulan * 30) + hari

#output
print("%d tahun, %d bulan, %d hari adalah %d hari" % (tahun,bulan,hari,hasil))
