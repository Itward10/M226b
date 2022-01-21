from Tier import Tier


class Katzen(Tier):
    tatzen_groesse = 0

    def __init__(self, tatzen_groesse, rasse, geschlecht, alter):
        super(Katzen, self).__init__(rasse, geschlecht, alter)
        self.tatzen_groesse = tatzen_groesse

    def tierLaut(self):
        print("Miau")

def Katzenausgeben():
    print("---Unsere Katzen---")
    k1 = Katzen (10, "Bengal Katze", "Männlich", 3)
    k1.printRasse()
    k1.printAlter()
    k1.printGeschlecht()
    print(" ")

    k2 = Katzen (10, "Birma Katze", "Weiblich", 4)
    k2.printRasse()
    k2.printAlter()
    k2.printGeschlecht()
    print(" ")

    k3 = Katzen (2, "Langhaar Katze", "Weiblich", 5)
    k3.printRasse()
    k3.printAlter()
    k3.printGeschlecht()
    print(" ")

    k4 = Katzen (3, "Kurzhaar Katze", "Männlich", 6)
    k4.printRasse()
    k4.printAlter()
    k4.printGeschlecht()
    print(" ")
    print(" ")
    print(" ")
    print(" ")
