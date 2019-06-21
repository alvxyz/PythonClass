# 18-03-2019

# Penggunaan list dua dimensi

a = [[1, 2], [3, 4]]
print(a)

a[0] [0]
print(a)

c = [[0] * 4] * 4 # akan mengikuti semuanya karena dikali
print(c)
c[0][1] = 1
print(c)
# jadi setiap baris merujuk ke baris yang lain
# jika ingin aman harus menulisnya secara manual

# mengakses c =[baris][colom]

d = [[0, 0, 0, 0], [0], [0], [0]]
print(d)

# mencetak dengan perulangan

for baris in c:
    for element in baris:
        print(element, end=" ")
    print()
# karena element baris maka dapat diulang lagi

g = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
for baris in g:
    for element in baris:
        print(element, end=" ")
    print()

