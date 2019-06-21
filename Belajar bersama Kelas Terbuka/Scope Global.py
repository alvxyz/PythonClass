# scope variabel : global

namaKucing = 'cassandra'
makananKucing = 'royal canin'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru # variabel global
    nama = namaBaru # variabel lokal
    print('saya rubah nama kucing saya menjadi', namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing # jika namaKucing tidak dimasukan ke global maka yang akan tereksekusi adalah nama kucing yang sudah diganti pada fungsi pertana
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('ketie')

kasihMakanKucing('pusscas','manadolla') #dia akan mengikuti fungsi (apa yang ada di dalam bagian
                                        # def-nya saja tidak akan mengangu fungsi yang diatas

print('nama kucing saya menjadi', namaKucing, 'dan makanannya adalah', makananKucing)
