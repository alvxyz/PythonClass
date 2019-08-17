class Stack:
    stack_list = []
    stack_redo = []
    max_size = 0
    top = 0

    def __init__(self, size):
        self.max_size = size
        self.stack_list = [" "] * self.max_size
        self.top = -1

    def push(self, perintah):
        # if not self.is_full():
        self.top += 1
        self.stack_list[self.top] = perintah

    def pop(self):
        temp = self.stack_list[self.top]
        self.top -= 1
        return temp

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def peek_top(self):
        return self.stack_list[self.top]

    def histori(self):
        print("History: ")
        for i in range(0, self.top + 1):
            print(self.stack_list[i].capitalize(), end=" ")
        print()

    def redo(self):
        temp = self.stack_list[self.top + 1]
        self.top += 1
        return temp


import time


def mainprogram():
    photoshop = Stack(20)
    Quit = False

    print("""         
    Welcome to the Photoshop.
    Your Photoshop version is CC 2019
    Copyright (c) 2019, Alvian, Alvxyz Corporation and others.

    List perintah yang dapat digunakan
    
    - Blur = Menghilangkan fokus objek
    - Crop = Memotong Objek
    - Undo = Mengembalikan proses sebelumnya
    - Delete = Menghapus layer / efek
    - History = Menampilkan perintah yang telah di buat
    - Quit = Keluar dari program
    """)

    while not quit:

        perintah = input("Photoshop [CC 2019] > ")

        if perintah == "blur":
            if not photoshop.is_full():
                photoshop.push(perintah)
                print("Mengaktifkan Blur, objek Anda akan kehilangan Fokus")
            else:
                print("Maaf Perintah Melewati batas maksimal")

        elif perintah == "crop":
            if not photoshop.is_full():
                photoshop.push(perintah)
                print("Memotong objek yang telah di pilih")
            else:
                print("Maaf Perintah Melewati batas maksimal")

        elif perintah == "delete":
            if not photoshop.is_full():
                photoshop.push(perintah)
                print("Menghapus objek yang dipilih")
            else:
                print("Maaf Perintah Melewati batas maksimal")

        elif perintah == "undo":
            if photoshop.is_empty():
                print("Tidak ada perintah yang tersedia untuk di Undo")
            elif not photoshop.is_full():
                print("Perintah", photoshop.peek_top().capitalize(), "dibatalkan")
                photoshop.pop()

        elif perintah == "history":
            photoshop.histori()

        elif perintah == "quit":
            Quit = True
            time.sleep(1.5)
            print("""
            ====== Terima Kasih telah menggunakan Program Photoshop Sederhana ini ======
            """)
        else:
            print("Perintah tidak dikenali")


mainprogram()
