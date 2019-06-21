class GameItem:
    price = 0
    weight = 0

    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

    def print_data(self):
        print("Price: {}\nWeight: {}\n".format(self.price, self.weight))
