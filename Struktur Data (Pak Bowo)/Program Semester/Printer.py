class Printer:
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
    def enqueue(self, perintah):
        self.rear += 1
        self.q_list[self.rear] = perintah
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

    def list(self):
        print("List antrian: ")
        for i in range(0, self.rear + 1):
            print(self.q_list[i], end=" ")
        print()

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


def mainProgram():
    printer = Printer(10)
    Quit = False

    print("""
    Welcome to the Printer Center.
    Your Printer Center version is v 3.9
    Copyright (c) 2019, Alvian, Alvxyz Corporation and others.
    
    List perintah yang dapat digunakan
    
    - Print = Melakukan proses pencetakakn
    - List = Mengecek antrian proses
    - Done = Menyelesaikan proses dokumen pertama di antrian
    - Quit = Keluar dari program 
    
    """)

    while not Quit:

        perintah = input("Printer Center [v 3.9] > ")

        if not printer.is_full():
            if perintah == "print":
                nama_dokumen = input("Masukkan nama dokumen: ")
                printer.enqueue(nama_dokumen)
                print("Memasukkan", nama_dokumen, "ke dalam antrian")
            elif perintah == "list":
                printer.list()
            elif perintah == "done":
                print(printer.peekfront(), "telah selesai di cetak")
                printer.dequeue()
            elif perintah == "quit":
                Quit = True
                print("""
                ====== Terima Kasih telah menggunakan Program Printer Sederhana ini ======
                """)
            else:
                print("Perintah tidak dikenali")


mainProgram()
