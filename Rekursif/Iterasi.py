# 31-12-2018
# Program iterasi (konvensioanl)

def iterasi_faktorial(n):
    hasil = 1
    for i in range(2,n+1):
        hasil *= i
    return hasil

print(iterasi_faktorial(5))






# nilai = int(input("Masukan nilai yang ingin dicari: "))
#
# def reversed(nilai):
#     for i in range (nilai + 1):
#         hasil = list(i)
#         reversed(hasil)
#
# reversed(nilai)