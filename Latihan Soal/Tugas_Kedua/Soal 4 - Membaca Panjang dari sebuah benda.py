print("PROGRAM UNTUK MENGKONVERSIKAN PANJANG")
print("1 Inchi = 25,4 mm, 1 kaki = 30,48n cm, dan 1 yard = 0,9144 m")
# input
meter = float(input("Masukan panjang dalam meter : "))

#proses
inchi = (meter * 1000) / 25.4
kaki = (meter * 100) / 30.48
yard = (meter / 0.9144)

#output
print("%d meter = %d inchi, %d kaki, %d yard " %(meter, inchi, kaki, yard))
