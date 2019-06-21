data = list(input("Masukan kata yang ingin dipecah: ").lower())

nilai_vokal = 0
nilai_non = 0

for element in data:
    if element == "a" \
            or element == "i" \
            or element == "u" \
            or element == "e" \
            or element == "o":
        nilai_vokal += 1
    else:
        nilai_non += 1

print("jumlah vokal pada data adalah: ", nilai_vokal)
print("jumlah non vokal pada data adalah: ", nilai_non)