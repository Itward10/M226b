from Tier import Tier
class Reptilien(Tier):
    tatzen_grösse = 0

    def __init__(self, tatzen_grösse, rasse, geschlecht, alter):
        super(Reptilien, self).__init__(rasse, geschlecht, alter)
        self.tatzen_grösse = tatzen_grösse


print("---Unsere Reptilien---")
r1 = Reptilien(10, "Leopardgecko", "Weiblich", 7)
r1.printRasse()
r1.printAlter()
r1.printGeschlecht()