from Tier import Tier
class Hunde(Tier):
    tatzen_grösse = 0

    def __init__(self, tatzen_grösse, rasse, geschlecht, alter):
        super(Hunde, self).__init__(rasse, geschlecht, alter)
        self.tatzen_grösse = tatzen_grösse


print("---Unsere Hunde---")
h1 = Hunde(10, "Dackel", "Männlich", 5)
h1.printRasse()
h1.printAlter()
h1.printGeschlecht()