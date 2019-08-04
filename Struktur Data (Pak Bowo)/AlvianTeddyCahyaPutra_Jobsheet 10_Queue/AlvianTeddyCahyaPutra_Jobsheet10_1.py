class Queue:
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


import random
import time

my_q = Queue(5)

# x = 1
while not my_q.is_full():
    data = random.randrange(1, 100, 5)
    print("Memasukkan Orang nomer:", data, "ke dalam antrian")
    my_q.enqueue(data)
    time.sleep(0.5)
    # x += 1

my_q.clear()

print()
print("Yang mengantri sekarang ada:", my_q.size(), "Orang")
print("Yang paling depan adalah:", my_q.peekfront())


print()
while not my_q.is_empty():
    print("Orang nomer antrian:", my_q.dequeue(), "telah dipanggil")
    time.sleep(0.5)

print()
print("Yang mengantri sekarang ada:", my_q.size(), "Orang")
print("Yang paling depan adalah:", my_q.peekfront())


