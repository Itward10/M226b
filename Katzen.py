from Tier import Tier
class Katzen(Tier):
    tatzen_grösse = 0

    def __init__(self, tatzen_grösse, rasse, geschlecht, alter):
        super(Katzen, self).__init__(rasse, geschlecht, alter)
        self.tatzen_grösse = tatzen_grösse

print("")
print("---Unsere Katzen---")
k1 = Katzen(10, "Bengal Cat", "Männlich", 3)
k1.printRasse()
k1.printAlter()
k1.printGeschlecht()
