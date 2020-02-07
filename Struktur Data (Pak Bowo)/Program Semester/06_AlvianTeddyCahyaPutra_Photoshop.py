class Stack:
    # variabel local
    stack_list = []
    stack_redo = []
    max_size = 0
    top = 0

    # konstruktor dengan parameter size
    def __init__(self, size):
        self.max_size = size
        self.stack_list = [0] * self.max_size
        # nilai top -1 dikarenakan slot tumpukan pertama [indeks 0] belum di isi
        self.top = -1

    def push(self, perintah):
        # nilai top bergeser, seiiring dengan dimasukkan data baru
        self.top += 1
        self.stack_list[self.top] = perintah

    def pop(self):
        temp = self.stack_list[self.top]
        # nilai top berkurang
        self.top -= 1
        return temp

    def is_empty(self):
        # melakukan cek apakah nilai top seperti keadaan pertama (sebelum data masuk)
        return self.top == -1

    def is_full(self):
        # melakukan cek apakah nilai top sama dengan nilai maksimum (dikurangi 1 karena indeks mulai dari 0)
        return self.top == self.max_size - 1

    def peek_top(self):
        # mengembalikan nilai pada list yang berada di indeks top
        return self.stack_list[self.top]

    def histori(self):
        print("History: ")
        # melakukan perulangan untuk menampilkan isi list (top + 1 dikrenanan aturan dalam range)
        for i in range(0, self.top + 1):
            print("-", self.stack_list[i].capitalize())


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

    while not Quit:

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
