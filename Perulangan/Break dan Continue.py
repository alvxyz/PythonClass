# 4-12-2018 Selasa

#contoh while dengan break
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

#contoh for dengan continue
# for x in range (10):
#     #check if x is even
#     if x % 2 == 0:
#         continue
#     print(x, end=" ")
#
# print("="*100, end=" ")
#
# for x in range (10):
#     #check if x is even
#     if x % 2 == 0:
#         print(x, end=" ")

#contoh kedua while dengan continue
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
#guna continue adalah untuk melewati suatu kondisi tanpa memberhentikan suatu proses perulangan
#jika perulangan sampai ke 3 maka continue akan melanjutkan perulangan lagi tanpa menampilkan angka 3

print("="*100)
for i in range(1,11):
    if i == 5:
        continue
    print(i)