class Bapak:
    def Motor(self):
        print("Bapak mempunyai motor ninja")
class Anak(Bapak):
    def Motor(self):
        super().Motor()
        print("Anak mempunyai motor ninja punya bapaknya")

jono = Anak()

jono.Motor()