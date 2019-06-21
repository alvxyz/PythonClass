a = [[1, 2], [3, 4]]

print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])

print("="*100)

for i_baris in range(0, len(a)): # cuman memberitahu jumlah barisnya --> 0  1
    # hasil i_baris adalah
    # 0
    # 1
    # print(i_baris)
    # print(a[i_baris][0])
    # print(a[i_baris][1])
    for i_kolom in range(0, len(a[i_baris])):
        print(a[i_baris][i_kolom], end=" ")
    print()

# print(a)