# 11 - 01 - 2019, Belajar tentang oop (bagian class)

class ayam:
    # atribut kelas
    species = "Bird"
    # menginisiasi / instance Attributes

    def __init__(self)(self, name, age):
        self.name = name
        self.age = age

# Instantiate The Ayam object
Rambo = ayam("Rambo", 12)

# Access the instance attributes
print("{} and {}".format(Rambo.name, Rambo.age))

