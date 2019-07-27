class Stack:
    # Variabel Global
    stack_list = []
    max_size = 0
    top = 0

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


import random
import time

mystack = Stack(10)

# for x in range(5, 1005, 5):
#     mystack.push(x)

while (not mystack.is_full()):
    angka_random = random.randrange(0, 100, 5)
    print(f"Memasukkan {angka_random} ke dalam Stack")
    time.sleep(0.2)
    mystack.push(angka_random)


# melakukan penghapusan data dan nilai indeksnya dimulai dari -1
# mystack.clear()


mystack.push(100)
print("Indeks top sekarang berada di", mystack.peek_top())

while not mystack.is_empty():
    print("Data yang diambil", mystack.pop())



# print("Indeks top sekarang berada di", mystack.peek_top())
