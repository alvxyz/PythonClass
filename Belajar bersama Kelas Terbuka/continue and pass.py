number =  int(input("Masukan nilai i:" ))

for number in range (1,11):

    if number is 5:
        print("nilai number adalah",5)
        #break #: fungsinya untuk mengakhiri for (terminasi)
        continue #: fungsinya untuk melanjutkan ke step berikutnya
        # pass dummy looping
        print("cek bro 1")
    print('nilai saat ini adalah', number)
else:
    print("akhir dari loop")
#print("di luar loop")