def main():
    bilangan = int(input("Masukan bilangan bulat: "))

    #memeriksa bilangan, genap atau tidak
    if bilangan % 2 == 0:
        print("%d adalah bilangan genap" % bilangan)
    elif bilangan % 2 != 0:
        print("%d adalah bilangan ganjil" % bilangan)

if __name__ == "__main__" :
    main()
