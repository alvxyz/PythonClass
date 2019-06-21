# # cara menginputkan nilai pada array 2 dimensi
# baris = int(input("Masukan jumlah baris: "))
#
# a = [[int(s) for s in input("Masukan nilai array per baris: ").split()]
#      for i in range(baris)]
# # dari segi performa list komperhension lebih ngebuttt
#
# print(a)


# cara ke 2 untuk menginputkan
# jagged array adalah jumlah kolom dalam setiap baris tidak sama

baris = int(input("Masukan jumlah baris: "))
a = []
for i in range(baris):  # ini akan membuat 3 perulangan
    str_prompt = "Masukkan array baris ke- " + str(i + 1) + " : "
    a.append([int(s) for s in input(str_prompt).split()])
print(a)

# cara dengan append input + input
baris = int(input("Masukan jumlah baris: "))
a = []

for i in range(baris):
    # hasil dari perulanagan i adalah = 0 1 2
    a.append([int(s) for s in input("Masukkan array baris ke-" + str(i + 1) + " : ").split()])
    # str(i+1) maksudnya pada saat perulangan akan menambahan nilai untuk penomeran
    # jadi masukan array baris ke 1
    # jadi masukan array baris ke 2
    # jadi masukan array baris ke 3 dst tergantung banyak baris
print(a)

baris = 3
for i in range(baris):
    print(i)
    # 0 1 2
