import statistics

class Stack:
    # Variabel Global
    stack_list = []
    max_size = 0
    top = -1

    # dicantumkan self agar dapat mengakses variabel global
    def __init__(self, size):
        self.max_size = size
        self.stack_list = [0] * size
        self.top = -1

    def push(self, x):
        self.top += 1
        self.stack_list[self.top] = x

    def pop(self):
        dummy = self.stack_list[self.top]
        self.top -= 1
        return dummy

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def hasil(self):
        return self.stack_list

    def peek_top(self):
        return self.top

    def clear(self):
        self.top = -1

    def hapus_data(self):
        x = int(input("Masukkan angka yang akan dihapus: "))
        self.stack_list.remove(x)
        return self.stack_list

    def cari_data(self):

        i = 0
        ketemu = False
        key = int(input("Masukkan angka yang dicari: "))
        while i < len(self.stack_list) and not ketemu:
            if self.stack_list[i] == key:
                ketemu = True
            elif self.stack_list[i] > key:
                break
            else:
                i += 1

        if ketemu:
            print("Data", key, "yang dicari berada di indeks: ", i)
            return self.stack_list.index(key)
        else:
            print("Data tidak ditemukan")

    def edit_data(self):
        di_edit = int(input("Masukkan indeks yang akan diubah: "))
        data_baru = int(input("Masukkan data baru: "))
        self.stack_list[di_edit] = data_baru
        return self.stack_list

    def total_data(self):
        return sum(self.stack_list)

    def rata_rata_data(self):
        return statistics.mean(self.stack_list)
        # return self.total_data() / len(self.stack_list)

    def nilai_terbesar(self):
        return max(self.stack_list)

    def nilai_terkecil(self):
        return min(self.stack_list)


import random
import time

mystack = Stack(10)

# for x in range(5, 1005, 5):
#     mystack.push(x)

print("===Memasukkan angka ke dalam stack===")

# while not mystack.is_full():
#     angka_random = random.randrange(0, 10)
#     print(f"Memasukkan {angka_random} ke dalam Stack")
#     time.sleep(0.2)
#     mystack.push(angka_random)

while not mystack.is_full():
    for i in range(1, 11):
        print("Memasukkan", i, "kedalam Stack")
        mystack.push(i)

# melakukan penghapusan data dan nilai indeksnya dimulai dari -1
# mystack.clear()


# mystack.push(12)
print("Indeks top sekarang berada di", mystack.peek_top())

print()

# print("===Mengeluarkan angka ke dalam stack===")
# while not mystack.is_empty():
#     print("Data yang diambil", mystack.pop())
#
# # print("Indeks top sekarang berada di", mystack.peek_top())
# print("Indeks top sekarang berada di", mystack.peek_top())

print(mystack.hasil())

# print("Setelah di hapus:\n", mystack.hapus_data())

# print(mystack.cari_data())

# print(mystack.edit_data())

print("Total data adalah: ", mystack.total_data())

print("Rata-rata: ", mystack.rata_rata_data())

print("Nilai terbesar: ", mystack.nilai_terbesar())

print("Nilai terkecil: ", mystack.nilai_terkecil())