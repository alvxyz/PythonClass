# Scope dengan variabel : local

namaKucing = 'cassandra bellow'

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('saya merubah nama kucing menjadi' , namaKucing)

namaKucing = 'alex manasi'
namaKucing = 'dimansansn' # yang akan dieksekusi adalah variabel yang paling akhir

rubahNamaKucing('Kentos')

print('nama kucing saya menjadi', namaKucing) # akan mengeksekusi variabel yang paling akhir (dimansans)