# # cara primitif
# data = list(input("Masukan kata yang ingin dipecah: ").lower())
#
# nilai_vokal_a = 0
# nilai_vokal_i = 0
# nilai_vokal_u = 0
# nilai_vokal_e = 0
# nilai_vokal_o = 0
# nilai_non = 0
#
# for element in data:
#     if element == "a" :
#         nilai_vokal_a += 1
#     elif element == "i" :
#         nilai_vokal_i += 1
#     elif element == "u" :
#         nilai_vokal_u += 1
#     elif element == "e" :
#         nilai_vokal_e += 1
#     elif element == "o" :
#         nilai_vokal_o += 1
#     else:
#         nilai_non += 1
#
# print("jumlah vokal a: ", nilai_vokal_a)
# print("jumlah vokal i: ", nilai_vokal_i)
# print("jumlah vokal u: ", nilai_vokal_u)
# print("jumlah vokal e: ", nilai_vokal_e)
# print("jumlah vokal o: ", nilai_vokal_o)
# print("jumlah non vokal pada data adalah: ", nilai_non)

# cara good
data = list(input("Masukan kata yang ingin dipecah: ").lower())

nilai_vokal = [0] * 5  # inisiasi list 5 element, dengan nilai awal 0 => [0,0,0,0,0]

for element in data:
    if element == "a":
        nilai_vokal[0] += 1
    elif element == "i":
        nilai_vokal[1] += 1
    elif element == "u":
        nilai_vokal[2] += 1
    elif element == "e":
        nilai_vokal[3] += 1
    elif element == "o":
        nilai_vokal[4] += 1

print("jumlah vokal a: ", nilai_vokal[0])
print("jumlah vokal i: ", nilai_vokal[1])
print("jumlah vokal u: ", nilai_vokal[2])
print("jumlah vokal e: ", nilai_vokal[3])
print("jumlah vokal o: ", nilai_vokal[4])
print("jumlah non vokal pada data adalah: ", len(data) - sum(nilai_vokal))

# cara good
data = list(input("Masukan kata yang ingin dipecah: ").lower())

nilai_vokal = [0] * 6  # inisiasi list 5 element, dengan nilai awal 0 => [0,0,0,0,0]

for element in data:
    if element == "a":
        nilai_vokal[0] += 1
    elif element == "i":
        nilai_vokal[1] += 1
    elif element == "u":
        nilai_vokal[2] += 1
    elif element == "e":
        nilai_vokal[3] += 1
    elif element == "o":
        nilai_vokal[4] += 1
    else:
        nilai_vokal[5] += 1

print("jumlah vokal a: ", nilai_vokal[0])
print("jumlah vokal i: ", nilai_vokal[1])
print("jumlah vokal u: ", nilai_vokal[2])
print("jumlah vokal e: ", nilai_vokal[3])
print("jumlah vokal o: ", nilai_vokal[4])
print("jumlah non vokal: ", nilai_vokal[5])
