# awal = int(input("Masukan Nilai Awal: "))
# akhir = int(input("Masukan Nilai Akhir: "))
#
# count = 0
# summ = 0
#
# print("Bilangan antara %d dan %d " % (awal, akhir))
#
# for i in range (awal, akhir+1) :
#     print(i, end=" ")
#     count = count + 1
#     summ = summ + 1

awal = int(input("Masukan Nilai Awal: "))
akhir = int(input("Masukan Nilai Akhir: ")

count = 0

summ = 1

print("Bilangan antara %d dan %d " % (awal, akhir))

for i in range (awal, akhir += 1 , 3):
    print(i, end=" ")
    count = count + 1
    summ = summ * i

print("Bilangan diatas ada %d bilangan" % count)
print("Jumlah keseluruhan bilangan adalah = %d" % summ)