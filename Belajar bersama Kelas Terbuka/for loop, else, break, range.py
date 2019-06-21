# for i in range(0,11):
#     print(i)
#
# for z in range(5,51,10):
#     print(z)

number = int(input("Maskan angaka yang akan dicari dalam range 1-50: "))

for i in range(1,51):
    print(i)

    if i is number:
        print("angka ditemukan", i)
        break
else:
    print("angka tidak ditemukan, Anda memasukan angka lebih dari 1-50")


# for i in range(100,150):
#     print(i)