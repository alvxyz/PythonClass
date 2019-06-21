class Student:
    def __init__(self, nilai1, nilai2):
        self.nilai1 = nilai1
        self.nilai2 = nilai2

    # def JumlahNilai(self, a=None, b=None, c=None):
    #     hasil = 0
    #     if a!= None and b!=None and c!= None:
    #         hasil = a+b+c
    #     # elif a!= None and b!= None:
    #     #     hasil = a+b
    #     # else:
    #     #     hasil = a
    #
    #     return hasil
    def JumlahNilai(self, a, b, c):
        hasil = a+b+c
        return hasil

    def JumlahNilai(self, a, b):
        hasil = a+b
        return hasil

    def JumlahNilai(self,a):
        hasil = a
        return hasil

labo = Student(90, 100)

print(labo.JumlahNilai(12, 12))
