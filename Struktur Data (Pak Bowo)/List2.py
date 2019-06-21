# 11-03-2019

my_list = list(('apple','banana','cherry'))

print(my_list)

# ini adalah cara untuk mengakses list
print(my_list[0])

# jika menggunakan -1 (kebelakang) ini akan membuat perhitungan dari belakang
print(my_list[-1])

# mengganti isi list
my_list[1] = "manggo"

print(my_list)

# mengecek apakah ada atau tidaknya isi di dalam list

if "manggo" in my_list:
    print("Yes, Manggo included")

if "Pepaya" in my_list:
    print("Yes")

# untuk mengetahui panjang suatu array
print(len(my_list))

# menambahkan data baru di dalam array
my_list.append("Naga")

print(my_list)

my_list.insert(0, "Durian")
print(my_list)

# menghilangkan data di dalam list (array)
my_list.remove("Naga")
print(my_list)

my_list.clear() #menghapus seluruh data
print(my_list)

# menukar indeks list
this_list = ['apple', 'manggo']

c = this_list
this_list[0] = this_list[1]
this_list [1] = c

print(this_list)

# atau menggunakan cara python
this_list[0], this_list[1] = this_list[1], this_list[0]

print(this_list)

