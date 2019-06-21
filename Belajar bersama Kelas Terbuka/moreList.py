Barang = ['kunci', 'ember', 'jaket', 'ban', 'mobil']
print(Barang)

#beberapa method yang bisa digunakan untuk memanipulasi list
#method untuk menambah data ke dalam list
Barang.append('Sepeda')
print(Barang)

Barang.extend('gundam')
print(Barang)

Barang.insert(3,'Sepeda')
print(Barang)

#method untuk menghitung anggota
jumlahSepeda = Barang.count('Sepeda')
print('Jumlah sepeda adalah:', jumlahSepeda)

#meremove data
Barang.remove('Sepeda')
print(Barang)

Barang.reverse()
print(Barang)

print('='*100)
Stuff = Barang.copy()
Stuff.append('amoeba')
print(Stuff)
print(Barang)

