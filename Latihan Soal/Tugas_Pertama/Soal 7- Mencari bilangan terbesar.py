print("ALVIAN TEDDY CAHYA PUTRA 3201816023")
print("Program untuk mencari bilangan terbesar")

# menginputkan nilai bilangan
print("Nilai maksimum dari tiga bilagan")
bil1 = float(input("Masukan bilangan ke-1 : "))
bil2 = float(input("Masukan bilangan ke-2 : "))
bil3 = float(input("Masukan bilangan ke-3 : "))

# proses
if bil1 > bil2 and bil1 > bil3:
    hasil = bil1
if bil2 > bil1 and bil2 > bil3:
     hasil = bil2
if bil3 > bil1 and bil3 > bil2:
    hasil = bil3

# hasil
print("Bilangan terbesar adalah", hasil)


