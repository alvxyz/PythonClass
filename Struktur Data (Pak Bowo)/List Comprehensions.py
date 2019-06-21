a = [2, 3, 5, 7, 9, 11]

b = []

for indeks in a:
    b.append(indeks * 2)
print(b)

d = [indeks * 2 for indeks in a]
print(d)

print("=" * 100)

# [1, 4, 9, 16, 18, 25, 36]
e1 = []
for x in range(1, 7):
    e1.append(x ** 2)
print(e1)

# dengan menggunakan list comprehensions
e2 = [x ** 2 for x in range((7 - 1), 0, -1)]
print(e2)

print("=" * 100)

# [36, 25, 16, 9 ,4, 1]
# for indeks in range(6, 0, -1):
#     print(indeks)

e3 = []
for indeks in range(6, 0, -1):
    e3.append(indeks ** 2)
    print(indeks)
print(e3)

# e4 = [indeks ** 2 for indeks in range(6, 0, -1)]
# print(e4)

o = []
for x in range(1, 6):
    o.append(x)
    print(o)
print(o)
