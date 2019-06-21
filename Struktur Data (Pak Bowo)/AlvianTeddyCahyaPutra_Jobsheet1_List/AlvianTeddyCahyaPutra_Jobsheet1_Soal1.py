# meminta input dari user, dan simpan ke dalam list

my_list = [int(s) for s in input("Masukan angka dipisah spasi: ").split()]
print(my_list)

# string from
# split berguna untuk memisah inputan
total = 0
for element in my_list:
    # print(element)
    total += element

print(total)
print("="*100)

# menggunakan cara python
print("Total data:", sum(my_list))
print("Rata-rata: ", sum(my_list)/len(my_list))

# # menghitung rata-rata dengan efisien
# total = sum(my_list)
# print("Jumlah total data di dalam list adalah: ", total)
# print("Rata-rata: ", total/len(my_list))
a = ("ayam bakar tiga rasa", "enak sekali", "damber")
print(len(a))
b = ['ayua,f,d,fd,f,df,df,df,d,']
print(len(b))