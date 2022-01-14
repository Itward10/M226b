class Tier:
    rasse = ""
    geschlecht = ""
    alter = 0
    name = ""

    def __init__(self, rasse, geschlecht, alter):
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printRasse(self):
        print('Rasse: ', self.rasse)

    def printGeschlecht(self):
        print("Geschlecht: ", self.geschlecht)

    def printAlter(self):
        print("Alter:", self.alter)



