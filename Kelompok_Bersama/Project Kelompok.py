def ucapan():
    print("Harap Nama yang dicantumkan melaksanakan tugasnya dengan sepenuh hati :D, hehehehe ")


print("PROGRAM UNTUK MENENTUKAN JADWAL PIKET")

nomer_hari = int(input("""Masukan hari apa yang ingin Anda Cek:
1. Senin   2. Selasa   3. Rabu  
4. Kamis   5. Juma't
-->"""))

jadwal_piket = {'senin': {1: 'Khairani',
                          2: 'Juini',
                          3: 'Darul',
                          4: 'Mawan',
                          5: 'Alvian'
                          },
                'selasa': {1: 'Roby',
                           2: 'Riski',
                           3: 'Nurhidayah',
                           4: 'Dalilah',
                           5: 'Ayu'
                           },
                'rabu': {1: 'Mega',
                         2: 'Agus',
                         3: 'Arsyad',
                         4: 'Sindy',
                         5: 'Suryadi'
                         },
                'kamis': {1: 'Medi',
                          2: 'Irfan',
                          3: 'Salsa',
                          4: 'Nabil',
                          5: 'Aldi'
                          },
                'jumat': {1: 'Eka',
                          2: 'Kerry',
                          3: 'Nurazma',
                          4: 'Juniarsih',
                          5: 'Lazu',
                          }
                }
if nomer_hari == 1:
    print("Petugas piket hari adalah :")
    for no, nama in jadwal_piket['senin'].items():
        print(no, ".", nama)
elif nomer_hari == 2:
    print("Petugas piket hari adalah :")
    for no, nama in jadwal_piket['selasa'].items():
        print(no, ".", nama)
elif nomer_hari == 3:
    print("Petugas piket hari adalah :")
    for no, nama in jadwal_piket['rabu'].items():
        print(no, ".", nama)
elif nomer_hari == 4:
    print("Petugas piket hari adalah :")
    for no, nama in jadwal_piket['kamis'].items():
        print(no, ".", nama)
elif nomer_hari == 5:
    print("Petugas piket hari adalah :")
    for no, nama in jadwal_piket['jumat'].items():
        print(no, ".", nama)

print("\n")

ucapan()
# for hari, nama in jadwal_piket.items():
#     print("%s : %s" % (hari, nama))
