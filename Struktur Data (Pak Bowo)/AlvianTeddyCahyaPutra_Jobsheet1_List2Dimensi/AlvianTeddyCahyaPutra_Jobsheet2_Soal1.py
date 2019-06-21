# 18-03-2019
print("==== PROGRAM ARRAY MULTIDIMENSI ====")
jml_baris = int(input("Masukan jumlah baris array: "))
a = []
for i in range(jml_baris):
    a.append([int(s) for s in input(
        "Masukan elemen array baris ke- {0}(pisahkan dengan spasi): ".format(str(i + 1))).split()])

# print(a)

    # split langsung menjadi ke list
    # join akan mengubah list ke string
print("Array yang Anda masukan adalah: ")
for baris in a:
    # print(a)
    for element in baris:
        print("[", element, "]", end=" ")
    print()

# # penggunaan split dan join
# a = ["Hello", "Saya", "Budi"]
# " ".join(a).split()