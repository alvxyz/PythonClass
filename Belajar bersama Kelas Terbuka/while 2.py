# else, break, continue, pass
angka = int(input('Masukan angka yang ingin dicari: '))

while angka < 10:
    if angka is 5:
        print('checkpoint 1')
        print('nilai angka adalah:', angka)
        angka += 1
    else:
        print('nilai angka di akhir while adalah', angka)