# cara mendefinisikan dicrtionary

data_mahasiswa = {'nama' : 'Alvian Teddy Cahya Putra',
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


# Menampilakan data dalam dictionary
print("Nama saya adalah %s" % data_mahasiswa['nama'])
print("Hobby saya adalah %s" % data_mahasiswa['Hobby'])
print("Facebook saya adalah %s" % data_mahasiswa ['Social Media'] ['facebook'])
print("Instagram saya adalah %s" % data_mahasiswa ['Social Media'] ['Instagram'])