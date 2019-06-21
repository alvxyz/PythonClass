# for i in (0,10):
#     for j in range (0, i+1):
#         if j == i:
#             print('x')
#         else:
#             print("*")
# print ("")

# for i in range (1,21):
#     count_zero_remainder = 0
#     for j in range (1, i + 1):
#         num_remainder = i % j
#         if num_remainder == 0:
#             count_zero_remainder = count_zero_remainder + 1
#
#     if count_zero_remainder == 2:
#         print(i, "adalah bilangan prima")
#     else:
#         print(i, "bukanlah bilangan prima")

tumpukan = [1,2,3,4,5,6]
print('data sekatang', tumpukan)

#memasukan data baru
tumpukan.append(7)
print('data masuk', 7)
print('data sekarang', tumpukan)

tumpukan.pop()
print('data keluar',7)
print('data sekarang', tumpukan)
# out = tumpukan.out
# print('data keluar', out)
# print('data sekarang', tumpukan)

