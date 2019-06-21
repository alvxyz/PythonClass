def main():
    print(
        """          _______________________________________________________  
            |     Program untuk mengurutkan data yang acak     |
            |                                                  |
            |                  =====MENU=====                  |
            |                                                  |
            |   1. Bubble Sort              4. Insetion Sort   |
            |   2. Exchange Sort                               |
            |   3. Selection Sort                              |              
            |                                                  |
            |__________________________________________________|                                                
                                                            """)

    pilihan = int(input("Masukkan metode sorting yang Anda inginkan (1-4): "))

    data = [int(s) for s in input("Masukan angka yang akan diurutkan dipisah dengan 'Spasi' : ").split()]

    def bubble_sort(data):
        for indeks in range(len(data) - 1, -1, -1):
            swapped = False
            for indeks2 in range(0, indeks):
                if data[indeks2] > data[indeks2 + 1]:
                    data[indeks2], data[indeks2 + 1] = data[indeks2 + 1], data[indeks2]
                    swapped = True
            if swapped is False:
                break

        print()
        print("===Angka setelah di urutkan dengan Bubble Sort===")
        print(data)

    def exchange_sort(data):
        for pivot in range(0, len(data) - 1):  # exchange sort in action
            for i in range(pivot + 1, len(data)):
                if data[i] < data[pivot]:
                    data[i], data[pivot] = data[pivot], data[i]
        print()
        print("===Angka setelah di urutkan dengan Exchange Sort===")
        print(data)

    def selection_sort(data):
        for proses in range(0, len(data) - 1):
            # print(proses)
            terkecil = proses  # inisialisasi nilai awal
            for indeks in range(proses + 1, len(data)):
                if data[indeks] < data[terkecil]:
                    terkecil = indeks
            data[proses], data[terkecil] = data[terkecil], data[proses]
        print()
        print("===Angka setelah di urutkan dengan Selection Sort===")
        print(data)

    def insertion_sort(data):
        for i in range(len(data) - 1):
            proses = i + 1
            for j in range(i + 1, 0, -1):
                if data[proses] < data[j - 1]:
                    data[proses], data[j - 1] = data[j - 1], data[proses]
                    proses = j - 1
        print()
        print("===Angka setelah di urutkan dengan Insertion Sort===")
        print(data)

    if pilihan == 1:
        bubble_sort(data)
    elif pilihan == 2:
        exchange_sort(data)
    elif pilihan == 3:
        selection_sort(data)
    elif pilihan == 4:
        insertion_sort(data)
    else:
        print("Maaf Anda salah memasukkan nomer pilihan")

    pilihan = ["Yes", "yes", "Ya", "ya", "Y", "y", "boleh", "ok", "oke"]

    print()
    restart = input("Apakah Anda ingin menggunakan program selection lagi?   ")

    if restart in pilihan:
        main()

    else:
        print("Terima Kasih telah menggunakan program ini")
        exit()


main()
