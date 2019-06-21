data = list(input("Masukan kata yang ingin dipecah: ").lower())

nilai_vokal = [0]*5 # inisiasi list 5 element, dengan nilai awal 0 => [0,0,0,0,0]
vokal = ['a', 'i', 'u', 'e', 'o']

for element in data:
    if element == "a" :
        nilai_vokal[0] += 1
    elif element == "i" :
        nilai_vokal[1] += 1
    elif element == "u" :
        nilai_vokal[2] += 1
    elif element == "e" :
        nilai_vokal[3] += 1
    elif element == "o" :
        nilai_vokal[4] += 1

for nilai in range(0, len(vokal)):
    print("Jumlah vokal %s = %s" % (vokal[nilai], nilai_vokal[nilai]))

print("jumlah non vokal pada data adalah: ", len(data)-sum(nilai_vokal))