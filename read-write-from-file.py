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
        f = open("dataFile.txt", "r")
        print (f.readlines())
        f.close()
    except FileNotFoundError:
        print("\nFile doesn't not exist")
        createFile()
        return

#end function

#function overwriteFile
def writeToFile():
    try:
        f = open("dataFile.txt", "a")
        f.writelines("\nNew content")
        f.close()
    except FileNotFoundError:
        print("\nFile doesn't not exist")
        createFile()
        return

#end function

#function deleteFile
def deleteFile():
    try:
        os.remove('dataFile.txt')
        print("\nFile deleted.")
    except FileNotFoundError:
        print("\nFile doesn\'t not exist. Nothing deleted.")

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
        writeToFile()
    elif choice==4:
        deleteFile()
    elif choice==5:
        break
    else:
        print("You can only select 1,2,3,4 or 5")
#end main menu
