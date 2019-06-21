print('''
Daftar Buah :
1. Mangga
2. Jeruk
3. Durian
''')

buah = int(input('Pilih buah : '))
jumlah = int(input('Berapa banyak : '))

harga = {"Mangga": 15000,
         "Jeruk": 12000,
         "Durian" : 50000}

def mangga(jumlah, buah):
    hitungan = jumlah * buah
    return  hitungan

print(mangga(buah,jumlah))
# def jeruk (jumlah, 12000):
#     hitungan =jumlah * 12000
#     return hitungan
# def durian (jumlah, 50000):
#     hitungan = jumlah * 50000
#     return hitungan
#
# if buah == 1:
#     def mangga()
#
# ulang = input('Mau beli lagi ? [y/t]')
# while ulang == 'y':
#     a = int(input('Pilih buah : '))
#     b = int(input('Berapa banyak : '))
#     ulang = input('Mau beli lagi ? [y/t]')
#     if ulang == 't':
#         print('makaseh')
#
# hasil = hitung(a,b)
# print(hasil)
