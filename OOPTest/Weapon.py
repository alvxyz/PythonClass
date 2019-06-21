from . import GameItem

class Weapon(GameItem):
    damage = 0

    def __init__(self, price, weight, damage):
        GameItem.__init__(self, price, weight)
        self.damage = damage

    def print_data(self):
        print("Price: {}\nWeight: {}\nDamage: {}".format(self.price, self.weight, self.damage))
