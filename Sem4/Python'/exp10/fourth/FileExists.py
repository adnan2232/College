import os
from pathlib import Path
if os.path.exists("Adnan.txt"):
    print("YES, The file does exist")
else:
    print("NO, The file does not exist\nCreating a new file called Adnan.txt")
    f1  = open("Adnan.txt","w+")
    print("Writing something in Adnan.txt")
    f1.write("Well well what do we have we here")
    print("Closing the file.....")
    f1.close()
