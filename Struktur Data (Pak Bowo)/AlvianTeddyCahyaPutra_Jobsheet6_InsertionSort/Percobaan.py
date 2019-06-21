
#....0...1...2...3...4
a = [9, 8, 2, 1 , 2]

# 1 < 0 ? tidak

# 2 < 1 ? tukar
# [1, 34, 100, 45, 5}

for i in range(0, len(a)):
    for j in range(i - 1, 0, -1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        else:
            break
print(a)