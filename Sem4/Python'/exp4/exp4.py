class Student:
    def __init__(self):
        self.tup = tuple() 

    def addinfo(self):
        roll, name  = int(input("Enter roll no: ")), input("Enter name: ")
        sub1, sub2, sub3 =  map(int,input("Enter Three subjects marks: ").strip().split())
        l = list(self.tup)
        l.append((roll,name,sub1,sub2,sub3))
        self.tup = tuple(l)
        print("Inserted Tuple:",self.tup[len(self.tup)-1])
    
    def fetchinfo(self):
        print(*[str(x)+"\n" for x in self.tup if x[1].lower() == "python"])

    def display(self):
        print(*[str(x)+"\n" for x in sorted(self.tup,key= lambda x: x[1])])
        

if __name__ == "__main__":
    stud = Student()
    while True:
        num = int(input("*********Menu Driven***************\n1. To add student information\n2. To fetch all students where, name == python \n3. To display all student information in sorted order.\n4. Exit\n"))
        if num == 1:
            stud.addinfo()
        elif num == 2:
            stud.fetchinfo()
        elif num == 3:
            stud.display()
        elif num ==4:
            break
        else:
            print("You pressed wrong key please try again")