print("Program untuk menghitung upah")

#input
jam_kerja = float(input("Masukan jumlah jam kerja Anda dalam satu minggu : "))
bayaran = float(input("Masukan Bayaran anda per-jam : "))

if jam_kerja <= 48:
    gaji = jam_kerja * bayaran

elif jam_kerja > 48:
    x = jam_kerja - 48
    bonus = bayaran + 2000
    gaji = 48 * bayaran + (float (x) * float(bonus))
print("Jadi jumlah gaji Anda adalah Rp. %s" %(gaji))