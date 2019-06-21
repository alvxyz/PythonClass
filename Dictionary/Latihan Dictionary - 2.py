data_mahasiswa = {'Nama' : 'Alvian Teddy Cahya Putra',
                  'NIM' : '3201816023',
                  'Prodi' : 'Teknik Informatika',
                  'E-Mail' : 'alvianteddy@gmail.com',
                  'Website' : 'www.alvxyz.co.id',
                  'Hobby' : 'Ngulik Komputer',
                  'Social Media' : {
                      'facebook' : 'Alvian Teddy Cahya Putra',
                      'Instagram' : '@_alvxyz'
                      }
                  }
# for i in data_mahasiswa:
#     print([i], data_mahasiswa [i])

# input_user = str(input("Masukan Hal yang ingin Anda ketahui : "))
# print(data_mahasiswa [input_user])

# masukan = str(input("Masukan NIM Anda : "))
# if masukan == data_mahasiswa['NIM']:
#     for data in data_mahasiswa:
#         print(data, ":", data_mahasiswa[data])
#         print(100*"-")
# else:
#     print("Data tidak ditemukan")
print ("Fb :", data_mahasiswa['Social Media']['facebook'])
# cara kedua
# for i, z in data_mahasiswa.items():
#     print("%s : %s" % (i,z))
