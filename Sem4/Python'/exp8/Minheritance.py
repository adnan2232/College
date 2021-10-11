
class Father:
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
class Mother:
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 

class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
s1 = Son()  # Object of Son class
s1.fathername = "Joseph Joester"
s1.mothername = "Lily"
s1.show_parent()