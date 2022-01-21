from Tier import Tier
class Reptilien(Tier):
    tatzen_grösse = 0

    def __init__(self, tatzen_grösse, rasse, geschlecht, alter):
        super(Reptilien, self).__init__(rasse, geschlecht, alter)
        self.tatzen_grösse = tatzen_grösse


def Reptilienausgeben():
    print("---Unsere Reptilien---")
    r1 = Reptilien(10, "Leopardgecko", "Weiblich", 7)
    r1.printRasse()
    r1.printAlter()
    r1.printGeschlecht()
    print(" ")

    r2 = Reptilien (10, "Helmkopfgecko", "Männlich", 2)
    r2.printRasse()
    r2.printAlter()
    r2.printGeschlecht()
    print(" ")


    r3 = Reptilien(10, "Siamesischer Grümaugengecko", "Männlich", 1)
    r3.printRasse()
    r3.printAlter()
    r3.printGeschlecht()
    print(" ")

    r4 = Reptilien(10, "Goldgecko", "Männlich", 3)
    r4.printRasse()
    r4.printAlter()
    r4.printGeschlecht()
    print(" ")

