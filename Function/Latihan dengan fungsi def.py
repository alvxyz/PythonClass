print("""       Tugas Kelompok oleh:
            - Alvian Teddy Cahya Putra
            - Darul Ihsan
            - Khairani
            - Mawan Saputra
            - Marsela Juini
            
            Pemrograman Tersturktur
            Penggunaan Function
            Politeknik Negeri Pontianak
            Kelas A Semester 1

        Operasi Matematika mana yang Anda ingin cari
        *==================================*
        |1. Penjumlahan   |   4. Pembagian |
        |2. Pengurangan   |   5. Modulus   |
        |3. Perkalian     |                |                  
        *==================================*""")

pilihan = int(input("Masukan pilihan yang ingin dicari :  "))
bilangan_pertama = int(input("Masukan bilangan Pertama : "))
bilangan_kedua = int(input("Masukan bilangan Kedua : "))

#untuk membuat fungsi operasi matematika
def penjumlahan( bilangan_pertama, bilangan_kedua):
    hitungan = bilangan_pertama + bilangan_kedua
    return hitungan
def pengurangan(bilangan_pertama,bilangan_kedua):
    hitungan = bilangan_pertama - bilangan_kedua
    return hitungan
def perkalian(bilangan_pertama, bilangan_kedua):
    hitungan = bilangan_pertama * bilangan_kedua
    return hitungan
def pembagian(bilangan_pertama, bilangan_kedua):
    hitungan = bilangan_pertama / bilangan_kedua
    return hitungan
def modulus(bilangan_pertama, bilangan_kedua):
    hitungan = bilangan_pertama % bilangan_kedua
    return hitungan

if bilangan_pertama % 2 == 0 :
    print("bilangan ini bukan bilangan bulat")

#hitungan hanya untuk bilangan bulat
# if bilangan_pertama and bilangan_kedua % 2 == 0 :
if pilihan == 1:
            # if bilangan_pertama and bilangan_kedua % 2 == 0:
    hasil = penjumlahan(bilangan_pertama,bilangan_kedua)
    print("Penjumlahan antara %s + %s  = %s" % (bilangan_pertama,bilangan_kedua,hasil))
elif pilihan == 2:
    hasil = pengurangan(bilangan_pertama, bilangan_kedua)
    print("Pengurangan antara %s - %s = %s" % (bilangan_pertama,bilangan_kedua,hasil))
elif pilihan == 3:
    hasil = perkalian(bilangan_pertama, bilangan_kedua)
    print("Perkalian antara %s x %s = %s" % (bilangan_pertama,bilangan_kedua,hasil))
elif pilihan == 4:
    hasil = pembagian(bilangan_pertama, bilangan_kedua)
    print("Pembagian antara %s : %s = %s" % (bilangan_pertama,bilangan_kedua,hasil))
elif pilihan == 5:
    hasil = modulus(bilangan_pertama, bilangan_kedua)
    print("Modulus antara %s modulus %s = %s" % (bilangan_pertama,bilangan_kedua,hasil))
else:
    print("Maaf Anda memasukan bilangan ganjil")

# Bertanya akan menggulang proses program kembali jika user menginginkannya atau tidak
# ulang = True
ulang = input('Apakah ingin menghitung kembali [ya,tidak] ? ')
while ulang == 'ya':
    if ulang == 'ya':
        print("""
        Operasi Matematika mana yang Anda ingin cari
        *==================================*
        |1. Penjumlahan   |   4. Pembagian |
        |2. Pengurangan   |   5. Modulus   |
        |3. Perkalian     |                |                  
        *==================================*""")
        pilihan = int(input("Masukan pilihan yang ingin dicari :  "))
        bilangan_pertama = int(input("Masukan bilangan Pertama : "))
        bilangan_kedua = int(input("Masukan bilangan Kedua : "))

        def penjumlahan(bilangan_pertama, bilangan_kedua):
            hitungan = bilangan_pertama + bilangan_kedua
            return hitungan

        def pengurangan(bilangan_pertama, bilangan_kedua):
            hitungan = bilangan_pertama - bilangan_kedua
            return hitungan

        def perkalian(bilangan_pertama, bilangan_kedua):
            hitungan = bilangan_pertama * bilangan_kedua
            return hitungan

        def pembagian(bilangan_pertama, bilangan_kedua):
            hitungan = bilangan_pertama / bilangan_kedua
            return hitungan

        def modulus(bilangan_pertama, bilangan_kedua):
            hitungan = bilangan_pertama % bilangan_kedua
            return hitungan

        if pilihan == 1:
            hasil = penjumlahan(bilangan_pertama, bilangan_kedua)
            print("Penjumlahan antara %s + %s = %s" % (bilangan_pertama, bilangan_kedua, hasil))
        elif pilihan == 2:
            hasil = pengurangan(bilangan_pertama, bilangan_kedua)
            print("Pengurangan antara %s - %s = %s" % (bilangan_pertama, bilangan_kedua, hasil))
        elif pilihan == 3:
            hasil = perkalian(bilangan_pertama, bilangan_kedua)
            print("Perkalian antara %s x %s = %s" % (bilangan_pertama, bilangan_kedua, hasil))
        elif pilihan == 4:
            hasil = pembagian(bilangan_pertama, bilangan_kedua)
            print("Pembagian antara %s : %s = %s" % (bilangan_pertama, bilangan_kedua, hasil))
        elif pilihan == 5:
            hasil = modulus(bilangan_pertama, bilangan_kedua)
            print("Modulus antara %s modulus %s = %s" % (bilangan_pertama, bilangan_kedua, hasil))
        else:
            print("Maaf Anda memasukan nomer pilihan yang salah, harap mengecek pilihan dari no 1-5")
        ulang = input('Apakah ingin menghitung kembali [ya,tidak] ? ')
if ulang == 'tidak':
    print('Terimakasih telah menggunakan Program yang telah kami buat :D, have an aice day')


