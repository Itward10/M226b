from Tier import Tier
class Menu:

    __Tier: Tier = None

    def showMenu (self):
        print("Bitte wählen sie:")
        print("k: Alle Katzen anzeigen")
        print("h: Alle Hunde anzeigen")
        print("r: Alle Reptilien anzeigen")
        print("v: Alle Vögel anzeigen")
        print("o: Ausloggen")
        print("x: Beenden")
        result: str = input()

        # Switch statements are more complicated in python. therefore we use if-elseif
        if result == "x":
            self.__exit()
        elif result == "k":
            self.__Katzen()
        elif result == "h":
            self.__Hunde()
        elif result == "a":
            self.__Reptilien()
        elif result == "v":
            self.__Voegel()


    def __Katzen(self):
        print(Katzen)

    def __Hunde(self):
        print(Hunde)

    def __Reptilien(self):
        print(Reptilien)

    def __Voegel(self):
        print(Voegel)

    def __exit(self):
        print("Wir wünschen ihnen einen schönen tag")
        exit()



