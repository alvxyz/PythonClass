# membuat fungsi sederhana
def suaraayam(): #mendefinisikan fungsi
    print("petok-petok")

def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah Rp. 20.000')

# # memanggil fungsi
# # suaraayam()
#
# membuat fungsi dengan input argumen
nilai = input("Masukan jumlah ayam yang ingin dibeli: ")
def hargatotalayam(nilai):
    suaraayam()
    harga = 20000
    hargaTotal= nilai*harga
    print("harga",nilai,'ayam adalah',hargaTotal)
suaraayam()

hargatotalayam(2)
# hargaayam()