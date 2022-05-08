#MUSHFIQUR RAHMAN
#TP059649


def warehouseContent(name):    
    while True:
        choice = input("ENTER 1 TO CONTINUE OR 999 TO END: ")
        if choice != "1":
            break
        else:
            content = []
            data = []
            file = []
            supplierInfo = []
            partID = input("ENTER PART ID: ")
            fileHandler = open(name+".txt","r")
            info = fileHandler.read()
            if partID in info:
                print("PARTID ALREADY EXIST")
                fileHandler.close()
                continue
            else:
                data.append(partID)
                supplierInfo.append(partID)
                partQuantity = input("ENTER PART QUANTITY IN WAREHOUSE: ")
                data.append(partQuantity)
                assemblySection = input("ENTER ASSEMBLY SECTION: ")
                data.append(assemblySection)
                partDistributed = input("ENTER PART QUANTITY GIVEN TO ASSEMBLY SECTION: ")
                data.append(partDistributed)
                supplierID = input("ENTER SUPPLIER ID: ")
                data.append(supplierID)
                supplierInfo.append(supplierID)
                supplierName = input("ENTER SUPPLIER NAME: ")
                supplierInfo.append(supplierName)
                supplierContact = input("ENTER SUPPLIER CONTACT NO.: ")
                supplierInfo.append(supplierContact)
                file.append(supplierInfo)
                content.append(data)
                fileHandler.close()
            fileHandler = open(name+".txt","a")
            for record in content:
                for item in record:
                    fileHandler.write(item)
                    fileHandler.write("\t")
                fileHandler.write('\n')
            fileHandler.close()
            fileHandler = open("SUPPLIER_INFO.txt","a")
            for line in file:
                for thing in line:
                    fileHandler.write(thing)
                    fileHandler.write("\t")
                fileHandler.write('\n')
            fileHandler.close()


def add(x,y):
    ans = str(int(x)+int(y))
    return ans
def subtract(x,y):
    ans = str(int(x)-int(y))
    return ans

def update(name):
    while True:
        choice = input("ENTER 1 TO CONTINUE OR 999 TO END: ")
        if choice != "1":
            break
        else:
            fileHandler = open(name+'.txt','r')
            data = fileHandler.readlines()
            newData = []
            updateItem = input("ENTER PART ID: ")
            try:
                quantity = input("ENTER QUANTITY: ")
                quantity = int(quantity)
            except:
                print("ENTER VALUE ONLY TRY AGAIN")
                continue
            updateChoice = input("\t1.RECEIVE FROM SUPPLIER\n\t2.DISTRIBUTE TO ASSEMBLY\nENTER CHOICE:")
            if updateChoice == "1":
                for line in data:
                    line = line.strip()
                    newLine = line.split("\t")
                    if newLine[0] == updateItem:
                        newLine[1] = add(quantity,newLine[1])
                        newData.append(newLine)
                    else:
                        newData.append(newLine)
            elif updateChoice == "2":
                for line in data:
                    line = line.strip()
                    newLine = line.split("\t")
                    if newLine[0] == updateItem:
                        if int(newLine[1])>=int(quantity):
                            newLine[1] = subtract(newLine[1],quantity)
                            newLine[3] = add(quantity,newLine[3])
                            newData.append(newLine)
                        else:
                            print("NOT ENOUGH QUANTITY AVAILABLE IN WAREHOUSE")
                            newData.append(newLine)
                    else:
                        newData.append(newLine)
            else:
                print("INVALID INPUT")
                fileHandler.close()
                continue
              
            fileHandler.close()

            fileHandler = open(name+'.txt','w')
            newData.sort()
            for line in newData:
                for item in line:
                    fileHandler.write(item)
                    fileHandler.write("\t")
                fileHandler.write("\n")
            fileHandler.close()

def trackAllParts(name):
    fileHandler = open(name+".txt","r")
    data = fileHandler.readlines()
    data = sorted(data)
    print("PARTSID/AVAILABLE QUANTITY IN WAREHOUSE/ASSEMBLY SECTION/NUMBER OF PARTS GIVEN TO THE ASSEMBLY SECTION/SUPPLIERID")
    for line in data:
        line = line.strip()
        print(line)
    fileHandler.close()


def trackPartsLessThan10(name):
    fileHandler = open(name+".txt","r")
    data = fileHandler.readlines()
    data = sorted(data)
    print("PARTSID/AVAILABLE QUANTITY IN WAREHOUSE/ASSEMBLY SECTION/",
          "NUMBER OF PARTS GIVEN TO THE ASSEMBLY SECTION/SUPPLIERID")
    for line in data:
        line = line.strip()
        newLine = line.split("\t")
        if int(newLine[1])<10:
            print(line)
        
    fileHandler.close()


def searchAPart(name):
    while True:
        choice = input("ENTER 1 TO CONTINUE OR 999 TO END: ")
        if choice != "1":
            break
        else:
            fHand = open(name+".txt","r")
            data = fHand.readlines()
            data = sorted(data)
            searchPart = input("ENTER PART ID THAT YOU WANT TO SEARCH: ")
            print("PARTSID/AVAILABLE QUANTITY IN WAREHOUSE/ASSEMBLY SECTION/",
                  "NUMBER OF PARTS GIVEN TO THE ASSEMBLY SECTION/SUPPLIERID")
            count = 0
            for line in data:
                line = line.strip()
                if line.startswith(searchPart):
                    print(line)
                    count = count + 1
            if count == 0:
                print("PART ID NOT FOUND")

            fHand.close()


def supplierDetails():
    while True:
        choice = input("ENTER 1 TO CONTINUE OR 999 TO END: ")
        if choice != "1":
            break
        else:
            fileHand = open("SUPPLIER_INFO.txt","r")
            data = fileHand.readlines()
            data = sorted(data)
            searchSuppDetails = input("ENTER PART ID THAT YOU WANT SUPPLIER DETAILS FOR: ")
            print("PARTSID/SUPPLIERID/SUPPLIER NAME/SUPPLIER CONTACT NO.")
            count = 0
            for line in data:
                line = line.strip()
                if line.startswith(searchSuppDetails):
                    print(line)
                    count = count + 1
            if count == 0:
                print("PART ID NOT FOUND")

            fileHand.close()


def partsGivenBySupplier():
    while True:
        choice = input("ENTER 1 TO CONTINUE OR 999 TO END: ")
        if choice != "1":
            break
        else:
            fileHand = open("SUPPLIER_INFO.txt","r")
            data = fileHand.readlines()
            data = sorted(data)
            suppID = input("ENTER SUPPLIER ID: ")
            print("PARTSID/SUPPLIERID/SUPPLIER NAME/SUPPLIER CONTACT NO.")
            count = 0
            for line in data:
                line = line.strip()
                if suppID in line:
                    print(line)
                    count = count + 1
            if count == 0:
                print("SUPPLIER ID NOT FOUND")

            fileHand.close()


def mainMenu():
    print("AUTOMOBILE PART INVENTORY MANAGEMENT SYSTEM")
    while True:
        print("MAIN MENU")
        print("\t1.RECORD NEW PARTS\n\t2.UPDATE PARTS QUANTITY\n\t3.TRACK PARTS INVENTORY\n\t4.SEARCH\n\t5.EXIT")
        option = input("ENTER CHOICE: ")
        if option == "1":
            print("WHICH WAREHOUSE DO YOU WANT TO ADD PARTS?")
            print("\t1.Bios\n\t2.Ambry\n\t3.Barrier")
            option_1 = input("SELECT WAREHOUSE: ")
            if option_1 == "1":
                name = "WBS_INVENTORY"
                warehouseContent(name)
            elif option_1 == "2":
                name = "WAY_INVENTORY"
                warehouseContent(name)
            elif option_1 == "3":
                name = "WBR_INVENTORY"
                warehouseContent(name)
            else:
                print("INVALID INPUT")
        elif option == "2":
            print("WHICH WAREHOUSE DO YOU WANT TO UPDATE PARTS QUANTITY?")
            print("\t1.Bios\n\t2.Ambry\n\t3.Barrier")
            option_2 = input("SELECT WAREHOUSE: ")
            if option_2 == "1":
                name = "WBS_INVENTORY"
                update(name)
            elif option_2 == "2":
                name = "WAY_INVENTORY"
                update(name)
            elif option_2 == "3":
                name = "WBR_INVENTORY"
                update(name)
            else:
                print("INVALID INPUT")
        elif option == "3":
            print("WHICH WAREHOUSE DO YOU WANT TO TRACK PARTS?")
            print("\t1.Bios\n\t2.Ambry\n\t3.Barrier")
            option_3 = input("SELECT WAREHOUSE: ")
            if option_3 == "1":
                print("1.TRACK ALL PARTS\n2.TRACK PARTS LESS THAN 10")
                select_1 = input("ENTER CHOICE: ")
                # input()

                if select_1 == "1":
                    name = "WBS_INVENTORY"
                    trackAllParts(name)
                    # input()
                elif select_1 == "2":
                    name = "WBS_INVENTORY"
                    trackPartsLessThan10(name)
                else:
                    print("INVALID INPUT")
            elif option_3 == "2":
                print("1.TRACK ALL PARTS\n2.TRACK PARTS LESS THAN 10")
                select_2 = input("ENTER CHOICE: ")
                if select_2 == "1":
                    name = "WAY_INVENTORY"
                    trackAllParts(name)
                elif select_2 == "2":
                    name = "WAY_INVENTORY"
                    trackPartsLessThan10(name)
                else:
                    print("INVALID INPUT")
            elif option_3 == "3":
                print("1.TRACK ALL PARTS\n2.TRACK PARTS LESS THAN 10")
                select_3 = input("ENTER CHOICE: ")
                if select_3 == "1":
                    name = "WBR_INVENTORY"
                    trackAllParts(name)
                elif select_3 == "2":
                    name = "WBR_INVENTORY"
                    trackPartsLessThan10(name)
                else:
                    print("INVALID INPUT")
            else:
                print("INVALID INPUT")
        elif option == "4":
            print("1.SEARCH A PART\n2.SEARCH SUPPLIER DETAILS\n3.SEE PARTS SUPPLIED BY A SUPPLIER")
            searchOption = input("ENTER CHOICE: ")
            if searchOption == "1":
                print("WHICH WAREHOUSE DO YOU WANT TO SEARCH PARTS?")
                print("\t1.Bios\n\t2.Ambry\n\t3.Barrier")
                option_4 = input("SELECT WAREHOUSE: ")
                if option_4 == "1":
                    name = "WBS_INVENTORY"
                    searchAPart(name)
                elif option_4 == "2":
                    name = "WAY_INVENTORY"
                    searchAPart(name)
                elif option_4 == "3":
                    name = "WBR_INVENTORY"
                    searchAPart(name)
                else:
                    print("INVALID INPUT")
            elif searchOption == "2":
                supplierDetails()
            elif searchOption == "3":
                partsGivenBySupplier()
            else:
                print("INVALID INPUT")
        elif option == "5":
            print("YOU HAVE EXITED THE PROGRAM")
            break
        else:
            print("INVALID INPUT")
                
                
                
                    
mainMenu()
# input()






