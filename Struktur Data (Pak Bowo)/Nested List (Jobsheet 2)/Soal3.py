array = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]
# array = [int(s) for s in input("Masukan nilai: ").split()]
# array = int(input("Masukan nilai array: "))
# print(array)
# print(len(array))

# x = array[0]
# array[0] = array[1]
# array[1] = x
# print(x)
# print(array)

# for indeks in range(0, len(array) - 2):
#     if array[indeks] > array[indeks+1]:
#         array[indeks], array[indeks+1] = array[indeks+1], array[indeks]
# print(array)

print("=" * 100)
jum = 0
for indeks2 in range(len(array) - 1, -1, -1):
    # len(array) -1, -1, -1
    swap = False
    for indeks in range(0, indeks2):
        if array[indeks] > array[indeks + 1]:
            array[indeks], array[indeks + 1] = array[indeks + 1], array[indeks]
            swap = True
        jum = jum + 1
    print(array)

    if swap == False:
        break
print(jum)
print(array)
