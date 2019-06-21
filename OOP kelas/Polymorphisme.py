# 23-1-2019 Rabu

class Hiu():
    def renang(self):
        print("Hiu sedang bernang")
    def renang_mundur(self):
        print("Hiu tidak bisa berenang mundur")
    def rangka(self):
        print("Rangka hiu terbuat dari tulang rawan")

class IkanBadut():
    def renang(self):
        print("Ikan badut sedang berenang")
    def renang_mundur(self):
        print("Ikan badut dapat berenang mundur")
    def rangka(self):
        print("Rangka Ikan badut terbuat dari tulang keras")

# contoh polymorphisme
sammy = Hiu()
nemo = IkanBadut()

# for fish in (sammy, nemo):
#     fish.renang()
#     fish.renang_mundur()
#     fish.rangka()

sammy.renang_mundur()
nemo.renang_mundur()