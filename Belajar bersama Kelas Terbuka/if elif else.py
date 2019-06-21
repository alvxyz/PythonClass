print(100*"+")

nilai = int(input("Masukan nilai Anda: "))

if 80 <= nilai <= 100:
    print("Nilai Anda adalah A")
elif 70 <= nilai < 80:
    print("Nilai Anda adalah B")
elif 60 <= nilai < 70:
    print("Nilai Anda adalah C")
elif 50 <= nilai < 60:
    print("Nilai Anda adalah D")
else:
    print("Anda tidak lulus mata kuliah ini")

