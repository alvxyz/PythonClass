# Meminta input dari user
mystr = input("Masukan nama yang ingin dibalik: ")
mylist = list(mystr) # konversi string ke list
mylist.reverse() # membalik posisi indeks pada list
print(mylist) # mencetak list untuh, jadinya masih ada kurung dan petik
# ['n','o','t','n','a']
print(''.join(mylist)) # konversi list ke string dan mencetaknya

# # menggunakan cara primitif
# for i in range(1, len(mylist)+1):
#     print(mylist[i])
nama = ["a","n","t","o"]

nama.reverse()
print(nama)