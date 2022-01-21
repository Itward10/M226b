from Tier import Tier
class Voegel(Tier):
    tatzen_grösse = 0

    def __init__(self, tatzen_grösse, rasse, geschlecht, alter):
        super(Voegel, self).__init__(rasse, geschlecht, alter)
        self.tatzen_grösse = tatzen_grösse


def Voegelausgeben():
    print("---Unsere Voegel---")
    v1 = Voegel(10, "Wellensittich", "Weiblich", 7)
    v1.printRasse()
    v1.printAlter()
    v1.printGeschlecht()
    print(" ")

    v2 = Voegel(10, "Papagei", "Männlich", 1)
    v2.printRasse()
    v2.printAlter()
    v2.printGeschlecht()
    print(" ")

    v3 = Voegel(10, "Kanarienvogel", "Weiblich", 7)
    v3.printRasse()
    v3.printAlter()
    v3.printGeschlecht()
    print(" ")

    v1 = Voegel(10, "Zebrafink", "Weiblich", 3)
    v1.printRasse()
    v1.printAlter()
    v1.printGeschlecht()
    print(" ")
