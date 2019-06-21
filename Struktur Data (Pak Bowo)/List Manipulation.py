# x = [5,6,2,1,6,7,2,2,6,7,2,10]
# #
# # x.append(2)
# # x.insert(0,99)
# # Memotong list = print(x[5:7])
# # Mengetahui nomer indeks suatu list = print (x.index(1))
# # Mengetahui panjang suatu list dengan menggunakan len()
# # Menghitung banyak data yang ada di dalam suatu list = x.count(2)
# # Mengurutkan suatu data = x.sort
#
# print(x.count(2))
# print(len(x))
# print(x.index(10))
#
# x.sort()
#
# print(x)

players= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
vote = 0
cont = 0

while(vote >= 0 and vote <23):
    vote = int(input('Enter the name of the player you wish to vote for'))
    if (0 < vote <=24):
        players[vote +1] += 1;cont +=1
    else:
        print('Invalid vote, try again')