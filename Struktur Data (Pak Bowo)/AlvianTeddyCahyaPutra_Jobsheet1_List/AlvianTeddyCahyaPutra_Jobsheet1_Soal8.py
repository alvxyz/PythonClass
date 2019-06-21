nilai_a = [5, 10, 6, 0, 4]
nilai_a.reverse()
nilai_b = []

for indeks in range(0, len(nilai_a)):
    if nilai_a[indeks] % 2 == 0 and nilai_a[indeks] > 0:
        nilai_b.insert(0, nilai_a[indeks])
    else:
        nilai_b.append("_")

print(nilai_b)
