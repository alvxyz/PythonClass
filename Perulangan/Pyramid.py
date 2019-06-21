#membuat sebuah piramid
# Input = lebar dari pyramid
# Output = tampilan pyramid
# 5 - 12 - 2018

lebar_pyramid = int(input("Masukan lebar piramid yang diinginkan: "))

for i in range(0, lebar_pyramid):
    for j in range(0, lebar_pyramid-i):
        print(" ", end="")
    for k in range(0, 2*i+1):
        print("0", end="")
    print("")