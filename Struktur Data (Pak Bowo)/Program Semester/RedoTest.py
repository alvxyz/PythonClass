class Stack:
    stack_list = []
    stack_redo = []
    max_size = 0
    top = 0

    def __init__(self):
        max_size = 20
        self.stack_list = [" "] * max_size
        self.redo = [0] * max_size
        self.top = -1

    def push(self, perintah):
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
        return self.stack_list

    def redo(self):
        return self.pop()


import time


def mainprogram():
    photoshop = Stack()
    quit = False

    print(""" =========PROGRAM PHOTOSHOP SEDERHANA============

        List Perintah yang dapat digunakan
        - Blur = Menghilangkan fokus objek
        - Crop = Memotong Objek
        - Undo = Mengembalikan proses sebelumnya

        - Delete = Menghapus layer / efek
        - Quit = Keluar dari program
        - History = Menampilkan perintah yang telah di buat
        """)

    while not quit:

        perintah = input("Photoshop > ".lower())

        if perintah == "blur":
            photoshop.push(perintah)
            print("Mengaktifkan Blur, objek Anda akan kehilangan Fokus")
        elif perintah == "crop":
            photoshop.push(perintah)
            print("Memotong objek yang telah di pilih")
        elif perintah == "delete":
            photoshop.push(perintah)
            print("Menghapus objek yang dipilih")
        elif perintah == "undo":
            if not photoshop.is_full():
                print("Perintah", photoshop.peek_top().capitalize(), "dibatalkan")
                photoshop.pop()
            else:
                print("Tidak ada perintah yang tersedia untuk di Undo")
        elif perintah == "history":
            print(photoshop.histori())
        elif perintah == "quit":
            quit = True
            time.sleep(1.5)
            print("""
            ====== Terima Kasih telah menggunakan Program Photoshop Sederhana ini ======
            """)
        else:
            print("Perintah tidak dikenali")


mainprogram()
