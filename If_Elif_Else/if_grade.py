# Program untuk mengetahui predikat IP
# Input : Nilai IP
# Output : Predikat IP
# Author : Alvian

print("PROGRAM UNTUK MENGETAHUI PREDIKAT IP")
ip = float(input("Masukan nilai IP Anda: ")) #Input dari user berupa IP

if (ip > 2 and ip < 2.75): # Pengklasifikasi IP
    print("IP Anda adalah %s Predikat Anda adalah Lulus Memuaskan" % ip) # Mencetak predikat IP

elif (ip >= 2.75 and ip < 3.5 ): # Pengklasifikasi IP
    print("IP Anda adalah %s Predikat Anda adalah Lulus Sangat Memuaskan" % ip) # Mencetak predikat IP

elif(ip >= 3.5 and ip <= 4.00): # Pengklasifikasi IP
    print("IP Anda adalah %s Predikat Anda adalah Lulus dengan Pujian" % ip) # Mencetak predikat IP
else:
    print("Data IP tidak valid") # Mencetak nilai IP jika semua syarat di atas tidak terpenuhi
