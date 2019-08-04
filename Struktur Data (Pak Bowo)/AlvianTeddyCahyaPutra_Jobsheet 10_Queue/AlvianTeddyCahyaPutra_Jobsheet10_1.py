class Queue:
    # variabel global
    q_list = []
    front = 0
    rear = 0
    n_items = 0
    max_size = 0

    def __init__(self, x):
        self.max_size = x
        self.q_list = [0] * self.max_size
        self.front = 0
        self.rear = -1
        self.n_items = 0

    # menambahkan data (data pertama akan tetap, data rear akan bertamba terus)
    def enqueue(self, n):
        self.rear += 1
        self.q_list[self.rear] = n
        self.n_items += 1

    # mengeluarkan data dalam antrian (data pertama yang akan keluar)
    def dequeue(self):
        tmp = self.q_list[self.front]
        self.front += 1
        self.n_items -= 1
        return tmp

    # mengecek apakah queue penuh
    def is_full(self):
        return self.n_items == self.max_size

    # mengecek apakah queue kosong
    def is_empty(self):
        return self.n_items == 0

    # melihat nilai terdepan angka berapa
    def peekfront(self):
        if not self.is_empty():
            return self.q_list[self.front]
        else:
            return "Tidak ada antrian"

    # mengembalikan size
    def size(self):
        return self.n_items

    # menghapus semua data
    def clear(self):
        self.front = 0
        self.rear = -1
        self.n_items = 0

    def hasil(self):
        return self.q_list

    def hapus_data(self):
        x = int(input("Masukkan data yang akan dihapus: "))
        self.q_list.remove(x)
        return self.q_list

    def cari_data(self):

        i = 0
        ketemu = False
        key = int(input("Masukkan angka yang dicari: "))
        while i < len(self.q_list) and not ketemu:
            if self.q_list[i] == key:
                ketemu = True
            elif self.q_list[i] > key:
                break
            else:
                i += 1

        if ketemu:
            print("Data", key, "yang dicari berada di indeks: ", i)
            return self.q_list.index(key)
        else:
            print("Data tidak ditemukan")


import random
import time

my_q = Queue(5)

# x = 1
# while not my_q.is_full():
#     data = random.randrange(1, 100, 5)
#     print("Memasukkan Orang nomer:", data, "ke dalam antrian")
#     my_q.enqueue(data)
#     time.sleep(0.5)
    # x += 1


# untuk percobaan pengganti soal 3
while not my_q.is_full():
    for i in range(1, 6):
        print("Memasukkan Orang nomer:", i, "ke dalam antrian")
        my_q.enqueue(i)
        time.sleep(0.5)


# pecahkan masalah data kenapa bisa random
# i = 1
# data = 1
#
# while not my_q.is_full():
#     while i <= 5:
#         data += i
#         print("Memasukkan Orang nomer:", data, "ke dalam antrian")
#         my_q.enqueue(data)
#         time.sleep(0.5)
#         i += 1


print()
print("Yang mengantri sekarang ada:", my_q.size(), "Orang")
print("Yang paling depan adalah:", my_q.peekfront())
print()
print("Antrian sekarang: " + str(my_q.hasil()))

my_q.hapus_data()
print("========Menghapus data========")
print("Antrian sekarang: " + str(my_q.hasil()))

print("========Mencari data========")
my_q.cari_data()


# print()
# while not my_q.is_empty():
#     print("Orang nomer antrian:", my_q.dequeue(), "telah dipanggil")
#     time.sleep(0.5)
#
# print()
# print("Yang mengantri sekarang ada:", my_q.size(), "Orang")
# print("Yang paling depan adalah:", my_q.peekfront())


# my_q.clear()
