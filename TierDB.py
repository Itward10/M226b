from Katzen import Katzen
from Hunde import Hunde
from Reptilien import Reptilien
from Voegel import Voegel
class TierDB():
    Tierliste= []


    def __init__(self):
        k1 = Katzen(10, "Bengal Katze", "Männlich", 3)
        self.Tierliste.append(k1)
        k2 = Katzen(10, "Birma Katze", "Weiblich", 2)
        self.Tierliste.append(k2)
        k3 = Katzen(10, "Langhaar Katze", "Weiblich", 4)
        self.Tierliste.append(k3)
        k4 = Katzen(10, "Kurzhaar Katze", "Weiblich", 3)
        self.Tierliste.append(k4)

        h1 = Hunde(10, "Dackel", "weiblich", 3)
        self.Tierliste.append(h1)

        r1 = Reptilien(10, "Leopardgecko", "Männlich", 6)
        self.Tierliste.append(r1)

        v1 = Voegel(10, "Kanarienvogel", "Weiblich", 4)
        self.Tierliste.append(v1)

    def Katzenausgabe(self):
        for x in self.Tierliste:
            if type(x) == Katzen:
                x.printRasse()
                x.printAlter()
                x.printGeschlecht()

    def Katzenhinzufuegen(self, tatzen_groesse, rasse, geschlecht, alter):
        k4 = Katzen(tatzen_groesse, rasse, geschlecht, alter)
        self.Tierliste.append(k4)

    def Katzenhinzufuegen2(self, katze):
        self.Tierliste.append(katze)



    def Hundeausgabe(self):
        for x in self.Tierliste:
            if type(x) == Hunde:
                x.printRasse()

DB = TierDB()
#DB.Katzenausgabe()
DB.Hundeausgabe()
DB.Katzenhinzufuegen(10, "Langhaar Katze", "Weiblich", 4)
k = Katzen(10, "Langhaar Katze", "Weiblich", 4)
DB.Katzenhinzufuegen2(k)
DB.Katzenausgabe()
