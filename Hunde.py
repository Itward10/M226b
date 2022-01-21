from Tier import Tier
class Hunde(Tier):
    tatzen_grösse = 0

    def __init__(self, tatzen_grösse, rasse, geschlecht, alter):
        super(Hunde, self).__init__(rasse, geschlecht, alter)
        self.tatzen_grösse = tatzen_grösse


def Hundeausgeben():
    print("---Unsere Hunde---")
    h1 = Hunde(10, "Dackel", "Männlich", 5)
    h1.printRasse()
    h1.printAlter()
    h1.printGeschlecht()
    print(" ")

    h2 = Hunde(9, "Pudel", "Weiblich", 12)
    h2.printRasse()
    h2.printAlter()
    h2.printGeschlecht()
    print(" ")

    h3 = Hunde(7, "Bulldog", "Männlich", 5)
    h3.printRasse()
    h3.printAlter()
    h3.printGeschlecht()
    print(" ")

    h4 = Hunde(9, "Bernhardiner", "Weiblich", 6)
    h4.printRasse()
    h4.printAlter()
    h4.printGeschlecht()
    print("")
    print("")
    print("")
    print("")