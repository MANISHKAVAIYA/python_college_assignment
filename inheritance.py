class TATA:
    def tata(self):
        print("Tata Safari")


class Jaguar(TATA):
    def jaguar(self):
        print("JAGUAR F-PACE")


class LandRover(Jaguar):
    def land_rover(self):
        print("Range Rover")


lr = LandRover()
lr.tata()
