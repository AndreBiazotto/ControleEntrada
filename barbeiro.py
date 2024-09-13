from time import sleep

class Barbeiro():
    def __init__(self):
        self.ocupado = False

    def cortarCabelo(self, user):
        print(f"Cabelo de {user} sendo cortada")
        sleep(3)
        print("Cabelo cortada")

    def cortarBarba(self, user):
        print(f"Barba de {user} sendo cortada")
        sleep(4)
        print("Barba cortada")

    def cortarBigode(self, user):
        print(f"Bigode de {user} sendo cortada")
        sleep(5)
        print("Bigode cortada")