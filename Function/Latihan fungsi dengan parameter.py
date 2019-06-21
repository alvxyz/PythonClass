# variabel lokal dan global

def halo(nama):
    print('Hallo %s!' %nama)

def cetak_maksimal(a,b):
    if a > b:
        print("%s merupakan nilai maksimal" %a)
    elif a == b:
        print("%s sama dengan %s" % (a,b))
    else:
        print("%s merupakan nilai maksimal" %b)

halo("Cantik") # ini bagian memanggil fungsi halo dengan argumen
halo('Ganteng') # memanggil fungsi halo dengan argumen Ganteng

cetak_maksimal(10,100)

x = 9
y = 3

cetak_maksimal(x,y)