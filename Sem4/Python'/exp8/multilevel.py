class Family:
    def show_family(self):
        print("This is Cujoh Family:")
 
 

class Father(Family):
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
 

class Mother(Family):
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 

class Child(Father, Mother):
    def __init__(self):
        super().__init__()
        self.childname = "" 
    def show_parent(self):
        print("Son name: ",self.childname)
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
if __name__ == "__main__": 
	s1 = Child()
	s1.childname = "Jotaro Cujoh"
	s1.fathername = "Sadao Cujoh"
	s1.mothername = "Holy Cujoh"
	s1.show_family()
	s1.show_parent()