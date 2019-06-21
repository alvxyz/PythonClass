print("Menampilkan Nama 5 Teman")

# List teman
teman_teman = ["Eka","Fresco","Irfan","Rezky","Agus"]
print(teman_teman[2])
print(1000*"=")

#menambah teman menggunakan append -> menambahkan data di ujung list
teman_teman.append("PAK POL")

#menambah teman menggunakan insert ->
teman_teman.insert(0,"Agus")

#menghapus item fresco dari list teman_teman
del teman_teman[2]
teman_teman.remove("PAK POL")

# perulangan untuk menulis data di dalam list
print("DAFTAR TEMAN")
# for g in teman_teman:
#     print(g, end=' ')

for teman in teman_teman:
    print("Nama teman saya =", teman)

print("Semua teman saya berjumlah : ", len(teman_teman))
