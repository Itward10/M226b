from Tier import Tier
from Katzen import Katzenausgeben
from Hunde import Hundeausgeben
from Reptilien import Reptilienausgeben
from Voegel import Voegelausgeben
class Menu:
    __Tier: Tier = None
    def __showMenu():
        loop = True
        while loop:

            print("Bitte wählen sie:")
            print("1: alle Katzen anzeigen")
            print("2: alle Hunde anzeigen")
            print("3: alle Reptilien anzeigen")
            print("4: alle Vögel anzeigen")
            print("5: Beenden")
            tierbuchstabeneingabe = str((input("Bitte wähle eine Zahl Zwischen 1-5:")))

            if tierbuchstabeneingabe == "1":
                Katzenausgeben()
            elif tierbuchstabeneingabe == "2":
                Hundeausgeben()
            elif tierbuchstabeneingabe == "3":
                Reptilienausgeben()
            elif tierbuchstabeneingabe == "4":
                Voegelausgeben()
            elif tierbuchstabeneingabe == "5":
                loop = False

    __showMenu()


