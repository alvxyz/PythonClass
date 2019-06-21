# def rekursif(angka):
#     if angka > 0:
#         print(angka)
#         angka = angka - 1
#         rekursif(angka)
#     else:
#         print(angka)
#
# angka = int(input("Masukan angka yang ingin dicari: "))
#
# rekursif(angka)


# def faktorial(n):
#     if n == 1:
#         print("1 = ", end="")
#         return 1
#     else:
#         print(n, "* ", end="")
#         return n * faktorial(n - 1)
#
# print(faktorial(5))



def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

print(faktorial(5))
