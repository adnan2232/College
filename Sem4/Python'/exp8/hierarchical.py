
class Parent:
    parentname = ""
    childname = ""
 
    def show_parent(self):
        print("Parent Name: ",self.parentname)
 
 

class Son(Parent):
    def show_child(self):
        print("Son Name: ",self.childname)
 
 

class Daughter(Parent):
    def show_child(self):
        print("Daughter Name: ",self.childname)
 
 
s1 = Son()  
s1.parentname = "Cujoh"
s1.childname = "Jotaro"
s1.show_parent()
s1.show_child()
 
d1 = Daughter() 
d1.childname = "Jolyne"
d1.parentname = "Jotaro"
d1.show_parent()
d1.show_child()