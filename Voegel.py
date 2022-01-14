from Tier import Tier
class Voegel(Tier):
    tatzen_grösse = 0

    def __init__(self, tatzen_grösse, rasse, geschlecht, alter):
        super(Voegel, self).__init__(rasse, geschlecht, alter)
        self.tatzen_grösse = tatzen_grösse


print("---Unsere Voegel---")
r1 = Voegel(10, "Wellensittich", "Weiblich", 7)
r1.printRasse()
r1.printAlter()
r1.printGeschlecht()