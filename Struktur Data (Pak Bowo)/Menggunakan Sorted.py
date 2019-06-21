num = [10,2,3.4,56,1,1.11]
num.sort(reverse=True)
print(num)
num.sort(reverse=False)
print(num)

# print(help(list))
# Struktur Sorted memiliki parameter yaitu (key = None, reverse)
word = ['alvian', 'teddyi0', 'fdfcahya', 'putra']

word.sort(key = len)

print(word)