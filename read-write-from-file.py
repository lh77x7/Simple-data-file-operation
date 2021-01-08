import os
import os.path

#function createFile
def createFile():
    if os.path.isfile('dataFile.txt'):
        print("\nFile exists")
    else:
        f=open("dataFile.txt", "x")
        print("\nFile created. Done")
        f.close()

#end function

#function readFile
def readFile():
    try:
        result=os.stat("dataFile.txt")
        if result.st_size!=1:
            print("\nFile is empty")
        else:
            f = open("dataFile.txt", "r")
            print (f.readlines())
            f.close()
    except FileNotFoundError:
        print("\nFile doesn't not exist")

#end function

#function overwriteFile
def overwriteFile():
    pass

#end function

#function deleteFile
def deleteFile():
    pass

#end function

print("------------------------------------")
print("Simple example operation on the file")
print("------------------------------------")
#main menu
while(True):
    print("\n1. Create file\n2. Read from file"
    "\n3. Overwrite file\n4. Delete file"
    "\n5. Exit")
    choice = int(input("Select 1,2,3,4 or 5: "))
    if choice==1:
        createFile()
    elif choice==2:
        readFile()
    elif choice==3:
        overwriteFile()
    elif choice==4:
        deleteFile()
    elif choice==5:
        break
    else:
        print("You can only select 1,2,3,4 or 5")
#end main menu
