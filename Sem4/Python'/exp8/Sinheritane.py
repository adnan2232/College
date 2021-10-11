class Animal:
    def __init__(self):
        self.kingdomname = "Animalia"
    def kingdom(self):
        print("Kingdom: ",self.kingdomname)


class Cow(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Cow"
        self.voc = "Moooo"

    def naam(self):
        print("Name: ",self.name)
    
    def voice(self):
        print(f"{self.name} {self.voc}")


if __name__ == "__main__":
    cow1 = Cow()
    cow1.kingdom()
    cow1.naam()
    cow1.voice()