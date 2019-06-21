# 11 - 01 - 2019, Belajar tentang oop (bagian class)

class Ayam:
    # atribut kelas
    species = "Bird"
    # menginisiasi / instance Attributes
    def __init__(self, name, age, color, speed, power):
        self.name = name
        self.age = age
        self.color = color
        self.speed = speed
        self.power =  power

# Instantiate The Ayam object
rambo = Ayam("Rambo", 9, "Green", 81, 65)
jambul = Ayam("Jambul", 10, "Red", 70, 90)
jolio = Ayam("Jolio", 11, "Blue", 99, 99)

def get_biggest_number(*args):
    return max(args)

# Access the instance attributes
print("{} Ages is: {} \n have a {} Color \n Speed: is {}\n and Power: {}".format(rambo.name, rambo.age, rambo.color, rambo.speed, rambo.power))
# is Rambo a Bird?
if rambo.species == "Bird":
    print("\n{0} is a {1}!".format(rambo.name, rambo.species))
    print("Rambo is ",rambo.name)

print("The oldest Ayam is {} years old.".format(get_biggest_number(rambo.age, jambul.age, jolio.age)))
print("Yang paling tua adalah: ",get_biggest_number(rambo.name, jambul.name, jolio.name))