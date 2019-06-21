#deklarasi fungsi
def perkalian(bil1, bil2):
    'menghitung perkalian 2 bilangan bulat'
    hasil = bil1 * bil2
    return hasil

# program utama
bil1 = int(input("Input bilangan 1 : "))
bil2 = int(input('Masukan bilangan 2 : '))

# memanggil fungsi
print('Hasil perkalian', bil1, ' dengan ', bil2, ' adalah ', perkalian(bil1,bil2))